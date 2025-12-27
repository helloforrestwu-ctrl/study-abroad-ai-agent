"""
School Matcher Agent - 学校匹配引擎
根据学生背景智能匹配适合的学校和项目
"""

import json
import os


class SchoolMatcher:
    """学校匹配Agent"""

    def __init__(self):
        # 加载学校数据库
        self.schools_db = self._load_schools_database()

    def _load_schools_database(self):
        """加载学校数据库"""
        db_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "knowledge", "schools.json"
        )

        try:
            with open(db_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            # 如果数据库文件不存在，使用内置样例数据
            return self._get_sample_schools()

    def _get_sample_schools(self):
        """获取样例学校数据（当数据库文件不存在时使用）"""
        return {
            "美国": [
                {
                    "name": "Massachusetts Institute of Technology",
                    "中文名": "麻省理工学院",
                    "ranking": 1,
                    "tier": "冲刺",
                    "gpa_requirement": 3.7,
                    "toefl_requirement": 100,
                    "ielts_requirement": 7.0,
                    "programs": ["Computer Science", "Electrical Engineering", "AI/ML"],
                    "deadline": "2024-12-15",
                    "match_reason": "AI/ML研究实力全球第一，适合有强科研背景的申请者"
                },
                {
                    "name": "Carnegie Mellon University",
                    "中文名": "卡内基梅隆大学",
                    "ranking": 3,
                    "tier": "冲刺",
                    "gpa_requirement": 3.6,
                    "toefl_requirement": 100,
                    "ielts_requirement": 7.0,
                    "programs": ["Computer Science", "Software Engineering", "AI"],
                    "deadline": "2024-12-15",
                    "match_reason": "CS专业顶尖，重视项目经验和编程能力"
                },
                {
                    "name": "University of California, Berkeley",
                    "中文名": "加州大学伯克利分校",
                    "ranking": 4,
                    "tier": "匹配",
                    "gpa_requirement": 3.5,
                    "toefl_requirement": 90,
                    "ielts_requirement": 7.0,
                    "programs": ["EECS", "Data Science", "Business Analytics"],
                    "deadline": "2024-12-01",
                    "match_reason": "公立名校，工程和商科结合紧密，注重创新能力"
                },
                {
                    "name": "University of Southern California",
                    "中文名": "南加州大学",
                    "ranking": 25,
                    "tier": "匹配",
                    "gpa_requirement": 3.3,
                    "toefl_requirement": 90,
                    "ielts_requirement": 6.5,
                    "programs": ["Computer Science", "Data Science", "Game Design"],
                    "deadline": "2025-01-15",
                    "match_reason": "地理位置佳，就业资源丰富，对国际生友好"
                },
                {
                    "name": "Northeastern University",
                    "中文名": "东北大学",
                    "ranking": 49,
                    "tier": "保底",
                    "gpa_requirement": 3.0,
                    "toefl_requirement": 85,
                    "ielts_requirement": 6.5,
                    "programs": ["Computer Science", "Information Systems"],
                    "deadline": "2025-02-01",
                    "match_reason": "Co-op项目突出，实习机会多，适合注重就业的申请者"
                }
            ],
            "英国": [
                {
                    "name": "University of Cambridge",
                    "中文名": "剑桥大学",
                    "ranking": 2,
                    "tier": "冲刺",
                    "gpa_requirement": 3.8,
                    "toefl_requirement": 110,
                    "ielts_requirement": 7.5,
                    "programs": ["Computer Science", "Machine Learning"],
                    "deadline": "2024-12-01",
                    "match_reason": "学术声誉世界顶尖，适合纯学术路线申请者"
                },
                {
                    "name": "Imperial College London",
                    "中文名": "帝国理工学院",
                    "ranking": 6,
                    "tier": "匹配",
                    "gpa_requirement": 3.5,
                    "toefl_requirement": 100,
                    "ielts_requirement": 7.0,
                    "programs": ["AI", "Computing", "Data Science"],
                    "deadline": "2025-01-15",
                    "match_reason": "工科强校，AI方向投入大，地处伦敦就业便利"
                },
                {
                    "name": "University of Edinburgh",
                    "中文名": "爱丁堡大学",
                    "ranking": 15,
                    "tier": "保底",
                    "gpa_requirement": 3.2,
                    "toefl_requirement": 92,
                    "ielts_requirement": 6.5,
                    "programs": ["AI", "Data Science"],
                    "deadline": "2025-03-01",
                    "match_reason": "AI历史悠久，学费相对友好，生活成本适中"
                }
            ]
        }

    def match_schools(self, student_info, assessment):
        """
        根据学生背景和评估结果匹配学校
        :param student_info: 学生信息
        :param assessment: 背景评估结果
        :return: 推荐学校列表
        """
        print("🎯 SchoolMatcher Agent 开始匹配学校...")

        target_countries = student_info.get("target_countries", ["美国"])
        gpa = student_info.get("gpa", 0)
        language_info = student_info.get("language", {})

        # 获取语言成绩
        try:
            language_score = float(language_info.get("score", 0))
        except ValueError:
            language_score = 0

        language_test = language_info.get("test", "TOEFL").upper()

        recommendations = {
            "冲刺": [],
            "匹配": [],
            "保底": []
        }

        # 遍历目标国家的学校
        for country in target_countries:
            if country not in self.schools_db:
                continue

            schools = self.schools_db[country]

            for school in schools:
                # 检查GPA要求
                if gpa < school["gpa_requirement"] - 0.3:
                    continue

                # 检查语言要求
                if language_test == "TOEFL":
                    if language_score < school["toefl_requirement"] - 10:
                        continue
                elif language_test == "IELTS":
                    if language_score < school["ielts_requirement"] - 0.5:
                        continue

                # 确定梯度
                tier = self._determine_tier(gpa, language_score, language_test,
                                            school, assessment["competitiveness"])

                # 添加到推荐列表
                recommendations[tier].append({
                    "school": school,
                    "country": country,
                    "match_score": self._calculate_match_score(
                        gpa, language_score, school, assessment
                    )
                })

        # 排序：按匹配分数降序
        for tier in recommendations:
            recommendations[tier].sort(key=lambda x: x["match_score"], reverse=True)

        # 限制每个梯度最多5所学校
        for tier in recommendations:
            recommendations[tier] = recommendations[tier][:5]

        print(f"✅ 匹配完成 - 冲刺{len(recommendations['冲刺'])}所, "
              f"匹配{len(recommendations['匹配'])}所, "
              f"保底{len(recommendations['保底'])}所")

        return recommendations

    def _determine_tier(self, gpa, language_score, language_test, school, competitiveness):
        """确定学校梯度（冲刺/匹配/保底）"""
        gpa_req = school["gpa_requirement"]
        lang_req = school["toefl_requirement"] if language_test == "TOEFL" else school["ielts_requirement"]

        # GPA差距
        gpa_gap = gpa - gpa_req
        lang_gap = language_score - lang_req

        # 综合判断
        if gpa_gap >= 0 and lang_gap >= 0:
            if competitiveness == "强竞争力":
                return "匹配"
            else:
                return "保底"
        elif gpa_gap >= -0.2 and lang_gap >= -5:
            return "匹配"
        else:
            return "冲刺"

    def _calculate_match_score(self, gpa, language_score, school, assessment):
        """计算匹配分数"""
        # 基础分
        score = 50

        # GPA匹配度
        gpa_gap = gpa - school["gpa_requirement"]
        if gpa_gap >= 0:
            score += min(gpa_gap * 10, 20)
        else:
            score += gpa_gap * 15

        # 语言匹配度（简化）
        score += min(language_score / 10, 15)

        # 整体竞争力加成
        if assessment["competitiveness"] == "强竞争力":
            score += 10

        return round(score, 1)
