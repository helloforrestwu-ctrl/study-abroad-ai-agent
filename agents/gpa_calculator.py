"""
GPA Calculator Agent - GPA计算器
支持4.0制和百分制的GPA转换计算
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.settings import GPA_CONFIG


class GPACalculator:
    """GPA计算Agent"""

    def __init__(self):
        self.scale_4_0_map = GPA_CONFIG["scale_4_0"]
        self.percentage_map = GPA_CONFIG["百分制转换"]

    def calculate(self, grades, credits, grade_type="1"):
        """
        计算加权GPA
        :param grades: 成绩列表
        :param credits: 学分列表
        :param grade_type: "1" = 4.0制, "2" = 百分制
        :return: GPA值
        """
        print("🧮 GPACalculator Agent 开始计算...")

        if grade_type == "1":
            gpa_points = self._convert_4_0_scale(grades)
        else:
            gpa_points = self._convert_percentage_scale(grades)

        # 加权计算
        total_credits = sum(credits)
        weighted_sum = sum(gp * cr for gp, cr in zip(gpa_points, credits))

        if total_credits == 0:
            return 0.0

        final_gpa = weighted_sum / total_credits

        print(f"✅ GPA计算完成: {final_gpa:.2f}")

        return round(final_gpa, 2)

    def _convert_4_0_scale(self, grades):
        """将字母成绩转换为4.0制绩点"""
        gpa_points = []

        for grade in grades:
            grade = grade.strip().upper()
            gpa_points.append(self.scale_4_0_map.get(grade, 0.0))

        return gpa_points

    def _convert_percentage_scale(self, grades):
        """将百分制成绩转换为4.0制绩点"""
        gpa_points = []

        for grade in grades:
            try:
                score = float(grade)
                gp = self._percentage_to_gpa(score)
                gpa_points.append(gp)
            except ValueError:
                gpa_points.append(0.0)

        return gpa_points

    def _percentage_to_gpa(self, percentage):
        """百分制转4.0制的映射算法"""
        if percentage >= 90:
            return 4.0
        elif percentage >= 85:
            return 3.7
        elif percentage >= 82:
            return 3.3
        elif percentage >= 78:
            return 3.0
        elif percentage >= 75:
            return 2.7
        elif percentage >= 72:
            return 2.3
        elif percentage >= 68:
            return 2.0
        elif percentage >= 64:
            return 1.7
        elif percentage >= 60:
            return 1.0
        else:
            return 0.0

    def estimate_target_gpa(self, current_gpa, current_credits, target_gpa, remaining_courses):
        """
        计算达到目标GPA需要的平均成绩
        :param current_gpa: 当前GPA
        :param current_credits: 当前总学分
        :param target_gpa: 目标GPA
        :param remaining_courses: 剩余课程数量
        :return: 需要达到的平均GPA
        """
        total_credits = current_credits + remaining_courses
        required_total = target_gpa * total_credits
        current_total = current_gpa * current_credits
        needed_points = required_total - current_total

        if remaining_courses == 0:
            return None

        required_avg = needed_points / remaining_courses

        return round(required_avg, 2)
