"""
留学规划AI智能体系统配置文件
"""

# 系统配置
SYSTEM_CONFIG = {
    "name": "留学规划专家AI智能体",
    "version": "1.0.0",
    "expert_years": 20,
    "supported_countries": [
        "美国", "英国", "澳大利亚", "加拿大",
        "香港", "新加坡", "马来西亚"
    ]
}

# 学位类型
DEGREE_TYPES = {
    "本科": "Undergraduate",
    "硕士": "Master",
    "博士": "PhD"
}

# GPA计算配置
GPA_CONFIG = {
    "scale_4_0": {
        "A+": 4.0, "A": 4.0, "A-": 3.7,
        "B+": 3.3, "B": 3.0, "B-": 2.7,
        "C+": 2.3, "C": 2.0, "C-": 1.7,
        "D": 1.0, "F": 0.0
    },
    "百分制转换": {
        90: 4.0, 85: 3.7, 82: 3.3,
        78: 3.0, 75: 2.7, 72: 2.3,
        68: 2.0, 64: 1.7, 60: 1.0
    }
}

# 学校梯度分类
SCHOOL_TIERS = {
    "冲刺": "reach",
    "匹配": "match",
    "保底": "safety"
}

# 输出格式配置
OUTPUT_CONFIG = {
    "language": "中文",
    "preserve_english_terms": True,
    "bold_important_dates": True,
    "use_data_support": True,
    "avoid_vague_words": ["顶尖", "优秀", "卓越"]
}

# Agent配置
AGENT_CONFIG = {
    "background_evaluator": {"enabled": True, "priority": 1},
    "gpa_calculator": {"enabled": True, "priority": 2},
    "school_matcher": {"enabled": True, "priority": 3},
    "result_validator": {"enabled": True, "priority": 4},
    "report_generator": {"enabled": True, "priority": 5},
    "timeline_agent": {"enabled": True, "optional": True},
    "essay_advisor": {"enabled": True, "optional": True},
    "interview_coach": {"enabled": True, "optional": True},
    "visa_advisor": {"enabled": True, "optional": True}
}

# 时间线关键节点（月份）
TIMELINE_MILESTONES = {
    "标准化考试": {"start": -12, "end": -3},
    "文书准备": {"start": -6, "end": -1},
    "推荐信收集": {"start": -4, "end": -1},
    "网申提交": {"start": -2, "end": 0},
    "签证准备": {"start": 2, "end": 4}
}
