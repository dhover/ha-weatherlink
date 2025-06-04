from homeassistant import config_entries
from homeassistant.const import CONF_NAME, CONF_HOST
from homeassistant.data_entry_flow import FlowResult
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers import schema
from .const import DOMAIN

import voluptuous as vol


class WeatherlinkConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    def __init__(self):
        super().__init__()
        self.name = None
        self.host = None

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            self.name = user_input[CONF_NAME]
            self.host = user_input.get(CONF_HOST)
            return self.async_create_entry(title=self.name, data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=self._get_schema(),
        )

    def _get_schema(self):
        return vol.Schema({
            vol.Required(CONF_NAME): str,
            vol.Required(CONF_HOST): str,
        })

    async def async_step_zeroconf(self, discovery_info):
        """Handle zeroconf discovery."""
        self.host = discovery_info["host"]
        self.name = discovery_info.get("name", "Weatherlink Live")
        await self.async_set_unique_id(self.host)
        self._abort_if_unique_id_configured()
        return await self.async_step_user({
            CONF_NAME: self.name,
            CONF_HOST: self.host,
        })
