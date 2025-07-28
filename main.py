from functions.load_json import load_card_json_by_id, load_event_json_by_id
from functions.weather import fetch_weather_data
from mcp.server.fastmcp import FastMCP

app = FastMCP("mcp")

@app.tool("load_card_json_by_id")
async def tool_load_card_json_by_id(card_id: str):
    return await load_card_json_by_id(card_id)

@app.tool("load_event_json_by_id")
async def tool_load_event_json_by_id(event_id: str):
    return await load_event_json_by_id(event_id)

@app.tool("fetch_weather_data")
async def tool_fetch_weather_data(location: str):
    """
    获取指定地点的天气数据。

    返回数据字段说明：
        code           : 请参考状态码
        updateTime     : 当前API的最近更新时间
        fxLink         : 当前数据的响应式页面，便于嵌入网站或应用
        now.obsTime    : 数据观测时间
        now.temp       : 温度，默认单位：摄氏度
        now.feelsLike  : 体感温度，默认单位：摄氏度
        now.icon       : 天气状况的图标代码
        now.text       : 天气状况的文字描述，包括阴晴雨雪等
        now.wind360    : 风向360角度
        now.windDir    : 风向
        now.windScale  : 风力等级
        now.windSpeed  : 风速，公里/小时
        now.humidity   : 相对湿度，百分比数值
        now.precip     : 过去1小时降水量，默认单位：毫米
        now.pressure   : 大气压强，默认单位：百帕
        now.vis        : 能见度，默认单位：公里
        now.cloud      : 云量，百分比数值。可能为空
        now.dew        : 露点温度。可能为空
        refer.sources  : 原始数据来源，或数据源说明，可能为空
        refer.license  : 数据许可或版权声明，可能为空

    参数:
        location (str): 查询地区的 LocationID

    返回:
        dict: 包含天气信息的JSON对象
    """
    return await fetch_weather_data(location)


if __name__ == "__main__":
    app.run(transport="stdio")