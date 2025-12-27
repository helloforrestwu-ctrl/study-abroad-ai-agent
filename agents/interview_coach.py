"""
Interview Coach Agent - 面试准备与辅导
提供面试常见问题、答题框架和模拟训练
"""


class InterviewCoach:
    """面试辅导Agent"""

    def __init__(self):
        self.common_questions = {
            "通用问题": [
                "Tell me about yourself / 自我介绍",
                "Why this program? / 为什么选择这个项目?",
                "Why our university? / 为什么选择我们学校?",
                "What are your career goals? / 你的职业目标是什么?",
                "What's your greatest strength/weakness? / 最大优势/劣势?"
            ],
            "学术问题": [
                "Describe your research experience / 描述你的科研经历",
                "What's your favorite course and why? / 最喜欢的课程及原因",
                "How do you handle academic challenges? / 如何应对学术挑战?",
                "What area do you want to specialize in? / 想专攻哪个方向?"
            ],
            "行为问题": [
                "Tell me about a time you led a team / 描述一次领导团队的经历",
                "Describe a conflict and how you resolved it / 如何解决冲突",
                "Give an example of when you failed / 讲述一次失败经历",
                "How do you work under pressure? / 如何在压力下工作?"
            ]
        }

        self.school_cultures = {
            "MIT": "创新、动手能力、跨学科合作",
            "Stanford": "创业精神、社会影响力、领导力",
            "CMU": "技术深度、项目经验、团队协作",
            "Columbia": "国际视野、社会责任、多元文化",
            "Cambridge": "学术严谨、批判性思维、独立研究"
        }

    def prepare_interview(self, student_info, recommendations):
        """
        准备面试材料
        :param student_info: 学生信息
        :param recommendations: 推荐学校
        :return: 面试准备指南
        """
        print("🎤 InterviewCoach Agent 开始准备...")

        output = []
        output.append("\n" + "="*80)
        output.append("🎤 面试准备指南 | Interview Preparation Guide")
        output.append("="*80 + "\n")

        # 第一部分：高频面试问题及答题要点
        output.append("【高频面试问题及答题要点】\n")

        for category, questions in self.common_questions.items():
            output.append(f"**{category}:**\n")

            for i, question in enumerate(questions[:5], 1):
                output.append(f"  {i}. {question}")

                # 提供答题要点
                if "yourself" in question.lower():
                    output.append("     💡 答题框架: 学术背景(30s) → 核心经历(60s) → 为什么申请(30s)")
                elif "why this program" in question.lower():
                    output.append("     💡 答题要点: 项目特色+个人目标契合 (具体到课程、教授)")
                elif "weakness" in question.lower():
                    output.append("     💡 答题要点: 真实的小缺点 + 如何改进 (避免假弱点如\"太完美主义\")")
                elif "research" in question.lower():
                    output.append("     💡 答题框架: 研究背景 → 方法与挑战 → 成果与收获")
                elif "team" in question.lower() or "led" in question.lower():
                    output.append("     💡 STAR法则: Situation → Task → Action → Result")

                output.append("")

        # 第二部分：模拟案例 - 行为面试题
        output.append("="*80)
        output.append("【模拟案例：行为面试题答题示范】")
        output.append("="*80 + "\n")

        output.append("**问题: \"Tell me about a time when you had to work with a difficult team member.\"**\n")

        output.append("**STAR答题框架:**\n")
        output.append("**S (Situation 情境):**")
        output.append("  \"在XX项目中，我和一位组员在技术方案上产生分歧...\"")
        output.append("  ⏱️ 时长: 15-20秒\n")

        output.append("**T (Task 任务):**")
        output.append("  \"作为项目负责人，我需要在保证进度的同时达成共识...\"")
        output.append("  ⏱️ 时长: 10秒\n")

        output.append("**A (Action 行动):**")
        output.append("  \"我采取了以下措施:")
        output.append("   1. 安排一对一沟通，倾听对方顾虑")
        output.append("   2. 用数据对比两个方案的优劣")
        output.append("   3. 提出折中方案，结合双方观点...\"")
        output.append("  ⏱️ 时长: 40-50秒\n")

        output.append("**R (Result 结果):**")
        output.append("  \"最终我们采用了折中方案，项目按时完成，团队关系也得到改善...\"")
        output.append("  ⏱️ 时长: 20秒\n")

        output.append("⚠️ **注意事项:**")
        output.append("  - 控制总时长在90-120秒")
        output.append("  - 用具体数据和细节增强说服力")
        output.append("  - 展示你的软技能(沟通、领导力、解决问题)")
        output.append("  - 结果部分可提及你的反思与成长\n")

        # 第三部分：目标学校的文化偏好
        output.append("="*80)
        output.append("【目标学校的文化偏好】")
        output.append("="*80 + "\n")

        # 从推荐学校中提取
        target_schools = set()
        for tier in recommendations:
            for rec in recommendations[tier]:
                school_name = rec['school']['name']
                for key in self.school_cultures:
                    if key in school_name:
                        target_schools.add(key)

        if target_schools:
            for school in target_schools:
                culture = self.school_cultures.get(school, "学术严谨、创新思维")
                output.append(f"**{school}:**")
                output.append(f"  文化关键词: {culture}")
                output.append(f"  面试策略: 准备能体现这些特质的案例\n")
        else:
            output.append("**通用建议:**")
            output.append("  - 研究每所学校的mission statement和核心价值观")
            output.append("  - 在面试中有意识地体现这些特质")
            output.append("  - 准备至少3个不同类型的案例以应对各种问题\n")

        # 第四部分：面试准备清单
        output.append("="*80)
        output.append("【面试准备清单】")
        output.append("="*80 + "\n")

        output.append("**准备阶段 (收到面试邀请后2周):**")
        output.append("  ☐ 研究项目网页，记录3-5个感兴趣的课程/教授")
        output.append("  ☐ 准备1分钟自我介绍(录音练习)")
        output.append("  ☐ 用STAR法整理5个核心案例")
        output.append("  ☐ 准备3-5个向面试官提问的问题")
        output.append("  ☐ 参加至少2次模拟面试\n")

        output.append("**面试当天:**")
        output.append("  ☐ 提前15分钟登录/到达")
        output.append("  ☐ 测试设备(如线上面试)")
        output.append("  ☐ 准备纸笔记录要点")
        output.append("  ☐ 保持微笑和眼神交流")
        output.append("  ☐ 面试结束后24小时内发送Thank-you Email\n")

        output.append("**向面试官提问的问题示例:**")
        output.append("  1. \"What do you think makes students successful in this program?\"")
        output.append("  2. \"Are there opportunities for interdisciplinary collaboration?\"")
        output.append("  3. \"What's the typical career path for graduates?\"")

        output.append("\n" + "="*80 + "\n")

        print("✅ 面试准备材料生成完成")

        return "\n".join(output)
