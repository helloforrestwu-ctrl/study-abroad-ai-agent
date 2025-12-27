"""
Essay Advisor Agent - 文书素材挖掘与立意建议
帮助学生挖掘文书素材，提供写作角度建议
"""


class EssayAdvisor:
    """文书辅导Agent"""

    def __init__(self):
        self.cliche_phrases = [
            "从小就对XX充满热情",
            "通过这次经历，我成长了很多",
            "我想改变世界",
            "我是一个领导者",
            "我热爱挑战",
            "失败是成功之母",
            "梦想成真"
        ]

    def provide_guidance(self, student_info):
        """
        提供文书指导
        :param student_info: 学生信息
        :return: 文书建议文本
        """
        print("✍️  EssayAdvisor Agent 开始分析...")

        experiences = student_info.get("experiences", [])
        major = student_info.get("major", "")

        output = []
        output.append("\n" + "="*80)
        output.append("✍️  文书素材挖掘与立意建议 | Essay Guidance")
        output.append("="*80 + "\n")

        # 第一部分：可能的文书角度
        output.append("【三个可能的文书立意角度】\n")

        # 角度1: 基于专业兴趣
        output.append("**角度1: 学术兴趣的演进与深化**")
        output.append(f"  核心叙事逻辑:")
        output.append(f"    → 起点: 如何对{major}领域产生初步兴趣")
        output.append(f"    → 发展: 通过课程/项目如何加深理解")
        output.append(f"    → 转折: 遇到的困惑或挑战")
        output.append(f"    → 升华: 通过研究/实践找到热情所在")
        output.append(f"  适用项目: 重视学术能力和研究潜力的项目\n")

        # 角度2: 基于实践经历
        if experiences:
            output.append("**角度2: 从实践中发现问题与使命**")
            output.append(f"  核心叙事逻辑:")
            output.append(f"    → 背景: 参与某个项目/实习的动机")
            output.append(f"    → 冲突: 发现现实与理想的差距")
            output.append(f"    → 行动: 如何尝试解决问题")
            output.append(f"    → 反思: 对职业方向/社会责任的新认识")
            output.append(f"  适用项目: 注重社会影响力和实践能力的项目\n")

        # 角度3: 跨文化/跨学科视角
        output.append("**角度3: 跨界思维与独特视角**")
        output.append(f"  核心叙事逻辑:")
        output.append(f"    → 独特性: 展示不同于传统路径的经历")
        output.append(f"    → 连接点: 如何将不同领域的知识/经验结合")
        output.append(f"    → 价值: 这种跨界视角如何帮助解决问题")
        output.append(f"    → 未来: 如何在研究生阶段继续这种探索")
        output.append(f"  适用项目: 鼓励创新和多元背景的项目\n")

        # 第二部分：避免的陈词滥调
        output.append("="*80)
        output.append("【⚠️  避免使用的陈词滥调】\n")

        for i, phrase in enumerate(self.cliche_phrases, 1):
            output.append(f"  {i}. \"{phrase}\"")

        output.append("\n**替代建议:**")
        output.append("  - 用具体的场景和细节代替空洞的宣言")
        output.append("  - 用数据和事实支撑你的观点")
        output.append("  - 展示思考过程而非结论")
        output.append("  - 承认不确定性和局限性，显得更真实")

        # 第三部分：文书写作通用建议
        output.append("\n" + "="*80)
        output.append("【文书写作建议】")
        output.append("="*80 + "\n")

        output.append("**1. Show, Don't Tell (展示，而非告知)**")
        output.append("  ❌ 我是一个有领导力的人")
        output.append("  ✅ 我组织了XX活动，协调10个部门，最终吸引500+参与者\n")

        output.append("**2. 具体化你的经历**")
        output.append("  ❌ 我参加了一个科研项目")
        output.append("  ✅ 在XX教授的实验室，我用Python分析了10000+条数据，发现...\n")

        output.append("**3. 体现成长与反思**")
        output.append("  - 不要只讲成功故事，也可以讲失败后的思考")
        output.append("  - 展示你的思维方式如何因某个经历而改变")
        output.append("  - 连接过去经历与未来目标\n")

        output.append("**4. 针对性写作**")
        output.append("  - 研究每个项目的特点(课程设置、教授研究方向、校园文化)")
        output.append("  - 在文书中体现\"Why this program\"")
        output.append("  - 避免模板化的通用文书")

        output.append("\n" + "="*80 + "\n")

        print("✅ 文书建议生成完成")

        return "\n".join(output)

    def analyze_draft(self, draft_text):
        """分析文书初稿，给出修改建议"""
        # 可以添加更多分析逻辑
        suggestions = []

        # 检查陈词滥调
        for cliche in self.cliche_phrases:
            if cliche in draft_text:
                suggestions.append(f"发现陈词滥调: \"{cliche}\", 建议用具体案例替代")

        # 检查字数
        word_count = len(draft_text.split())
        if word_count < 200:
            suggestions.append(f"字数偏少({word_count}词)，建议增加细节描述")
        elif word_count > 650:
            suggestions.append(f"字数超标({word_count}词)，建议精简")

        return suggestions
