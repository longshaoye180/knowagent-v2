import os

from agents import Agent, RunContextWrapper, TResponseInputItem, GuardrailFunctionOutput, Runner, input_guardrail
from pydantic import BaseModel


class SafetyCheckResult(BaseModel):
    allowed: bool
    reason: str

guardrail_agent = Agent(
    name="Safety Checker",

    model=os.getenv("LLM_MODEL"),

    instructions="""
你是一个安全检查 Agent。
判断用户请求是否允许执行。
禁止：
- 删除数据
- 绕过权限
- 非法攻击

允许：

- 正常查询
- 学习问题
- 普通业务请求    
""",
    output_type=SafetyCheckResult,
)


@input_guardrail
async def safety_guardrail(
        ctx: RunContextWrapper,
        agent: Agent,
        input: str | list[TResponseInputItem],
) -> GuardrailFunctionOutput:

    result = await Runner.run(
        starting_agent=guardrail_agent,
        input=input,
        context=ctx.context
    )

    output = result.final_output

    return GuardrailFunctionOutput(
        output_info=output,

        tripwire_triggered=(
            not output.allowed
        )
    )


