import aiohttp
from dotenv import load_dotenv
import os

load_dotenv()
async def fetch_weather_data(location):
    api_url = f"https://{os.getenv("WEATHER_API_URL")}/v7/weather/now?location={location}"
    headers = {
        "X-QW-Api-Key" : f"{os.getenv("WEATHER_API_KEY")}",
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url, headers=headers) as response:
            if response.status == 200:
                return await response.json()
            else:
                print(f"Error fetching weather data: {response.status}")
                return None