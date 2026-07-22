import os

from agents import Agent, RunContextWrapper, TResponseInputItem, GuardrailFunctionOutput, Runner, input_guardrail, \
    output_guardrail
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


class OutputSafetyResult(BaseModel):
    is_safe: bool
    reason: str


output_guardrail_agent = Agent(
    name="Output Safety Checker",
    model=os.getenv("LLM_MODEL"),
    instructions="""
你是一个输出内容合规检查 Agent。
审查助手生成的最终回答是否安全合规。

禁止：
- 泄露敏感个人隐私（如身份证、银行卡）
- 包含恶意攻击性言论或违禁内容
- 包含未经验证的系统内部凭据

允许：
- 正常的业务解答与代码示范
- 合规的系统提示   
""",
    output_type=OutputSafetyResult,
)


@output_guardrail
async def output_safety_guardrail(
        ctx: RunContextWrapper,
        agent: Agent,
        output: str,
) -> GuardrailFunctionOutput:
    result = await Runner.run(
        starting_agent=guardrail_agent,
        input=output,
        context=ctx.context
    )

    output_check = result.final_output

    return GuardrailFunctionOutput(
        output_info=output_check,
        tripwire_triggered=(not output_check.is_safe),
    )