"""
Report Generator Agent - 评估报告生成器
生成专业的留学规划评估报告
"""


class ReportGenerator:
    """报告生成Agent"""

    def __init__(self):
        pass

    def generate(self, student_info, assessment, recommendations):
        """
        生成评估报告
        :param student_info: 学生信息
        :param assessment: 评估结果
        :param recommendations: 学校推荐结果
        :return: 格式化的报告文本
        """
        print("📄 ReportGenerator Agent 开始生成报告...")

        report = []
        report.append("\n" + "="*70)
        report.append("📊 留学申请评估报告 | Study Abroad Assessment Report")
        report.append("="*70 + "\n")

        # 第一部分：学生背景概况
        report.append("【学生背景概况】")
        report.append(f"  学位目标: {student_info.get('degree', 'N/A')}")
        report.append(f"  目标国家/地区: {', '.join(student_info.get('target_countries', []))}")
        report.append(f"  本科院校: {student_info.get('school', 'N/A')}")
        report.append(f"  专业: {student_info.get('major', 'N/A')}")
        report.append(f"  GPA: {student_info.get('gpa', 0):.2f} / 4.0")

        language = student_info.get('language', {})
        report.append(f"  语言成绩: {language.get('test', 'N/A')} {language.get('score', 'N/A')}")
        report.append("")

        # 第二部分：竞争力评估
        report.append("【竞争力评估】")
        report.append(f"  综合评分: {assessment['overall_score']:.1f}/100")
        report.append(f"  竞争力等级: {assessment['competitiveness']}")
        report.append("")

        report.append("  分项评分:")
        for key, score in assessment['detailed_scores'].items():
            report.append(f"    • {key}: {score:.1f}/100")
        report.append("")

        if assessment['strengths']:
            report.append("  优势:")
            for strength in assessment['strengths']:
                report.append(f"    ✓ {strength}")
            report.append("")

        if assessment['weaknesses']:
            report.append("  待提升:")
            for weakness in assessment['weaknesses']:
                report.append(f"    → {weakness}")
            report.append("")

        # 第三部分：学校推荐清单
        report.append("="*70)
        report.append("【选校清单 | School List】")
        report.append("="*70 + "\n")

        for tier in ["冲刺", "匹配", "保底"]:
            tier_emoji = {"冲刺": "🎯", "匹配": "🎓", "保底": "🛡️"}
            report.append(f"{tier_emoji[tier]} **{tier}档 (Reach/Match/Safety)**\n")

            if not recommendations[tier]:
                report.append("  暂无推荐\n")
                continue

            for i, rec in enumerate(recommendations[tier], 1):
                school = rec['school']
                country = rec['country']

                report.append(f"  {i}. **{school['中文名']}** ({school['name']})")
                report.append(f"     国家: {country} | 排名: #{school['ranking']}")
                report.append(f"     推荐项目: {', '.join(school['programs'])}")
                report.append(f"     语言要求: TOEFL {school['toefl_requirement']}+ / IELTS {school['ielts_requirement']}+")
                report.append(f"     **申请截止: {school['deadline']}**")
                report.append(f"     匹配理由: {school['match_reason']}")
                report.append("")

        # 第四部分：申请建议
        report.append("="*70)
        report.append("【申请建议】")
        report.append("="*70 + "\n")

        report.append("  1. 建议申请总数: 8-12所 (冲刺3-4所, 匹配4-5所, 保底2-3所)")
        report.append("  2. 重点关注**加粗**的申请截止日期，提前3-6个月开始准备")
        report.append("  3. 根据各校特点准备针对性文书材料")

        if assessment['overall_score'] < 75:
            report.append("  4. 建议继续提升GPA或语言成绩以增强竞争力")

        report.append("\n" + "="*70 + "\n")

        print("✅ 报告生成完成")

        return "\n".join(report)

    def export_to_file(self, report_text, filename="留学规划报告.txt"):
        """将报告导出为文件"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(report_text)

        print(f"✅ 报告已导出到: {filename}")
