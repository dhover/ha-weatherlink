from .const import DOMAIN
from .coordinator import WeatherlinkCoordinator

PLATFORMS = ["sensor"]


async def async_setup(hass, config):
    hass.data.setdefault(DOMAIN, {})
    return True


async def async_setup_entry(hass, entry):
    # Create and store the coordinator
    coordinator = WeatherlinkCoordinator(hass, entry.data["host"])
    await coordinator.async_config_entry_first_refresh()
    hass.data[DOMAIN][entry.entry_id] = coordinator

    # Forward the config entry setup to the sensor platform
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass, entry):
    await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    hass.data[DOMAIN].pop(entry.entry_id)
    return True
