from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN

TEMP_FAHRENHEIT = "°F"
PRESSURE_INHG = "inHg"
PERCENTAGE = "%"

SENSOR_TYPES = {
    "temp": ["Outdoor Temperature", TEMP_FAHRENHEIT, "mdi:thermometer"],
    "hum": ["Outdoor Humidity", PERCENTAGE, "mdi:water-percent"],
    "dew_point": ["Dew Point", TEMP_FAHRENHEIT, "mdi:weather-fog"],
    "rainfall_daily": ["Daily Rainfall", "in", "mdi:weather-rainy"],
    "wind_speed_last": ["Wind Speed", "mph", "mdi:weather-windy"],
    "bar_sea_level": ["Barometric Pressure", PRESSURE_INHG, "mdi:gauge"],
    # Add more as needed
}


async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    sensors = []

    # Guard: Ensure data is present and has "conditions"
    if (
        not coordinator.data
        or "data" not in coordinator.data
        or "conditions" not in coordinator.data["data"]
    ):
        import logging
        logging.getLogger(__name__).warning(
            "Weatherlink API did not return 'data.conditions'. Data: %s", coordinator.data
        )
        return

    # Use the correct path to conditions
    conditions = coordinator.data["data"]["conditions"]

    # Find the first outdoor conditions (data_structure_type == 1)
    outdoor = next((c for c in conditions if c.get(
        "data_structure_type") == 1), None)
    indoor = next((c for c in conditions if c.get(
        "data_structure_type") == 4), None)
    bar = next((c for c in conditions if c.get(
        "data_structure_type") == 3), None)

    # Outdoor sensors
    if outdoor:
        for key in ["temp", "hum", "dew_point", "rainfall_daily", "wind_speed_last"]:
            if key in outdoor:
                sensors.append(WeatherlinkSensor(coordinator, key, outdoor))
    # Indoor sensors
    if indoor:
        for key in ["temp_in", "hum_in", "dew_point_in"]:
            if key in indoor:
                sensors.append(WeatherlinkSensor(coordinator, key, indoor))
    # Barometric sensors
    if bar:
        for key in ["bar_sea_level"]:
            if key in bar:
                sensors.append(WeatherlinkSensor(coordinator, key, bar))

    async_add_entities(sensors)


class WeatherlinkSensor(SensorEntity):
    def __init__(self, coordinator, key, data):
        self.coordinator = coordinator
        self._key = key
        self._data = data
        self._attr_name = SENSOR_TYPES.get(key, [key])[0]
        self._attr_icon = SENSOR_TYPES.get(key, [None, None, "mdi:cloud"])[2]
        self._attr_native_unit_of_measurement = SENSOR_TYPES.get(key, [None, None])[
            1]

    @property
    def unique_id(self):
        return f"{self.coordinator._host}_{self._key}"

    @property
    def device_info(self):
        # Use the device ID and host from the coordinator data
        device_id = None
        if (
            self.coordinator.data
            and "data" in self.coordinator.data
            and "did" in self.coordinator.data["data"]
        ):
            device_id = self.coordinator.data["data"]["did"]
        return {
            "identifiers": {(DOMAIN, device_id or self.coordinator._host)},
            "name": "Weatherlink Live",
            "manufacturer": "Davis Instruments",
            "model": "Weatherlink Live",
            "sw_version": None,
            "configuration_url": f"http://{self.coordinator._host}/",
        }

    @property
    def native_value(self):
        if (
            not self.coordinator.data
            or "data" not in self.coordinator.data
            or "conditions" not in self.coordinator.data["data"]
        ):
            return None
        for cond in self.coordinator.data["data"]["conditions"]:
            if self._key in cond:
                return cond[self._key]
        return None

    async def async_update(self):
        await self.coordinator.async_request_refresh()

    @property
    def available(self):
        return self.coordinator.last_update_success
