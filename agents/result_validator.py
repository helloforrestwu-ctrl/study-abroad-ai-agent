"""
Result Validator Agent - 结果验证器
验证匹配结果的合理性和准确性
"""


class ResultValidator:
    """结果验证Agent"""

    def __init__(self):
        self.validation_rules = {
            "min_schools_per_tier": 1,
            "max_schools_per_tier": 6,
            "total_min_schools": 3,
            "total_max_schools": 15
        }

    def validate(self, student_info, recommendations):
        """
        验证推荐结果
        :param student_info: 学生信息
        :param recommendations: 推荐结果
        :return: 验证后的推荐结果
        """
        print("✓ ResultValidator Agent 开始验证...")

        validated = recommendations.copy()

        # 规则1: 确保每个梯度至少有1所学校
        for tier in ["冲刺", "匹配", "保底"]:
            if len(validated[tier]) == 0:
                print(f"⚠️  警告: {tier}档学校数量为0，建议调整筛选条件")

        # 规则2: 检查总数量
        total_count = sum(len(validated[tier]) for tier in validated)

        if total_count < self.validation_rules["total_min_schools"]:
            print(f"⚠️  警告: 总推荐学校数({total_count})偏少")
        elif total_count > self.validation_rules["total_max_schools"]:
            print(f"⚠️  警告: 总推荐学校数({total_count})偏多，建议精简")

        # 规则3: 检查GPA和语言成绩的一致性
        gpa = student_info.get("gpa", 0)

        for tier in validated:
            for rec in validated[tier]:
                school = rec["school"]
                if gpa < school["gpa_requirement"] - 0.5:
                    print(f"⚠️  {school['中文名']} GPA要求({school['gpa_requirement']}) "
                          f"明显高于学生GPA({gpa})，建议移除")

        # 规则4: 检查截止日期合理性（确保有时间准备）
        # 这里可以添加截止日期检查逻辑

        print("✅ 验证完成")

        return validated

    def check_deadline_feasibility(self, recommendations, current_date=None):
        """检查申请截止日期的可行性"""
        # 简化版本：检查是否有足够时间准备
        warnings = []

        for tier in recommendations:
            for rec in recommendations[tier]:
                deadline = rec["school"]["deadline"]
                # 这里可以添加日期比较逻辑
                # 如果截止日期太近，添加警告

        return warnings
