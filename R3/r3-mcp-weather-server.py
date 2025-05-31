import os
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

import datetime

mcp = FastMCP("", "R3WeatherServer")

@mcp.tool()
def get_weather(location: str, date: str = None) -> str:
    """查詢指定地點與日期的天氣。location 是地點，date 是日期（YYYY-MM-DD，可選）"""
    if not date:
        date = (datetime.date.today() + datetime.timedelta(days=1)).isoformat()
    return f"{location} 在 {date} 的天氣是晴時多雲，氣溫約 26~32 °C。"

if __name__ == "__main__":
    mcp.run(transport="stdio")