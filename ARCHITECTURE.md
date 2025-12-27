# 系统架构文档 | System Architecture

## 概述

留学规划AI智能体系统采用**多Agent协作架构**，由一个Commands（总指挥）协调多个专业Agents（助手）完成复杂的留学规划任务。

---

## 核心设计理念

### 1. 分层架构 (Layered Architecture)

```
┌─────────────────────────────────────────┐
│         用户交互层 (main.py)             │
├─────────────────────────────────────────┤
│      Commands层 (commands/planner.py)   │  ← 总指挥
├─────────────────────────────────────────┤
│           Agents层 (agents/)             │  ← 专业助手
│  ┌──────────┬──────────┬──────────┐     │
│  │ 核心评估 │ 增值服务 │ 工具Agent │     │
│  └──────────┴──────────┴──────────┘     │
├─────────────────────────────────────────┤
│      数据层 (knowledge/, config/)        │  ← 知识库和配置
└─────────────────────────────────────────┘
```

### 2. Agent协作模式

**流程图**：
```
用户输入
   ↓
Commands (总指挥)
   ↓
   ├→ BackgroundEvaluator (评估背景)
   │      ↓
   ├→ GPACalculator (计算GPA) [如需要]
   │      ↓
   ├→ SchoolMatcher (匹配学校)
   │      ↓
   ├→ ResultValidator (验证结果)
   │      ↓
   ├→ ReportGenerator (生成报告)
   │      ↓
   └→ 可选服务Agents (时间线/文书/面试/签证)
          ↓
      最终输出
```

---

## 目录结构详解

```
留学规划专家/
│
├── main.py                      # 主入口：启动系统，创建Commands实例
│
├── commands/                    # Commands层：总指挥
│   └── planner.py              # StudyAbroadPlanner类
│       ├── 分步引导用户输入
│       ├── 协调各Agents工作
│       └── 整合结果并呈现
│
├── agents/                      # Agents层：专业助手
│   ├── __init__.py             # Agent模块导出
│   │
│   ├── [核心评估流程]
│   ├── background_evaluator.py  # Agent1: 学生背景评估
│   ├── gpa_calculator.py        # Agent2: GPA计算器
│   ├── school_matcher.py        # Agent3: 学校匹配引擎
│   ├── result_validator.py      # Agent4: 结果验证器
│   ├── report_generator.py      # Agent5: 评估报告生成器
│   │
│   └── [增值服务]
│       ├── timeline_agent.py    # Agent6: 时间线规划器
│       ├── essay_advisor.py     # Agent7: 文书素材挖掘
│       ├── interview_coach.py   # Agent8: 面试辅导
│       └── visa_advisor.py      # Agent9: 签证辅导
│
├── knowledge/                   # 知识库：数据驱动
│   └── schools.json            # 学校数据库（可扩展）
│       ├── 美国院校
│       ├── 英国院校
│       ├── 加拿大院校
│       ├── 香港院校
│       └── 新加坡院校
│
├── config/                      # 配置层：系统参数
│   └── settings.py             # 全局配置
│       ├── GPA评分标准
│       ├── 语言成绩要求
│       ├── Agent优先级
│       └── 输出格式配置
│
├── utils/                       # 工具层：辅助函数
│   └── helpers.py              # 通用工具函数
│
├── README.md                    # 项目说明文档
├── QUICKSTART.md               # 快速开始指南
├── ARCHITECTURE.md             # 本文档：系统架构说明
└── requirements.txt            # 依赖列表
```

---

## 核心组件详解

### 1. Commands (总指挥)

**文件**：`commands/planner.py`
**类**：`StudyAbroadPlanner`

**职责**：
- 管理对话状态（conversation_state）
- 分步引导用户输入（_ask_step_1, _ask_step_2, _ask_step_3）
- 协调Agents执行任务（_process_assessment）
- 提供增值服务选项（_offer_additional_services）

**关键方法**：
```python
start_consultation()         # 启动咨询流程
_ask_step_1()               # 第一步：学位和国家
_ask_step_2()               # 第二步：学术背景
_ask_step_3()               # 第三步：语言和经历
_process_assessment()       # 处理评估流程
_offer_additional_services() # 提供额外服务
```

---

### 2. Agents (专业助手)

#### Agent1: BackgroundEvaluator (背景评估)
**职责**：评估学生综合竞争力
- 输入：学生信息字典
- 输出：评估结果（分数、优劣势、竞争力等级）
- 评分维度：GPA (35%) + 语言 (25%) + 科研 (20%) + 实习 (20%)

#### Agent2: GPACalculator (GPA计算)
**职责**：计算加权GPA
- 支持4.0制字母成绩（A+, B+等）
- 支持百分制（90, 85等）
- 提供目标GPA规划功能

#### Agent3: SchoolMatcher (学校匹配)
**职责**：智能匹配适合的学校
- 加载schools.json数据库
- 根据GPA、语言、竞争力匹配
- 按冲刺/匹配/保底分类
- 计算匹配分数并排序

#### Agent4: ResultValidator (结果验证)
**职责**：验证推荐结果合理性
- 检查每档学校数量
- 验证GPA和语言要求一致性
- 确保总推荐数在合理范围

#### Agent5: ReportGenerator (报告生成)
**职责**：生成格式化的评估报告
- 学生背景概况
- 竞争力评估
- 选校清单（含截止日期）
- 申请建议
- 可导出为txt文件

