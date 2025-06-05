from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.const import UnitOfLength, UnitOfTemperature, UnitOfPressure, UnitOfSpeed
from .const import DOMAIN

SENSOR_TYPES = {
    "temp": ["Outdoor Temperature", "temperature", "mdi:thermometer", "measurement"],
    "hum": ["Outdoor Humidity", "humidity", "mdi:water-percent", "measurement"],
    "dew_point": ["Dew Point", "temperature", "mdi:weather-fog", "measurement"],
    "rainfall_daily": ["Daily Rainfall", "precipitation", "mdi:weather-rainy", "total"],
    "rainfall_year": ["Yearly Rainfall", "precipitation", "mdi:weather-rainy", "total"],
    "rainfall_monthly": ["Monthly Rainfall", "precipitation", "mdi:weather-rainy", "total"],
    "rainfall_last_15_min": ["Rainfall Last 15 Min", "precipitation", "mdi:weather-rainy", "total"],
    "rainfall_last_60_min": ["Rainfall Last 60 Min", "precipitation", "mdi:weather-rainy", "total"],
    "rainfall_last_24_hr": ["Rainfall Last 24 Hr", "precipitation", "mdi:weather-rainy", "total"],
    "rain_storm": ["Current Storm Rainfall", "precipitation", "mdi:weather-pouring", "total"],
    "rain_storm_last": ["Last Storm Rainfall", "precipitation", "mdi:weather-pouring", "total"],
    "wind_speed_last": ["Wind Speed", "wind_speed", "mdi:weather-windy", "measurement"],
    "wind_dir_last": ["Wind Direction", "wind_direction", "mdi:compass", None],
    "wind_speed_avg_last_1_min": ["Wind Speed Avg 1 Min", "wind_speed", "mdi:weather-windy", "measurement"],
    "wind_dir_scalar_avg_last_1_min": ["Wind Dir Scalar Avg 1 Min", "wind_direction", "mdi:compass", None],
    "wind_speed_avg_last_2_min": ["Wind Speed Avg 2 Min", "wind_speed", "mdi:weather-windy", "measurement"],
    "wind_dir_scalar_avg_last_2_min": ["Wind Dir Scalar Avg 2 Min", "wind_direction", "mdi:compass", None],
    "wind_speed_hi_last_2_min": ["Wind Speed Hi 2 Min", "wind_speed", "mdi:weather-windy", "measurement"],
    "wind_dir_at_hi_speed_last_2_min": ["Wind Dir at Hi Speed 2 Min", "wind_direction", "mdi:compass", None],
    "wind_speed_avg_last_10_min": ["Wind Speed Avg 10 Min", "wind_speed", "mdi:weather-windy", "measurement"],
    "wind_dir_scalar_avg_last_10_min": ["Wind Dir Scalar Avg 10 Min", "wind_direction", "mdi:compass", None],
    "wind_speed_hi_last_10_min": ["Wind Speed Hi 10 Min", "wind_speed", "mdi:weather-windy", "measurement"],
    "wind_dir_at_hi_speed_last_10_min": ["Wind Dir at Hi Speed 10 Min", "wind_direction", "mdi:compass", None],
    "bar_sea_level": ["Barometric Pressure", "pressure", "mdi:gauge", "measurement"],
    "bar_trend": ["Barometric Trend", None, "mdi:trending-up", None],
    "bar_absolute": ["Absolute Pressure", "pressure", "mdi:gauge", "measurement"],
    "temp_in": ["Indoor Temperature", "temperature", "mdi:thermometer", "measurement"],
    "hum_in": ["Indoor Humidity", "humidity", "mdi:water-percent", "measurement"],
    "dew_point_in": ["Indoor Dew Point", "temperature", "mdi:weather-fog", "measurement"],
    "heat_index": ["Heat Index", "temperature", "mdi:thermometer", "measurement"],
    "heat_index_in": ["Indoor Heat Index", "temperature", "mdi:thermometer", "measurement"],
    "wind_chill": ["Wind Chill", "temperature", "mdi:snowflake", "measurement"],
    "solar_rad": ["Solar Radiation", "illuminance", "mdi:white-balance-sunny", "measurement"],
    "uv_index": ["UV Index", "uv_index", "mdi:weather-sunny-alert", "measurement"],
    "wet_bulb": ["Wet Bulb", "temperature", "mdi:thermometer-water", "measurement"],
    "thw_index": ["THW Index", "temperature", "mdi:thermometer", "measurement"],
    "thsw_index": ["THSW Index", "temperature", "mdi:thermometer", "measurement"],
    "rx_state": ["Receiver State", None, "mdi:radio-tower", None],
    "trans_battery_flag": ["Transmitter Battery Flag", None, "mdi:battery-alert", None],
    "rain_size": ["Rain Collector Size", None, "mdi:cup-water", None],
    "rain_rate_last": ["Rain Rate Last", "precipitation_intensity", "mdi:weather-pouring", "measurement"],
    "rain_rate_hi": ["Rain Rate High", "precipitation_intensity", "mdi:weather-pouring", "measurement"],
    "rain_rate_hi_last_15_min": ["Rain Rate Hi Last 15 Min", "precipitation_intensity", "mdi:weather-pouring", "measurement"],
    "rain_storm_start_at": ["Rain Storm Start", None, "mdi:clock-start", None],
    "rain_storm_last_start_at": ["Last Rain Storm Start", None, "mdi:clock-start", None],
    "rain_storm_last_end_at": ["Last Rain Storm End", None, "mdi:clock-end", None],
    # Add more as needed
}


