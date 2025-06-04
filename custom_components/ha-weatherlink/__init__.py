from .const import DOMAIN

PLATFORMS = ["sensor"]


async def async_setup(hass, config):
    hass.data[DOMAIN] = {}
    return True


async def async_setup_entry(hass, entry):
    # Forward the config entry setup to the sensor platform
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass, entry):
    # Unload the sensor platform
    await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    return True
