from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.core import HomeAssistant
from .const import DOMAIN, DEFAULT_UPDATE_INTERVAL
from .davis import DavisWeatherlinkApi
import logging

_LOGGER = logging.getLogger(__name__)


class WeatherlinkCoordinator(DataUpdateCoordinator):
    def __init__(self, hass: HomeAssistant, host: str):
        super().__init__(
            hass,
            _LOGGER,
            name=f"{DOMAIN}_coordinator",
            # Set your desired update interval
            update_interval=timedelta(seconds=DEFAULT_UPDATE_INTERVAL),
        )
        self._api = DavisWeatherlinkApi(host)
        self._host = host

    async def _async_update_data(self):
        try:
            return await self._api.async_get_current_conditions()
        except Exception as err:
            raise UpdateFailed(f"Error communicating with API: {err}")
