import aiohttp
import async_timeout
from .const import API_URL


class DavisWeatherlinkApi:
    def __init__(self, host: str):
        self._host = host

    async def async_get_current_conditions(self):
        async with async_timeout.timeout(10):
            async with aiohttp.ClientSession() as session:
                async with session.get(API_URL.format(host=self._host)) as response:
                    response.raise_for_status()
                    return await response.json()
