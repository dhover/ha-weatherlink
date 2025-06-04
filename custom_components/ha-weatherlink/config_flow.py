from homeassistant import config_entries
from homeassistant.const import CONF_NAME, CONF_HOST
import voluptuous as vol
from .const import DOMAIN


class WeatherlinkConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(
                title=user_input[CONF_NAME],
                data=user_input,
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_NAME, description="A name for this Weatherlink device"): str,
                vol.Required(CONF_HOST, description="IP address or hostname of your Weatherlink Live"): str,
            }),
            description_placeholders={
                "name": "Weather Station",
                "host": "192.168.1.100"
            }
        )
