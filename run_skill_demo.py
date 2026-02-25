"""
运行 skill_my_first 示例
> 在项目根目录执行: python run_skill_demo.py
"""
import asyncio
import os
from skill_manager import SkillManager


async def main():
    # 使用当前项目目录为 vault_path，这样会从 ./Skills/ 加载
    project_root = os.path.dirname(os.path.abspath(__file__))
    manager = SkillManager(vault_path=project_root)

    result = await manager.execute("skill_my_first", {
        "text": "Hello World"
    })
    print(result)  # {"result": "处理结果: HELLO WORLD"}


if __name__ == "__main__":
    asyncio.run(main())
