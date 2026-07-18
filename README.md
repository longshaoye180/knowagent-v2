# KnowAgent v2

一个基于 [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) 构建的多智能体（Multi-Agent）AI 助手系统，支持工具调用、记忆管理、会话摘要和反思等能力。

## 项目结构

```
knowagent-v2/
├── agent/                  # Agent 定义
│   ├── assistant.py        # 默认助手 Agent（路由入口）
│   ├── math_agent.py       # 数学 Agent
│   ├── weather_agent.py    # 天气 Agent
│   ├── planner_agent.py    # 规划 Agent
│   ├── reflection_agent.py # 反思 Agent
│   └── summary_agent.py    # 摘要 Agent
├── app/
│   └── main.py             # 应用入口
├── context/
│   └── app_context.py      # 应用上下文（携带 Memory 等）
├── guardrails/
│   └── input_guardrail.py  # 输入护栏
├── memory/                 # 记忆系统
│   ├── memory.py           # 记忆数据模型
│   ├── memory_store.py     # 记忆存储
│   ├── memory_lifecycle.py # 记忆生命周期管理
│   ├── retriever.py        # 记忆检索
│   ├── semantic_retriever.py # 语义检索
│   ├── scorer.py           # 记忆评分
│   ├── embedding.py        # 嵌入向量
│   ├── conversation_summary.py # 会话摘要
│   ├── long_memory.py      # 长期记忆
│   ├── user_profile.py     # 用户资料
│   └── user_preference.py  # 用户偏好
├── models/
│   └── weather_result.py   # 数据模型
├── runtime/
│   └── logger.py           # 运行时日志
├── service/                # 服务层
│   ├── memory_service.py   # 记忆服务
│   ├── reflection_service.py # 反思服务
│   └── summary_service.py  # 摘要服务
├── tools/                  # 工具集
│   ├── calculator.py       # 计算器工具
│   ├── weather.py          # 天气查询工具
│   ├── profile.py          # 用户资料工具
│   ├── preference.py       # 用户偏好工具
│   ├── remember_memory.py  # 记忆保存工具
│   └── registry.py         # 工具注册中心
├── pyproject.toml
└── uv.lock
```

## 功能特性

- **多 Agent 协作**：Assistant 作为路由入口，根据用户意图自动分发给天气、数学等业务 Agent
- **工具调用**：支持计算器、天气查询、用户资料管理等工具
- **记忆系统**：支持用户资料、偏好设置、长期记忆的存储与检索
- **会话摘要**：自动生成会话摘要，保持长对话的上下文连贯性
- **反思机制**：Agent 可对自身回答进行反思和优化
- **护栏机制**：输入内容安全检查

## 环境要求

- Python >= 3.11
- [uv](https://github.com/astral-sh/uv) 包管理器（推荐）

## 快速开始

### 1. 克隆项目

```bash
git clone git@github.com:longshaoye180/knowagent-v2.git
cd knowagent-v2
```

### 2. 安装依赖

```bash
uv sync
```

### 3. 配置环境变量

创建 `.env` 文件：

```env
LLM_API_KEY=your_api_key
LLM_BASE_URL=https://api.openai.com/v1
LLM_MODEL=gpt-4o
```

### 4. 运行

```bash
uv run python app/main.py
```

在交互式命令行中输入问题，输入 `exit` 退出。

## 使用示例

```
User> 今天北京天气怎么样？
[Weather Agent 被调用，返回天气信息]

User> 计算 (123 + 456) * 7
[Math Agent 被调用，返回计算结果]

User> 记住我喜欢的颜色是蓝色
[调用 remember_memory 工具，保存到长期记忆]

User> 以后请用中文回答
[调用 remember_preference 工具，保存用户偏好]
```

## 技术栈

- **Agent 框架**：OpenAI Agents SDK (openai-agents)
- **嵌入模型**：sentence-transformers
- **会话存储**：SQLite
- **异步运行时**：asyncio

## License

MIT
