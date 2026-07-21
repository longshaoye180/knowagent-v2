import sys
import logging

from mcp.server import FastMCP

# 配置 logging 输出到 stderr，不影响 stdin/stdout 协议通信
logging.basicConfig(
    stream=sys.stderr,
    level=logging.INFO,
    format="[%(levelname)s] %(message)s",
)
logger = logging.getLogger("company-mcp")

mcp = FastMCP("KnowAgent Demo Server")


@mcp.tool()
def get_company_info(
        company: str,
) -> str:
    logger.info(f"get_company_info called with: {company}")

    data = {
        "OpenAI": "AI research company",
        "Alibaba": "Technology company",
    }

    return data.get(
        company,
        "Unknown company",
    )

if __name__ == "__main__":
    mcp.run()