async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    sensors = []

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

    conditions = coordinator.data["data"]["conditions"]

    # Add all sensors for each condition block, but skip those with value None, "Unknown", or null
    for cond in conditions:
        for key in SENSOR_TYPES:
            value = cond.get(key)
            if value not in (None, "Unknown", "null"):
                sensors.append(WeatherlinkSensor(coordinator, key, cond))

    async_add_entities(sensors)


class WeatherlinkSensor(SensorEntity):
    has_entity_name = True

    def __init__(self, coordinator, key, data):
        self.coordinator = coordinator
        self._key = key
        self._data = data
        self._attr_name = SENSOR_TYPES.get(key, [key])[0]
        self._attr_device_class = SENSOR_TYPES.get(
            key, [None, None, None, None])[1]
        self._attr_icon = SENSOR_TYPES.get(key, [None, None, "mdi:cloud"])[2]
        self._attr_state_class = SENSOR_TYPES.get(
            key, [None, None, None, None])[3]

    @property
    def unique_id(self):
        return f"{self.coordinator._host}_{self._key}"

    @property
    def device_class(self):
        return self._attr_device_class

    @property
    def state_class(self):
        return self._attr_state_class

    @property
    def native_unit_of_measurement(self):
        if self.device_class == "precipitation":
            # Show mm if HA is metric, else inch
            if self.hass and self.hass.config.units.length_unit == UnitOfLength.MILLIMETERS:
                return UnitOfLength.MILLIMETERS
            return UnitOfLength.INCHES
        if self.device_class == "temperature":
            # Weatherlink API returns Fahrenheit by default
            return UnitOfTemperature.FAHRENHEIT
        if self.device_class == "humidity":
            return "%"                          # Relative humidity
        if self.device_class == "pressure":
            return UnitOfPressure.INHG          # Weatherlink API returns inches of mercury
        if self.device_class == "wind_speed":
            return UnitOfSpeed.MILES_PER_HOUR   # Weatherlink API returns mph
        return None

    @property
    def suggested_display_precision(self):
        if self.device_class == "precipitation":
            if self.hass and self.hass.config.units.length_unit == UnitOfLength.MILLIMETERS:
                return 1
            return 2
        if self.device_class == "temperature":
            return 1
        if self.device_class == "humidity":
            return 1
        if self.device_class == "pressure":
            return 1
        if self.device_class == "wind_speed":
            return 1
        return None

    @property
    def device_info(self):
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

        rain_count_keys = {
            "rainfall_daily",
            "rainfall_year",
            "rainfall_monthly",
            "rainfall_last_15_min",
            "rainfall_last_60_min",
            "rainfall_last_24_hr",
            "rain_storm",
            "rain_storm_last",
            # Add more rain count fields if needed
        }

        for cond in self.coordinator.data["data"]["conditions"]:
            if self._key in cond:
                # Special handling for all rain count fields
                if self._key in rain_count_keys:
                    rain_size = cond.get("rain_size", 1)
                    count = cond[self._key]
                    # Determine mm per count
                    if self.hass and self.hass.config.units.length_unit == UnitOfLength.MILLIMETERS:
                        # Convert to mm
                        if rain_size == 1:
                            return round(count * 0.254, 2)  # 0.01 inch to mm
                        elif rain_size == 2:
                            return round(count * 0.2, 2)
                        elif rain_size == 3:
                            return round(count * 0.1, 2)
                        elif rain_size == 4:
                            return round(count * 0.0254, 3)  # 0.001 inch to mm
                    else:
                        # Convert to inches
                        if rain_size == 1:
                            return round(count * 0.01, 3)
                        elif rain_size == 2:
                            return round(count * 0.00787, 3)  # 0.2 mm to inch
                        elif rain_size == 3:
                            return round(count * 0.00394, 3)  # 0.1 mm to inch
                        elif rain_size == 4:
                            return round(count * 0.001, 3)
                    # Default fallback
                    return count
                return cond[self._key]
        return None

    async def async_update(self):
        await self.coordinator.async_request_refresh()

    @property
    def available(self):
        return self.coordinator.last_update_success

    @property
    def extra_state_attributes(self):
        return {
            "native_unit_of_measurement": self.native_unit_of_measurement,
        }
