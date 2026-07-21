import logging

from mcp.server import FastMCP

logger = logging.getLogger("knowledge-mcp")

mcp = FastMCP("Knowledge MCP Server")


@mcp.resource("company://{name}/profile")
def company_profile(
        name: str
) -> str:

    logger.info("resource requested: %s", name)

    data = {
        "OpenAI": (
            "OpenAI is an AI research",
            "company."
        ),

        "Alibaba": (
            "Alibaba is a technology",
            "company."
        )
    }

    return data.get(name, "Unknown company")

@mcp.prompt("company_analysis")
def company_analysis(
        company: str,
):
    logger.info("prompt requested: %s", company)

    return [
        {
            "role": "user",
            "content": (
                f"""
请分析公司：

{company}

分析一下内容：

1.公司业务模式
2.核心竞争力
3.潜在风险
"""
            )
        }
    ]

if __name__ == "__main__":
    mcp.run()
