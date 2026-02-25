"""
Obsidian Skill 管理器
> 小酷 (CTO) 实现 | 负责 Skill 的发现、加载、执行、验证
"""

import os
import re
import json
import yaml
import frontmatter
import importlib.util
import asyncio
from pathlib import Path
from typing import Dict, List, Optional, Any, Callable
from dataclasses import dataclass
from datetime import datetime
import httpx

# --- [小酷 CTO 核定配置] ---
CONFIG = {
    "VAULT_PATH": "/Volumes/Cabinet/cabinet/obsidian_vault",  # 【请修改：你的 Obsidian Vault 路径】
    "SKILLS_DIR": "Skills",
    "REGISTRY_FILE": "Skills/.registry.md",
    "3090_API_URL": "http://101.43.29.236:8189/v1/chat/completions",
    "3090_MODEL": "internlm3-8b-instruct"
}


@dataclass
class SkillMetadata:
    """Skill 元数据"""
    skill_id: str
    skill_name: str
    skill_version: str
    skill_type: str
    skill_category: str
    depends_on: List[str]
    inputs: List[Dict]
    outputs: List[Dict]
    execution: Dict
    author: str
    created_at: str
    tags: List[str]
    permissions: Dict
    file_path: str


@dataclass
class Skill:
    """Skill 对象"""
    metadata: SkillMetadata
    code: str
    execute_func: Optional[Callable] = None


