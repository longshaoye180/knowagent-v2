from mcp.server import FastMCP

mcp = FastMCP("KnowAgent Demo Server")


@mcp.tool()
def get_company_info(
        company: str,
) -> str:

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