#### Agent6: TimelineAgent (时间线规划)
**职责**：制定申请时间表
- 8个关键阶段的时间节点
- 每阶段的任务清单
- 风险提示

#### Agent7: EssayAdvisor (文书辅导)
**职责**：文书素材挖掘与立意
- 3个文书角度建议
- 核心叙事逻辑
- 避免陈词滥调提示

#### Agent8: InterviewCoach (面试辅导)
**职责**：面试准备与模拟
- 高频面试问题库
- STAR答题框架
- 学校文化偏好分析

#### Agent9: VisaAdvisor (签证辅导)
**职责**：签证材料与攻略
- 7国签证材料清单
- 资金证明要求
- 拒签原因及应对策略

---

## 数据流图

```
用户 → main.py → Commands
                    ↓
            [收集学生信息]
                    ↓
              student_info = {
                "degree": "硕士",
                "target_countries": ["美国"],
                "gpa": 3.6,
                "language": {"test": "TOEFL", "score": 105},
                "experiences": [...]
              }
                    ↓
         ┌──────────┴──────────┐
         ↓                      ↓
  BackgroundEvaluator    GPACalculator (如需要)
         ↓
   assessment = {
     "overall_score": 85,
     "competitiveness": "中等竞争力",
     "strengths": [...],
     "weaknesses": [...]
   }
         ↓
   SchoolMatcher
         ↓
   recommendations = {
     "冲刺": [school1, school2, ...],
     "匹配": [school3, school4, ...],
     "保底": [school5, school6, ...]
   }
         ↓
   ResultValidator
         ↓
   (验证通过)
         ↓
   ReportGenerator
         ↓
   formatted_report (文本)
         ↓
   显示给用户
         ↓
   提供增值服务选项
         ↓
   TimelineAgent / EssayAdvisor /
   InterviewCoach / VisaAdvisor
```

---

## 配置管理

### config/settings.py

**关键配置项**：

1. **SYSTEM_CONFIG**：系统基本信息
2. **GPA_CONFIG**：GPA计算标准
3. **SCHOOL_TIERS**：学校梯度分类
4. **AGENT_CONFIG**：Agent优先级和启用状态
5. **TIMELINE_MILESTONES**：时间线关键节点

**可定制性**：
- 修改评分权重
- 调整GPA转换标准
- 自定义Agent工作流程

---

## 知识库管理

### knowledge/schools.json

**数据结构**：
```json
{
  "国家名": [
    {
      "name": "英文校名",
      "中文名": "中文校名",
      "ranking": 排名,
      "tier": "梯度",
      "gpa_requirement": GPA要求,
      "toefl_requirement": TOEFL要求,
      "ielts_requirement": IELTS要求,
      "programs": ["专业列表"],
      "deadline": "截止日期",
      "match_reason": "匹配理由"
    }
  ]
}
```

**扩展方式**：
1. 编辑 `schools.json`
2. 按格式添加新学校
3. 系统自动加载更新后的数据

---

## 错误处理与容错

### 1. 数据缺失处理
- GPA缺失：提供计算器选项
- 语言成绩缺失：默认分数60
- 经历缺失：降低软背景分数

### 2. 文件缺失容错
- schools.json不存在：使用内置样例数据
- 导入失败：提示用户并优雅退出

### 3. 用户输入验证
- 学位类型：限定3种选项
- GPA范围：合理性检查
- 语言成绩：格式验证

---

## 扩展指南

### 添加新Agent

1. 在 `agents/` 目录创建新文件
2. 实现Agent类和核心方法
3. 在 `agents/__init__.py` 中导出
4. 在 `commands/planner.py` 中集成

**示例**：
```python
# agents/scholarship_advisor.py
class ScholarshipAdvisor:
    def recommend_scholarships(self, student_info):
        # 实现奖学金推荐逻辑
        pass
```

### 添加新国家/地区

1. 编辑 `knowledge/schools.json`
2. 添加新国家的学校数据
3. 更新 `config/settings.py` 中的 `supported_countries`
4. （可选）在 `visa_advisor.py` 中添加签证信息

---

## 性能优化建议

1. **数据缓存**：缓存已加载的schools.json
2. **并行处理**：部分Agent可并行执行
3. **懒加载**：按需加载知识库数据
4. **索引优化**：为学校数据建立索引

---

## 安全性考虑

1. **输入验证**：所有用户输入需验证
2. **数据隐私**：不保存敏感个人信息
3. **文件权限**：适当的文件读写权限
4. **异常捕获**：全局异常处理机制

---

## 未来架构演进

### Phase 2: Web化
- Flask/FastAPI后端
- React前端界面
- RESTful API设计

### Phase 3: 数据库集成
- SQLite/PostgreSQL存储用户数据
- 历史案例库
- 录取数据分析

### Phase 4: AI增强
- 集成LLM（GPT-4等）
- 智能对话式交互
- 个性化推荐算法优化

---

## 总结

本系统采用**模块化、可扩展**的多Agent架构，通过Commands协调各专业Agents完成复杂任务。系统设计遵循：

- ✅ **单一职责**：每个Agent专注一个功能
- ✅ **松耦合**：Agents之间独立工作
- ✅ **可扩展**：易于添加新Agent和新数据
- ✅ **数据驱动**：知识库与代码分离
- ✅ **用户友好**：分步引导，清晰呈现

---

**版本**：v1.0.0
**更新日期**：2024-12
