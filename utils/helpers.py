"""
工具函数模块
Utility functions for the Study Abroad Planning AI Agent System
"""


def format_currency(amount, currency="USD"):
    """
    格式化货币显示
    :param amount: 金额
    :param currency: 货币类型
    :return: 格式化字符串
    """
    currency_symbols = {
        "USD": "$",
        "GBP": "£",
        "EUR": "€",
        "CNY": "¥",
        "CAD": "C$",
        "AUD": "A$",
        "HKD": "HK$",
        "SGD": "S$"
    }

    symbol = currency_symbols.get(currency, currency)
    return f"{symbol}{amount:,.2f}"


def calculate_age(birth_year, current_year=2024):
    """
    计算年龄
    :param birth_year: 出生年份
    :param current_year: 当前年份
    :return: 年龄
    """
    return current_year - birth_year


def validate_email(email):
    """
    简单的邮箱验证
    :param email: 邮箱地址
    :return: 是否有效
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def truncate_text(text, max_length=100, suffix="..."):
    """
    截断文本
    :param text: 原文本
    :param max_length: 最大长度
    :param suffix: 后缀
    :return: 截断后的文本
    """
    if len(text) <= max_length:
        return text

    return text[:max_length - len(suffix)] + suffix


def parse_grade_range(grade_text):
    """
    解析成绩范围字符串
    例如："3.5-3.7" -> (3.5, 3.7)
    :param grade_text: 成绩范围文本
    :return: (最小值, 最大值)
    """
    try:
        if "-" in grade_text:
            parts = grade_text.split("-")
            return float(parts[0]), float(parts[1])
        else:
            val = float(grade_text)
            return val, val
    except ValueError:
        return None, None


# 预留：可以添加更多工具函数
# - 日期处理
# - 文件操作
# - 数据验证
# - 格式转换
# 等等
