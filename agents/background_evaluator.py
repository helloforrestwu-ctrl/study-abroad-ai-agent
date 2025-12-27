"""
Background Evaluator Agent - 学生背景评估
评估学生的学术背景、语言成绩、实习科研经历等
"""

import json
import os


class BackgroundEvaluator:
    """学生背景评估Agent"""

    def __init__(self):
        self.evaluation_criteria = {
            "GPA": {"weight": 0.35, "thresholds": {"high": 3.5, "medium": 3.0, "low": 2.7}},
            "语言成绩": {"weight": 0.25, "thresholds": {
                "TOEFL": {"high": 100, "medium": 90, "low": 80},
                "IELTS": {"high": 7.0, "medium": 6.5, "low": 6.0}
            }},
            "科研经历": {"weight": 0.20},
            "实习经历": {"weight": 0.20}
        }

    def evaluate(self, student_info):
        """
        评估学生背景
        :param student_info: 学生信息字典
        :return: 评估结果
        """
        print("🔍 BackgroundEvaluator Agent 开始工作...")

        assessment = {
            "overall_score": 0,
            "strengths": [],
            "weaknesses": [],
            "competitiveness": "",
            "detailed_scores": {}
        }

        # 评估GPA
        gpa_score = self._evaluate_gpa(student_info.get("gpa"))
        assessment["detailed_scores"]["GPA"] = gpa_score

        # 评估语言成绩
        language_score = self._evaluate_language(student_info.get("language", {}))
        assessment["detailed_scores"]["语言成绩"] = language_score

        # 评估经历背景
        experience_score = self._evaluate_experiences(student_info.get("experiences", []))
        assessment["detailed_scores"]["软背景"] = experience_score

        # 计算总分
        assessment["overall_score"] = (
            gpa_score * self.evaluation_criteria["GPA"]["weight"] +
            language_score * self.evaluation_criteria["语言成绩"]["weight"] +
            experience_score * 0.40
        )

        # 判定竞争力
        if assessment["overall_score"] >= 85:
            assessment["competitiveness"] = "强竞争力"
            assessment["strengths"].append("整体背景优秀，适合冲刺Top 30院校")
        elif assessment["overall_score"] >= 70:
            assessment["competitiveness"] = "中等竞争力"
            assessment["strengths"].append("背景扎实，适合申请Top 30-60院校")
        else:
            assessment["competitiveness"] = "有待提升"
            assessment["weaknesses"].append("建议加强语言成绩或增加软背景")

        # 具体优劣势分析
        if gpa_score >= 85:
            assessment["strengths"].append(f"GPA {student_info.get('gpa', 0):.2f} 达标主流院校要求")
        else:
            assessment["weaknesses"].append("GPA相对偏低，可能影响Top院校申请")

        if language_score >= 85:
            assessment["strengths"].append("语言成绩达到竞争性水平")
        else:
            assessment["weaknesses"].append("语言成绩有提升空间")

        if experience_score >= 75:
            assessment["strengths"].append("科研/实习经历丰富")
        else:
            assessment["weaknesses"].append("建议增加相关领域实践经验")

        print(f"✅ 评估完成 - 竞争力等级: {assessment['competitiveness']}")

        return assessment

    def _evaluate_gpa(self, gpa):
        """评估GPA，返回0-100分数"""
        if gpa is None:
            return 60

        thresholds = self.evaluation_criteria["GPA"]["thresholds"]
        if gpa >= thresholds["high"]:
            return 95
        elif gpa >= thresholds["medium"]:
            return 80
        elif gpa >= thresholds["low"]:
            return 65
        else:
            return 50

    def _evaluate_language(self, language_info):
        """评估语言成绩，返回0-100分数"""
        if not language_info or "score" not in language_info:
            return 60

        test_type = language_info.get("test", "").upper()
        try:
            score = float(language_info["score"])
        except ValueError:
            return 60

        if test_type not in self.evaluation_criteria["语言成绩"]["thresholds"]:
            return 70

        thresholds = self.evaluation_criteria["语言成绩"]["thresholds"][test_type]

        if score >= thresholds["high"]:
            return 95
        elif score >= thresholds["medium"]:
            return 80
        elif score >= thresholds["low"]:
            return 65
        else:
            return 50

    def _evaluate_experiences(self, experiences):
        """评估科研/实习经历，返回0-100分数"""
        if not experiences:
            return 50

        # 简单评估：根据经历数量和质量
        count = len(experiences)

        if count >= 3:
            return 90
        elif count >= 2:
            return 75
        elif count >= 1:
            return 60
        else:
            return 40

    def get_improvement_suggestions(self, assessment):
        """根据评估结果给出提升建议"""
        suggestions = []

        if assessment["detailed_scores"]["GPA"] < 80:
            suggestions.append("建议提升GPA至3.3+以增强竞争力")

        if assessment["detailed_scores"]["语言成绩"] < 80:
            suggestions.append("建议刷高语言成绩至TOEFL 100+或IELTS 7.0+")

        if assessment["detailed_scores"]["软背景"] < 75:
            suggestions.append("增加1-2段高质量科研或实习经历")

        return suggestions
