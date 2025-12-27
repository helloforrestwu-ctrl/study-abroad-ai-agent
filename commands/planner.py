"""
Commands - 留学规划专家总指挥
资深留学规划专家，拥有20年经验，负责协调所有agents完成留学规划任务
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.settings import *
from agents.background_evaluator import BackgroundEvaluator
from agents.gpa_calculator import GPACalculator
from agents.school_matcher import SchoolMatcher
from agents.result_validator import ResultValidator
from agents.report_generator import ReportGenerator
from agents.timeline_agent import TimelineAgent
from agents.essay_advisor import EssayAdvisor
from agents.interview_coach import InterviewCoach
from agents.visa_advisor import VisaAdvisor


class StudyAbroadPlanner:
    """留学规划专家主控制器"""

    def __init__(self):
        self.conversation_state = {
            "step": 0,
            "student_info": {},
            "assessment_result": None,
            "school_recommendations": None
        }

        # 初始化所有agents
        self.background_evaluator = BackgroundEvaluator()
        self.gpa_calculator = GPACalculator()
        self.school_matcher = SchoolMatcher()
        self.result_validator = ResultValidator()
        self.report_generator = ReportGenerator()
        self.timeline_agent = TimelineAgent()
        self.essay_advisor = EssayAdvisor()
        self.interview_coach = InterviewCoach()
        self.visa_advisor = VisaAdvisor()

        print(f"\n{'='*60}")
        print(f"欢迎使用 {SYSTEM_CONFIG['name']}")
        print(f"我是您的留学规划顾问，拥有{SYSTEM_CONFIG['expert_years']}年行业经验")
        print(f"支持国家/地区: {', '.join(SYSTEM_CONFIG['supported_countries'])}")
        print(f"{'='*60}\n")

    def start_consultation(self):
        """开始咨询流程 - 分步骤引导"""
        self._ask_step_1()

    def _ask_step_1(self):
        """第一步：询问目标学位和国家倾向"""
        print("📋 **第一步：了解您的基本规划**\n")
        print("请告诉我：")
        print("1. 您计划申请什么学位？")
        print("   - 本科 (Undergraduate)")
        print("   - 硕士 (Master)")
        print("   - 博士 (PhD)")
        print()
        degree = input("请输入学位类型 (本科/硕士/博士): ").strip()

        while degree not in DEGREE_TYPES:
            print("❌ 请输入有效的学位类型")
            degree = input("请输入学位类型 (本科/硕士/博士): ").strip()

        self.conversation_state["student_info"]["degree"] = degree

        print("\n2. 您倾向于哪些国家/地区？")
        print(f"   可选: {', '.join(SYSTEM_CONFIG['supported_countries'])}")
        countries = input("请输入国家/地区 (可多选，用逗号分隔): ").strip()

        self.conversation_state["student_info"]["target_countries"] = [
            c.strip() for c in countries.split(",")
        ]

        print("\n✅ 收到！让我们继续...\n")
        self._ask_step_2()

    def _ask_step_2(self):
        """第二步：询问学术背景"""
        print("📊 **第二步：学术背景评估**\n")

        # 询问学校背景
        print("1. 您目前就读/毕业的学校名称：")
        school = input("学校: ").strip()
        self.conversation_state["student_info"]["school"] = school

        # 询问专业
        print("\n2. 您的专业是什么？")
        major = input("专业: ").strip()
        self.conversation_state["student_info"]["major"] = major

        # 询问GPA
        print("\n3. 您的GPA是多少？(如果不清楚，可以稍后计算)")
        gpa_input = input("GPA (或输入'计算'让我帮您): ").strip()

        if gpa_input == "计算":
            gpa = self._calculate_gpa_interactive()
        else:
            try:
                gpa = float(gpa_input)
            except ValueError:
                print("⚠️ GPA格式有误，将在后续帮您计算")
                gpa = None

        self.conversation_state["student_info"]["gpa"] = gpa

        print("\n✅ 学术背景已记录！\n")
        self._ask_step_3()

    def _calculate_gpa_interactive(self):
        """交互式GPA计算"""
        print("\n📐 **GPA计算器**")
        print("请选择您的成绩格式：")
        print("1. 4.0制 (A+, A, B+...)")
        print("2. 百分制 (90, 85, 78...)")

        choice = input("选择 (1/2): ").strip()
        grades = input("请输入所有课程成绩，用逗号分隔: ").strip()
        credits = input("请输入对应学分，用逗号分隔 (若都相同可输入总数): ").strip()

        grade_list = [g.strip() for g in grades.split(",")]

        if "," in credits:
            credit_list = [float(c.strip()) for c in credits.split(",")]
        else:
            credit_list = [float(credits) / len(grade_list)] * len(grade_list)

        gpa_result = self.gpa_calculator.calculate(grade_list, credit_list, choice)
        print(f"\n✅ 计算结果: GPA = {gpa_result:.2f}")

        return gpa_result

    def _ask_step_3(self):
        """第三步：询问语言成绩和软背景"""
        print("🌍 **第三步：标准化考试与经历**\n")

        # 语言成绩
        print("1. 您的语言成绩 (TOEFL/IELTS):")
        language_test = input("考试类型 (TOEFL/IELTS): ").strip()
        score = input("分数: ").strip()

        self.conversation_state["student_info"]["language"] = {
            "test": language_test,
            "score": score
        }

        # 科研/实习
        print("\n2. 请简要描述您的科研、实习或竞赛经历 (可多条，用分号分隔):")
        experiences = input("经历: ").strip()

        self.conversation_state["student_info"]["experiences"] = [
            e.strip() for e in experiences.split(";") if e.strip()
        ]

        print("\n✅ 信息收集完成！开始为您分析...\n")
        self._process_assessment()

    def _process_assessment(self):
        """处理评估流程"""
        print("⚙️ **正在评估您的背景...**\n")

        # Step 1: 背景评估
        assessment = self.background_evaluator.evaluate(
            self.conversation_state["student_info"]
        )

        # Step 2: 学校匹配
        recommendations = self.school_matcher.match_schools(
            self.conversation_state["student_info"],
            assessment
        )

        # Step 3: 结果验证
        validated = self.result_validator.validate(
            self.conversation_state["student_info"],
            recommendations
        )

        # Step 4: 生成报告
        report = self.report_generator.generate(
            self.conversation_state["student_info"],
            assessment,
            validated
        )

        print(report)

        # 保存结果
        self.conversation_state["assessment_result"] = assessment
        self.conversation_state["school_recommendations"] = validated

        # 询问是否需要额外服务
        self._offer_additional_services()

    def _offer_additional_services(self):
        """提供额外服务"""
        print("\n" + "="*60)
        print("📌 **额外服务**\n")
        print("我还可以为您提供以下服务：")
        print("1. 📅 详细申请时间线规划")
        print("2. ✍️  文书素材挖掘与立意建议")
        print("3. 🎤 面试准备与模拟")
        print("4. 🛂 签证材料清单与攻略")
        print("5. ❌ 暂不需要，结束咨询")
        print()

        choice = input("请选择服务编号 (1-5): ").strip()

        if choice == "1":
            self._provide_timeline()
        elif choice == "2":
            self._provide_essay_guidance()
        elif choice == "3":
            self._provide_interview_prep()
        elif choice == "4":
            self._provide_visa_info()
        elif choice == "5":
            print("\n✅ 感谢使用！祝您申请顺利！")
            return
        else:
            print("❌ 无效选择")
            self._offer_additional_services()

    def _provide_timeline(self):
        """提供时间线规划"""
        timeline = self.timeline_agent.create_timeline(
            self.conversation_state["student_info"]
        )
        print(timeline)

        input("\n按回车继续...")
        self._offer_additional_services()

    def _provide_essay_guidance(self):
        """提供文书指导"""
        guidance = self.essay_advisor.provide_guidance(
            self.conversation_state["student_info"]
        )
        print(guidance)

        input("\n按回车继续...")
        self._offer_additional_services()

    def _provide_interview_prep(self):
        """提供面试准备"""
        prep = self.interview_coach.prepare_interview(
            self.conversation_state["student_info"],
            self.conversation_state["school_recommendations"]
        )
        print(prep)

        input("\n按回车继续...")
        self._offer_additional_services()

    def _provide_visa_info(self):
        """提供签证信息"""
        visa_info = self.visa_advisor.provide_visa_guide(
            self.conversation_state["student_info"]["target_countries"]
        )
        print(visa_info)

        input("\n按回车继续...")
        self._offer_additional_services()


if __name__ == "__main__":
    planner = StudyAbroadPlanner()
    planner.start_consultation()
