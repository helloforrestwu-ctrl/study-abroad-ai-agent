#!/usr/bin/env python3
"""
留学规划AI智能体系统 - 演示脚本
展示系统完整工作流程
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agents.background_evaluator import BackgroundEvaluator
from agents.gpa_calculator import GPACalculator
from agents.school_matcher import SchoolMatcher
from agents.result_validator import ResultValidator
from agents.report_generator import ReportGenerator
from agents.timeline_agent import TimelineAgent
from agents.essay_advisor import EssayAdvisor
from agents.interview_coach import InterviewCoach
from agents.visa_advisor import VisaAdvisor


def demo_case_1():
    """演示案例1: 强竞争力学生（清华大学，CS专业）"""
    print("\n" + "="*70)
    print("🎬 演示案例1：强竞争力学生")
    print("="*70 + "\n")

    # 模拟学生信息
    student_info = {
        "degree": "硕士",
        "target_countries": ["美国", "英国"],
        "school": "清华大学",
        "major": "计算机科学",
        "gpa": 3.75,
        "language": {
            "test": "TOEFL",
            "score": "110"
        },
        "experiences": [
            "机器学习实验室科研项目2年，发表1篇论文",
            "字节跳动AI Lab实习6个月",
            "ACM-ICPC区域赛金奖"
        ]
    }

    print("📝 学生信息：")
    print(f"  院校：{student_info['school']}")
    print(f"  专业：{student_info['major']}")
    print(f"  GPA：{student_info['gpa']}")
    print(f"  语言：{student_info['language']['test']} {student_info['language']['score']}")
    print(f"  经历：{len(student_info['experiences'])}项\n")

    # 初始化Agents
    background_evaluator = BackgroundEvaluator()
    school_matcher = SchoolMatcher()
    result_validator = ResultValidator()
    report_generator = ReportGenerator()

    # 执行评估流程
    print("\n⚙️  开始评估流程...\n")

    # 1. 背景评估
    assessment = background_evaluator.evaluate(student_info)

    # 2. 学校匹配
    recommendations = school_matcher.match_schools(student_info, assessment)

    # 3. 结果验证
    validated = result_validator.validate(student_info, recommendations)

    # 4. 生成报告
    report = report_generator.generate(student_info, assessment, validated)

    print(report)

    # 5. 展示增值服务
    print("\n" + "="*70)
    print("📌 增值服务演示")
    print("="*70)

    # 时间线规划
    timeline_agent = TimelineAgent()
    timeline = timeline_agent.create_timeline(student_info)
    print(timeline)

    return student_info, validated


def demo_case_2():
    """演示案例2: 中等竞争力学生（普通985，需要提升）"""
    print("\n" + "="*70)
    print("🎬 演示案例2：中等竞争力学生")
    print("="*70 + "\n")

    student_info = {
        "degree": "硕士",
        "target_countries": ["美国"],
        "school": "某985大学",
        "major": "电子工程",
        "gpa": 3.35,
        "language": {
            "test": "TOEFL",
            "score": "95"
        },
        "experiences": [
            "参与导师项目1个",
            "校内实验室助研"
        ]
    }

    print("📝 学生信息：")
    print(f"  院校：{student_info['school']}")
    print(f"  专业：{student_info['major']}")
    print(f"  GPA：{student_info['gpa']}")
    print(f"  语言：{student_info['language']['test']} {student_info['language']['score']}")
    print(f"  经历：{len(student_info['experiences'])}项\n")

    # 初始化Agents
    background_evaluator = BackgroundEvaluator()
    school_matcher = SchoolMatcher()
    result_validator = ResultValidator()
    report_generator = ReportGenerator()

    print("\n⚙️  开始评估流程...\n")

    # 执行评估
    assessment = background_evaluator.evaluate(student_info)
    recommendations = school_matcher.match_schools(student_info, assessment)
    validated = result_validator.validate(student_info, recommendations)
    report = report_generator.generate(student_info, assessment, validated)

    print(report)

    # 展示提升建议
    suggestions = background_evaluator.get_improvement_suggestions(assessment)
    if suggestions:
        print("\n💡 **提升建议：**")
        for i, suggestion in enumerate(suggestions, 1):
            print(f"  {i}. {suggestion}")

    return student_info, validated


def demo_gpa_calculator():
    """演示GPA计算功能"""
    print("\n" + "="*70)
    print("🎬 演示：GPA计算器")
    print("="*70 + "\n")

    calculator = GPACalculator()

    # 案例1: 4.0制
    print("**案例1: 4.0制字母成绩**")
    grades = ["A", "A-", "B+", "A", "B"]
    credits = [3, 3, 4, 3, 2]

    print(f"成绩: {', '.join(grades)}")
    print(f"学分: {', '.join(map(str, credits))}")

    gpa = calculator.calculate(grades, credits, grade_type="1")
    print(f"结果: GPA = {gpa}\n")

    # 案例2: 百分制
    print("**案例2: 百分制成绩**")
    grades = ["92", "88", "85", "90", "78"]
    credits = [3, 3, 4, 3, 2]

    print(f"成绩: {', '.join(grades)}")
    print(f"学分: {', '.join(map(str, credits))}")

    gpa = calculator.calculate(grades, credits, grade_type="2")
    print(f"结果: GPA = {gpa}\n")


def demo_essay_guidance():
    """演示文书辅导"""
    print("\n" + "="*70)
    print("🎬 演示：文书素材挖掘")
    print("="*70 + "\n")

    student_info = {
        "degree": "硕士",
        "major": "计算机科学",
        "experiences": [
            "AI实验室科研",
            "科技公司实习",
            "编程竞赛"
        ]
    }

    essay_advisor = EssayAdvisor()
    guidance = essay_advisor.provide_guidance(student_info)
    print(guidance)


def demo_interview_prep():
    """演示面试准备"""
    print("\n" + "="*70)
    print("🎬 演示：面试准备")
    print("="*70 + "\n")

    student_info = {
        "degree": "硕士",
        "target_countries": ["美国"]
    }

    recommendations = {
        "冲刺": [
            {"school": {"name": "Carnegie Mellon University", "中文名": "卡内基梅隆大学"}}
        ],
        "匹配": [],
        "保底": []
    }

    interview_coach = InterviewCoach()
    prep = interview_coach.prepare_interview(student_info, recommendations)
    print(prep)


def demo_visa_guide():
    """演示签证攻略"""
    print("\n" + "="*70)
    print("🎬 演示：签证材料清单")
    print("="*70 + "\n")

    target_countries = ["美国", "英国"]

    visa_advisor = VisaAdvisor()
    guide = visa_advisor.provide_visa_guide(target_countries)
    print(guide)


def main():
    """主演示函数"""
    print("\n" + "🌟"*35)
    print("欢迎使用 留学规划AI智能体系统 - 演示模式")
    print("🌟"*35)

    print("\n本演示将展示系统的完整功能：")
    print("1. 强竞争力学生评估")
    print("2. 中等竞争力学生评估")
    print("3. GPA计算器")
    print("4. 文书素材挖掘")
    print("5. 面试准备")
    print("6. 签证攻略")

    print("\n按回车开始演示...\n")
    # input()  # 如果需要交互可以取消注释

    # 演示1: 强竞争力学生
    demo_case_1()
    print("\n" + "-"*70)
    print("按回车继续下一个演示...")
    # input()

    # 演示2: 中等竞争力学生
    demo_case_2()
    print("\n" + "-"*70)

    # 演示3: GPA计算
    demo_gpa_calculator()
    print("\n" + "-"*70)

    # 演示4: 文书辅导
    demo_essay_guidance()
    print("\n" + "-"*70)

    # 演示5: 面试准备
    demo_interview_prep()
    print("\n" + "-"*70)

    # 演示6: 签证攻略
    demo_visa_guide()

    print("\n" + "="*70)
    print("🎉 演示完成！")
    print("="*70)
    print("\n如需使用完整交互版本，请运行：python3 main.py")
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n演示已退出。")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ 发生错误: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
