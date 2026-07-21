import logging

from mcp.server import FastMCP

logger = logging.getLogger("weather-mcp")

mcp = FastMCP("Weather MCP Server")


@mcp.tool()
def get_weather(
        city: str,
) -> str:

    logger.info("get_weather called: %s", city)

    data = {
        "Beijing": "Sunny",
        "Shanghai": "Cloudy",
    }

    return data.get(city, "Unknown weather")


if __name__ == "__main__":
    mcp.run()