class SkillManager:
    """Skill 管理器"""
    
    def __init__(self, vault_path: Optional[str] = None):
        """
        初始化 Skill 管理器
        
        Args:
            vault_path: Obsidian Vault 路径，默认使用 CONFIG 中的路径
        """
        self.vault_path = Path(vault_path or CONFIG["VAULT_PATH"])
        self.skills_dir = self.vault_path / CONFIG["SKILLS_DIR"]
        self.registry_file = self.vault_path / CONFIG["REGISTRY_FILE"]
        self.skills_cache: Dict[str, Skill] = {}
        self._ensure_directories()
    
    def _ensure_directories(self):
        """确保必要的目录存在"""
        categories = ["Core", "Analysis", "Automation", "Integration", "Custom"]
        for category in categories:
            (self.skills_dir / category).mkdir(parents=True, exist_ok=True)
        self.registry_file.parent.mkdir(parents=True, exist_ok=True)
    
    def discover(self) -> List[str]:
        """
        发现所有 Skill 文件
        
        Returns:
            List[str]: Skill 文件路径列表
        """
        skill_files = []
        for category_dir in self.skills_dir.iterdir():
            if category_dir.is_dir() and not category_dir.name.startswith('.'):
                for md_file in category_dir.glob("*.md"):
                    if md_file.name != ".registry.md":
                        skill_files.append(str(md_file))
        return skill_files
    
    def _parse_frontmatter(self, file_path: Path) -> Dict:
        """解析 YAML frontmatter"""
        with open(file_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
            return post.metadata
    
    def _extract_code_block(self, content: str) -> Optional[str]:
        """提取代码块中的 Python 代码"""
        # 查找 ```python 或 ```python:skill 代码块
        pattern = r'```python(?::skill)?\n(.*?)```'
        matches = re.findall(pattern, content, re.DOTALL)
        if matches:
            return matches[0].strip()
        return None
    
    def _compile_skill_code(self, code: str, skill_id: str) -> Callable:
        """编译 Skill 代码并返回 execute 函数"""
        # 创建临时模块
        spec = importlib.util.spec_from_loader(skill_id, loader=None)
        module = importlib.util.module_from_spec(spec)
        
        # 执行代码（在模块命名空间中）
        exec(code, module.__dict__)
        
        # 获取 execute 函数
        if not hasattr(module, 'execute'):
            raise ValueError(f"Skill {skill_id} 必须定义 execute 函数")
        
        return module.execute
    
    def validate(self, file_path: str) -> tuple[bool, List[str]]:
        """
        验证 Skill 文件格式
        
        Returns:
            (bool, List[str]): (是否有效, 错误列表)
        """
        errors = []
        file_path_obj = Path(file_path)
        
        if not file_path_obj.exists():
            return False, [f"文件不存在: {file_path}"]
        
        try:
            # 解析 frontmatter
            metadata = self._parse_frontmatter(file_path_obj)
            
            # 检查必需字段
            required_fields = [
                "skill_id", "skill_name", "skill_version", 
                "skill_type", "skill_category"
            ]
            for field in required_fields:
                if field not in metadata:
                    errors.append(f"缺少必需字段: {field}")
            
            # 检查代码块
            with open(file_path_obj, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
                code = self._extract_code_block(post.content)
                if not code:
                    errors.append("缺少 Python 代码块")
                elif 'def execute' not in code:
                    errors.append("代码块中必须定义 execute 函数")
            
            # 检查权限设置
            if metadata.get("permissions", {}).get("write_vault") and \
               "#modifies-original" not in metadata.get("tags", []):
                errors.append("具有 write_vault 权限的 Skill 必须标注 #modifies-original 标签")
            
        except Exception as e:
            errors.append(f"解析错误: {str(e)}")
        
        return len(errors) == 0, errors
    
    def load(self, skill_id: str, force_reload: bool = False) -> Skill:
        """
        加载 Skill
        
        Args:
            skill_id: Skill ID 或文件路径
            force_reload: 是否强制重新加载
            
        Returns:
            Skill 对象
        """
        # 检查缓存
        if not force_reload and skill_id in self.skills_cache:
            return self.skills_cache[skill_id]
        
        # 查找文件
        file_path = self._find_skill_file(skill_id)
        if not file_path:
            raise FileNotFoundError(f"未找到 Skill: {skill_id}")
        
        # 验证
        is_valid, errors = self.validate(str(file_path))
        if not is_valid:
            raise ValueError(f"Skill 验证失败: {', '.join(errors)}")
        
        # 解析
        with open(file_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
        
        metadata_dict = post.metadata
        code = self._extract_code_block(post.content)
        
        if not code:
            raise ValueError(f"Skill {skill_id} 缺少代码块")
        
        # 构建元数据对象
        metadata = SkillMetadata(
            skill_id=metadata_dict["skill_id"],
            skill_name=metadata_dict["skill_name"],
            skill_version=metadata_dict["skill_version"],
            skill_type=metadata_dict["skill_type"],
            skill_category=metadata_dict["skill_category"],
            depends_on=metadata_dict.get("depends_on", []),
            inputs=metadata_dict.get("inputs", []),
            outputs=metadata_dict.get("outputs", []),
            execution=metadata_dict.get("execution", {}),
            author=metadata_dict.get("author", "unknown"),
            created_at=metadata_dict.get("created_at", ""),
            tags=metadata_dict.get("tags", []),
            permissions=metadata_dict.get("permissions", {}),
            file_path=str(file_path)
        )
        
        # 编译代码
        try:
            execute_func = self._compile_skill_code(code, metadata.skill_id)
        except Exception as e:
            raise RuntimeError(f"编译 Skill 代码失败: {str(e)}")
        
        # 创建 Skill 对象
        skill = Skill(
            metadata=metadata,
            code=code,
            execute_func=execute_func
        )
        
        # 缓存
        self.skills_cache[skill_id] = skill
        
        return skill
    
    def _find_skill_file(self, skill_id: str) -> Optional[Path]:
        """查找 Skill 文件"""
        # 如果是完整路径
        if os.path.isabs(skill_id) or skill_id.startswith('./'):
            path = Path(skill_id)
            if path.exists():
                return path
        
        # 在 Skills 目录中搜索
        for md_file in self.skills_dir.rglob("*.md"):
            if md_file.name == ".registry.md":
                continue
            
            try:
                metadata = self._parse_frontmatter(md_file)
                if metadata.get("skill_id") == skill_id:
                    return md_file
            except:
                continue
        
        return None
    
    async def execute(
        self, 
        skill_id: str, 
        inputs: Dict[str, Any],
        timeout: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        执行 Skill
        
        Args:
            skill_id: Skill ID
            inputs: 输入参数字典
            timeout: 超时时间（秒），默认使用 Skill 配置
            
        Returns:
            输出结果字典
        """
        skill = self.load(skill_id)
        
        # 检查依赖
        for dep_id in skill.metadata.depends_on:
            dep_id_clean = dep_id.strip("[]").replace("[[", "").replace("]]", "")
            if not self._find_skill_file(dep_id_clean):
                raise RuntimeError(f"缺少依赖 Skill: {dep_id_clean}")
        
        # 检查权限
        self._check_permissions(skill, inputs)
        
        # 准备执行环境
        exec_timeout = timeout or skill.metadata.execution.get("timeout", 30)
        
        # 执行
        try:
            if asyncio.iscoroutinefunction(skill.execute_func):
                result = await asyncio.wait_for(
                    skill.execute_func(inputs),
                    timeout=exec_timeout
                )
            else:
                result = skill.execute_func(inputs)
            
            return result
        except asyncio.TimeoutError:
            raise TimeoutError(f"Skill {skill_id} 执行超时（{exec_timeout}秒）")
        except Exception as e:
            raise RuntimeError(f"Skill {skill_id} 执行失败: {str(e)}")
    
    def _check_permissions(self, skill: Skill, inputs: Dict):
        """检查 Skill 权限"""
        perms = skill.metadata.permissions
        
        # 检查网络访问
        if not perms.get("network_access", False):
            # 如果 Skill 需要 3090 但未声明网络权限，自动允许（因为这是系统级需求）
            if skill.metadata.execution.get("requires_3090"):
                pass  # 允许
            else:
                # 检查代码中是否有网络调用
                if "httpx" in skill.code or "requests" in skill.code:
                    raise PermissionError(
                        f"Skill {skill.metadata.skill_id} 需要网络访问但未声明 network_access 权限"
                    )
        
        # 检查写入权限
        if not perms.get("write_vault", False):
            if "write" in skill.code.lower() or "save" in skill.code.lower():
                # 检查是否是安全的写入操作
                if "#modifies-original" not in skill.metadata.tags:
                    raise PermissionError(
                        f"Skill {skill.metadata.skill_id} 可能修改文件但未声明 write_vault 权限"
                    )
    
    def update_registry(self):
        """更新 Skill 注册表"""
        skills = []
        for file_path in self.discover():
            try:
                metadata = self._parse_frontmatter(Path(file_path))
                skills.append({
                    "id": metadata.get("skill_id", "unknown"),
                    "name": metadata.get("skill_name", "Unknown"),
                    "version": metadata.get("skill_version", "0.0.0"),
                    "type": metadata.get("skill_type", "custom"),
                    "category": metadata.get("skill_category", "Custom"),
                    "status": "stable" if "stable" in metadata.get("tags", []) else "testing",
                    "file_path": file_path,
                    "updated_at": datetime.now().strftime("%Y-%m-%d")
                })
            except:
                continue
        
        # 生成注册表 Markdown
        registry_content = "# Skill 注册表\n"
        registry_content += "> 自动生成，请勿手动编辑\n\n"
        registry_content += "| Skill ID | 名称 | 版本 | 类型 | 分类 | 状态 | 最后更新 |\n"
        registry_content += "|---------|------|------|------|------|------|---------|\n"
        
        for skill in sorted(skills, key=lambda x: x["id"]):
            registry_content += f"| {skill['id']} | {skill['name']} | {skill['version']} | "
            registry_content += f"{skill['type']} | {skill['category']} | {skill['status']} | "
            registry_content += f"{skill['updated_at']} |\n"
        
        # 写入文件
        with open(self.registry_file, 'w', encoding='utf-8') as f:
            f.write(registry_content)
        
        print(f"✅ 注册表已更新：发现 {len(skills)} 个 Skill")
    
    def list_skills(self) -> List[Dict]:
        """列出所有 Skill"""
        skills = []
        for file_path in self.discover():
            try:
                metadata = self._parse_frontmatter(Path(file_path))
                skills.append({
                    "id": metadata.get("skill_id"),
                    "name": metadata.get("skill_name"),
                    "version": metadata.get("skill_version"),
                    "type": metadata.get("skill_type"),
                    "category": metadata.get("skill_category"),
                    "file_path": file_path
                })
            except:
                continue
        return skills


# 便捷函数：调用 3090 算力
async def call_3090(prompt: str, system_prompt: str = "", temperature: float = 0.3) -> str:
    """
    调用 3090 算力接口（供 Skill 使用）
    
    Args:
        prompt: 用户提示
        system_prompt: 系统提示
        temperature: 温度参数
        
    Returns:
        LLM 响应文本
    """
    payload = {
        "model": CONFIG["3090_MODEL"],
        "messages": [],
        "temperature": temperature,
        "repetition_penalty": 1.005
    }
    
    if system_prompt:
        payload["messages"].append({"role": "system", "content": system_prompt})
    payload["messages"].append({"role": "user", "content": prompt})
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                CONFIG["3090_API_URL"],
                json=payload,
                timeout=30.0
            )
            if response.status_code == 200:
                return response.json()['choices'][0]['message']['content']
            else:
                raise RuntimeError(f"3090 API 错误: {response.status_code}")
        except Exception as e:
            raise RuntimeError(f"调用 3090 失败: {str(e)}")


if __name__ == "__main__":
    # 测试代码
    manager = SkillManager()
    
    # 更新注册表
    manager.update_registry()
    
    # 列出所有 Skill
    skills = manager.list_skills()
    print(f"\n发现 {len(skills)} 个 Skill:")
    for skill in skills:
        print(f"  - {skill['id']}: {skill['name']} ({skill['version']})")
