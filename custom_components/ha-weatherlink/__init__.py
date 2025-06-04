from .sensor import WeatherlinkSensor
from .const import DOMAIN


async def async_setup(hass, config):
    hass.data[DOMAIN] = {}
    return True


async def async_setup_entry(hass, entry):
    hass.data[DOMAIN][entry.entry_id] = WeatherlinkSensor(hass, entry)
    await hass.data[DOMAIN][entry.entry_id].async_setup()
    return True


async def async_unload_entry(hass, entry):
    await hass.data[DOMAIN][entry.entry_id].async_unload()
    del hass.data[DOMAIN][entry.entry_id]
    return True
