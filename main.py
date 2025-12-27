#!/usr/bin/env python3
"""
留学规划AI智能体系统 - 主入口
Study Abroad Planning AI Agent System
"""

import sys
import os

# 添加项目路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from commands.planner import StudyAbroadPlanner


def main():
    """主函数"""
    try:
        # 创建留学规划专家实例
        planner = StudyAbroadPlanner()

        # 开始咨询流程
        planner.start_consultation()

    except KeyboardInterrupt:
        print("\n\n程序已退出。感谢使用！")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ 发生错误: {str(e)}")
        print("请联系技术支持或重新启动程序。")
        sys.exit(1)


if __name__ == "__main__":
    main()
