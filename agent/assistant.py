import os

from agents import Agent, RunContextWrapper

from context.app_context import AppContext
from memory.retriever import MemoryRetriever
from memory.user_preference import UserPreference
from memory.user_profile import UserProfile
from tools.registry import ToolRegistry


def create_assistant(
        registry: ToolRegistry,
        weather_agent: Agent[AppContext],
        math_agent: Agent[AppContext],
        mcp_servers=None,
) -> Agent[AppContext]:
    """
    创建默认助手。
    """

    return Agent(
        name='Assistant',
        instructions=build_instructions,
        model=os.getenv("LLM_MODEL"),
        handoffs=[
            weather_agent,
            math_agent,
        ],
        tools=registry.get_tools(),
        mcp_servers=mcp_servers or [],
    )

def build_profile_prompt(profile: UserProfile) -> str:

    hobbies = (
        "\n".join(profile.hobbies)
        if profile.hobbies
        else "未知"
    )

    return f"""
当前用户资料：

姓名：{profile.name or "未知"}
年龄：{profile.age or "未知"}
性别：{profile.gender or "未知"}
职业：{profile.job or "未知"}
兴趣：{hobbies}
"""

def build_summary_prompt(context: AppContext) -> str:
    """构建当前会话摘要 prompt。"""
    raw = context.memory.get_summary().summary
    if not raw:
        return ""
    summary = raw.strip()
    if not summary:
        return ""
    return f"""
## 当前会话摘要

{summary}
"""


def build_long_memory_prompt(
        context: AppContext,
        query: str,
) -> str:
    """
    构建长期记忆 prompt
    """

    long_memory = context.memory.get_long_memory()

    if not long_memory.memories:
        return ""

    retrieved = MemoryRetriever.retrieve(
        memories=long_memory.memories,
        query=query,
    )

    if not retrieved:
        return ""

    lines = [
        "## 用户长期记忆"
    ]

    for item in retrieved:
        lines.append(f"- {item.content}")

    return "\n".join(lines)


def build_instructions(
        ctx: RunContextWrapper[AppContext],
        agent: Agent[AppContext],
) -> str:

    profile = ctx.context.memory.get_profile()

    profile_prompt = build_profile_prompt(profile)

    preference =  ctx.context.memory.get_preference()

    preference_prompt = build_preference_prompt(preference)

    summary_prompt = build_summary_prompt(ctx.context)

    long_memory_prompt = build_long_memory_prompt(
        ctx.context,
        ctx.context.current_query,
    )

    return f"""
你是一名企业 AI 助手。

{profile_prompt}

{preference_prompt}

{summary_prompt}

{long_memory_prompt}

请遵循以下规则：
【用户资料规则】
1. 上面的"当前用户资料"来源于 Memory，是用户已经确认过的长期信息。
2. 当用户询问自己的姓名、年龄、职业、兴趣等信息时，应优先使用当前用户资料回答。
3. 不要假装遗忘已经记录的资料。
4. 如果用户提供了新的长期信息，应主动调用 remember_profile 工具更新 Memory。
5.当用户表达长期回答偏好时，例如：

- 以后全部使用中文回答
- 回答简洁一点
- 所有代码给完整代码

请主动调用 remember_preference 工具保存。
6. 如果用户的新信息与已有信息冲突，以用户最新提供的信息为准。
【长期记忆规则】

如果用户表达以下长期信息：

- 请记住……
- 以后记住……
- 长期保存……
- 永远记住……

以及任何未来长期有价值的信息，

请主动调用 remember_memory 工具保存到长期记忆。
【Agent 路由规则】
1. 天气问题交给 Weather Agent。
2. 数学问题交给 Math Agent。
3. 其他问题由你回答。
"""

def build_preference_prompt(
        preference: UserPreference,
) -> str:

    return f"""
用户偏好：

回答语言： {preference.language or "默认" }

回答风格: {preference.response_style or "默认"}

代码风格： {preference.code_style or "默认"}
"""