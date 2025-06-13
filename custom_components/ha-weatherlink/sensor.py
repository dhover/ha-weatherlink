from homeassistant.const import UnitOfLength, UnitOfTemperature, UnitOfPressure, UnitOfSpeed, CONCENTRATION_MICROGRAMS_PER_CUBIC_METER
from homeassistant.components.sensor import SensorStateClass, SensorDeviceClass, SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN

SENSOR_TYPES = {
    "bar_sea_level": {
        "name": "Barometric Pressure",
        "device_class": "pressure",
        "icon": "mdi:gauge",
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": UnitOfPressure.INHG,
    },
    "bar_trend": {
        "name": "Barometric Trend",
        "device_class": None,
        "icon": "mdi:trending-up",
        "state_class": None,
        "unit": None,
    },
    "bar_absolute": {
        "name": "Absolute Pressure",
        "device_class": "pressure",
        "icon": "mdi:gauge",
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": UnitOfPressure.INHG,
    },
    "dew_point": {
        "name": "Dew Point",
        "device_class": "temperature",
        "icon": "mdi:weather-fog",
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": UnitOfTemperature.FAHRENHEIT,
    },
    "dew_point_in": {
        "name": "Indoor Dew Point",
        "device_class": "temperature",
        "icon": "mdi:weather-fog",
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": UnitOfTemperature.FAHRENHEIT,
    },
    "heat_index": {
        "name": "Heat Index",
        "device_class": "temperature",
        "icon": "mdi:thermometer",
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": UnitOfTemperature.FAHRENHEIT,
    },
    "heat_index_in": {
        "name": "Indoor Heat Index",
        "device_class": "temperature",
        "icon": "mdi:thermometer",
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": UnitOfTemperature.FAHRENHEIT,
    },
    "hum": {
        "name": "Outdoor Humidity",
        "device_class": "humidity",
        "icon": "mdi:water-percent",
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": "%",
    },
    "hum_in": {
        "name": "Indoor Humidity",
        "device_class": "humidity",
        "icon": "mdi:water-percent",
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": "%",
    },
    "last_report_time": {
        "name": "Time Last Report",
        "device_class": None,
        "icon": None,
        "state_class": None,
        "unit": None,
    },
    "pm_1_last": {
        "name": "PM 1.0 Last",
        "device_class": SensorDeviceClass.PM1,
        "icon": None,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
    },
    "pm_2p5_last": {
        "name": "PM 2.5 Last",
        "device_class": SensorDeviceClass.PM25,
        "icon": None,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
    },
    "pm_10_last": {
        "name": "PM 10 Last",
        "device_class": SensorDeviceClass.PM10,
        "icon": None,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
    },
    "pm_1": {
        "name": "PM 1.0",
        "device_class": SensorDeviceClass.PM1,
        "icon": None,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
    },
    "pm_2p5": {
        "name": "PM 2.5",
        "device_class": SensorDeviceClass.PM25,
        "icon": None,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
    },
    "pm_2p5_last_1_hour": {
        "name": "PM 2.5 Last 1h",
        "device_class": SensorDeviceClass.PM25,
        "icon": None,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
    },
    "pm_2p5_last_3_hours": {
        "name": "PM 2.5 Last 3h",
        "device_class": SensorDeviceClass.PM25,
        "icon": None,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
    },
    "pm_2p5_last_24_hours": {
        "name": "PM 2.5 Last 24h",
        "device_class": SensorDeviceClass.PM25,
        "icon": None,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
    },
    "pm_2p5_nowcast": {
        "name": "PM 2.5 Nowcast",
        "device_class": SensorDeviceClass.PM25,
        "icon": None,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
    },
    "pm_10": {
        "name": "PM 10",
        "device_class": SensorDeviceClass.PM10,
        "icon": None,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
    },
    "pm_10_last_1_hour": {
        "name": "PM 10 Last 1h",
        "device_class": SensorDeviceClass.PM10,
        "icon": None,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
    },
    "pm_10_last_3_hours": {
        "name": "PM 10 Last 3h",
        "device_class": SensorDeviceClass.PM10,
        "icon": None,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
    },
    "pm_10_last_24_hours": {
        "name": "PM 10 Last 24h",
        "device_class": SensorDeviceClass.PM10,
        "icon": None,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
    },
    "pm_10_nowcast": {
        "name": "PM 10 Nowcast",
        "device_class": SensorDeviceClass.PM10,
        "icon": None,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
    },
    "pct_pm_data_last_1_hour": {
        "name": "PM Data Last 1h",
        "device_class": None,
        "icon": None,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": "%",
    },
    "pct_pm_data_last_3_hours": {
        "name": "PM Data Last 3h",
        "device_class": None,
        "icon": None,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": "%",
    },
    "pct_pm_data_last_24_hours": {
        "name": "PM Data Last 24h",
        "device_class": None,
        "icon": None,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": "%",
    },
    "pct_pm_data_nowcast": {
        "name": "PM Data Nowcast",
        "device_class": None,
        "icon": None,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": "%",
    },
    "rainfall_daily": {
        "name": "Daily Rainfall",
        "device_class": "precipitation",
        "icon": "mdi:weather-rainy",
        "state_class": SensorStateClass.TOTAL,
        "unit": UnitOfLength.INCHES,
    },
    "rainfall_last_15_min": {
        "name": "Rainfall Last 15 Min",
        "device_class": "precipitation",
        "icon": "mdi:weather-rainy",
        "state_class": SensorStateClass.TOTAL,
        "unit": UnitOfLength.INCHES,
    },
    "rainfall_last_60_min": {
        "name": "Rainfall Last 60 Min",
        "device_class": "precipitation",
        "icon": "mdi:weather-rainy",
        "state_class": SensorStateClass.TOTAL,
        "unit": UnitOfLength.INCHES,
    },
    "rainfall_last_24_hr": {
        "name": "Rainfall Last 24 Hr",
        "device_class": "precipitation",
        "icon": "mdi:weather-rainy",
        "state_class": SensorStateClass.TOTAL,
        "unit": UnitOfLength.INCHES,
    },
    "rainfall_monthly": {
        "name": "Monthly Rainfall",
        "device_class": "precipitation",
        "icon": "mdi:weather-rainy",
        "state_class": SensorStateClass.TOTAL,
        "unit": UnitOfLength.INCHES,
    },
    "rainfall_year": {
        "name": "Yearly Rainfall",
        "device_class": "precipitation",
        "icon": "mdi:weather-rainy",
        "state_class": SensorStateClass.TOTAL,
        "unit": UnitOfLength.INCHES,
    },
    "rain_rate_hi": {
        "name": "Rain Rate High",
        "device_class": "precipitation_intensity",
        "icon": "mdi:weather-pouring",
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": f"{UnitOfLength.INCHES}/h",
    },
    "rain_rate_hi_last_15_min": {
        "name": "Rain Rate Hi Last 15 Min",
        "device_class": "precipitation_intensity",
        "icon": "mdi:weather-pouring",
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": f"{UnitOfLength.INCHES}/h",
    },
    "rain_rate_last": {
        "name": "Rain Rate Last",
        "device_class": "precipitation_intensity",
        "icon": "mdi:weather-pouring",
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": f"{UnitOfLength.INCHES}/h",
    },
    "rain_size": {
        "name": "Rain Collector Size",
        "device_class": None,
        "icon": "mdi:cup-water",
        "state_class": None,
        "unit": None,
    },
    "rain_storm": {
        "name": "Current Storm Rainfall",
        "device_class": "precipitation",
        "icon": "mdi:weather-pouring",
        "state_class": SensorStateClass.TOTAL,
        "unit": UnitOfLength.INCHES,
    },
    "rain_storm_last": {
        "name": "Last Storm Rainfall",
        "device_class": "precipitation",
        "icon": "mdi:weather-pouring",
        "state_class": SensorStateClass.TOTAL,
        "unit": UnitOfLength.INCHES,
    },
    "rain_storm_last_end_at": {
        "name": "Last Rain Storm End",
        "device_class": None,
        "icon": "mdi:clock-end",
        "state_class": None,
        "unit": None,
    },
    "rain_storm_last_start_at": {
        "name": "Last Rain Storm Start",
        "device_class": None,
        "icon": "mdi:clock-start",
        "state_class": None,
        "unit": None,
    },
    "rain_storm_start_at": {
        "name": "Rain Storm Start",
        "device_class": None,
        "icon": "mdi:clock-start",
        "state_class": None,
        "unit": None,
    },
    "rx_state": {
        "name": "Receiver State",
        "device_class": None,
        "icon": "mdi:radio-tower",
        "state_class": None,
        "unit": None,
    },
    "solar_rad": {
        "name": "Solar Radiation",
        "device_class": "illuminance",
        "icon": "mdi:white-balance-sunny",
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": "W/m²",
    },
    "temp": {
        "name": "Outdoor Temperature",
        "device_class": "temperature",
        "icon": "mdi:thermometer",
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": UnitOfTemperature.FAHRENHEIT,
    },
    "temp_in": {
        "name": "Indoor Temperature",
        "device_class": "temperature",
        "icon": "mdi:thermometer",
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": UnitOfTemperature.FAHRENHEIT,
    },
    "thsw_index": {
        "name": "THSW Index",
        "device_class": "temperature",
        "icon": "mdi:thermometer",
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": UnitOfTemperature.FAHRENHEIT,
    },
    "thw_index": {
        "name": "THW Index",
        "device_class": "temperature",
        "icon": "mdi:thermometer",
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": UnitOfTemperature.FAHRENHEIT,
    },
    "trans_battery_flag": {
        "name": "Transmitter Battery Flag",
        "device_class": None,
        "icon": "mdi:battery-alert",
        "state_class": None,
        "unit": None,
    },
    "uv_index": {
        "name": "UV Index",
        "device_class": "uv_index",
        "icon": "mdi:weather-sunny-alert",
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": None,
    },
    "wet_bulb": {
        "name": "Wet Bulb",
        "device_class": "temperature",
        "icon": "mdi:thermometer-water",
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": UnitOfTemperature.FAHRENHEIT,
    },
    "wind_speed_last": {
        "name": "Wind Speed",
        "device_class": "wind_speed",
        "icon": "mdi:weather-windy",
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": UnitOfSpeed.MILES_PER_HOUR,
    },
    "wind_dir_last": {
        "name": "Wind Direction",
        "device_class": "wind_direction",
        "icon": "mdi:compass",
        "state_class": None,
        "unit": "°",
    },
    "wind_speed_avg_last_1_min": {
        "name": "Wind Speed Avg 1 Min",
        "device_class": "wind_speed",
        "icon": "mdi:weather-windy",
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": UnitOfSpeed.MILES_PER_HOUR,
    },
    "wind_dir_scalar_avg_last_1_min": {
        "name": "Wind Dir Scalar Avg 1 Min",
        "device_class": "wind_direction",
        "icon": "mdi:compass",
        "state_class": None,
        "unit": "°",
    },
    "wind_speed_avg_last_2_min": {
        "name": "Wind Speed Avg 2 Min",
        "device_class": "wind_speed",
        "icon": "mdi:weather-windy",
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": UnitOfSpeed.MILES_PER_HOUR,
    },
    "wind_dir_scalar_avg_last_2_min": {
        "name": "Wind Dir Scalar Avg 2 Min",
        "device_class": "wind_direction",
        "icon": "mdi:compass",
        "state_class": None,
        "unit": "°",
    },
    "wind_speed_hi_last_2_min": {
        "name": "Wind Speed Hi 2 Min",
        "device_class": "wind_speed",
        "icon": "mdi:weather-windy",
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": UnitOfSpeed.MILES_PER_HOUR,
    },
    "wind_dir_at_hi_speed_last_2_min": {
        "name": "Wind Dir at Hi Speed 2 Min",
        "device_class": "wind_direction",
        "icon": "mdi:compass",
        "state_class": None,
        "unit": "°",
    },
    "wind_speed_avg_last_10_min": {
        "name": "Wind Speed Avg 10 Min",
        "device_class": "wind_speed",
        "icon": "mdi:weather-windy",
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": UnitOfSpeed.MILES_PER_HOUR,
    },
    "wind_dir_scalar_avg_last_10_min": {
        "name": "Wind Dir Scalar Avg 10 Min",
        "device_class": "wind_direction",
        "icon": "mdi:compass",
        "state_class": None,
        "unit": "°",
    },
    "wind_speed_hi_last_10_min": {
        "name": "Wind Speed Hi 10 Min",
        "device_class": "wind_speed",
        "icon": "mdi:weather-windy",
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": UnitOfSpeed.MILES_PER_HOUR,
    },
    "wind_dir_at_hi_speed_last_10_min": {
        "name": "Wind Dir at Hi Speed 10 Min",
        "device_class": "wind_direction",
        "icon": "mdi:compass",
        "state_class": None,
        "unit": "°",
    },
    "wind_chill": {
        "name": "Wind Chill",
        "device_class": "temperature",
        "icon": "mdi:snowflake",
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": UnitOfTemperature.FAHRENHEIT,
    },
}

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

    # Create a separate device for each condition object
    for cond in conditions:
        # Use a unique device_id for each condition (e.g., lsid or txid)
        device_id = cond.get("lsid") or cond.get("txid") or id(cond)
        for key in SENSOR_TYPES:
            value = cond.get(key)
            if value not in (None, "Unknown", "null"):
                sensors.append(
                    WeatherlinkSensor(coordinator, key, cond, device_id)
                )

    async_add_entities(sensors)


class WeatherlinkSensor(SensorEntity):
    has_entity_name = True

    def __init__(self, coordinator, key, data, device_id=None):
        self.coordinator = coordinator
        self._key = key
        self._data = data
        self._device_id = device_id
        sensor_info = SENSOR_TYPES.get(key, {})
        self._attr_name = sensor_info.get("name", key)
        self._attr_device_class = sensor_info.get("device_class")
        self._attr_icon = sensor_info.get("icon", "mdi:cloud")
        self._attr_state_class = sensor_info.get("state_class")
        self._attr_unit = sensor_info.get("unit")

    @property
    def unique_id(self):
        # Make unique per device/condition
        return f"{self.coordinator._host}_{self._device_id}_{self._key}"

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
        if self.device_class == "precipitation_intensity":
            if self.hass and self.hass.config.units.length_unit == UnitOfLength.MILLIMETERS:
                return f"{UnitOfLength.MILLIMETERS}/h"
            return f"{UnitOfLength.INCHES}/h"
        if self._attr_unit is not None:
            return self._attr_unit
        # fallback logic if needed
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
        # Each condition object gets its own device
        device_id = self._device_id or self.coordinator._host
        name = f"Weatherlink Device {device_id}"
        return {
            "identifiers": {(DOMAIN, device_id)},
            "name": name,
            "manufacturer": "Davis Instruments",
            "model": "Weatherlink Live",
            "sw_version": None,
            "configuration_url": f"http://{self.coordinator._host}/",
        }

    @property
    def native_unit_of_measurement(self):
        if self.device_class == "precipitation":
            # Show mm if HA is metric, else inch
            if self.hass and self.hass.config.units.length_unit == UnitOfLength.MILLIMETERS:
                return UnitOfLength.MILLIMETERS
            return UnitOfLength.INCHES
        if self.device_class == "precipitation_intensity":
            if self.hass and self.hass.config.units.length_unit == UnitOfLength.MILLIMETERS:
                return f"{UnitOfLength.MILLIMETERS}/h"
            return f"{UnitOfLength.INCHES}/h"
        if self.device_class == "temperature":
            return UnitOfTemperature.FAHRENHEIT
        if self.device_class == "humidity":
            return "%"
        if self.device_class == "pressure":
            return UnitOfPressure.INHG
        if self.device_class == "wind_speed":
            return UnitOfSpeed.MILES_PER_HOUR
        if self.device_class in ["pm1", "pm25", "pm10"]:
            return CONCENTRATION_MICROGRAMS_PER_CUBIC_METER
        return None

    @property
    def native_value(self):
        if self._key in self._data:
            # Special handling for all rain count fields
            if self._key in rain_count_keys:
                rain_size = self._data.get("rain_size", 1)
                count = self._data[self._key]
                to_mm = self.hass and self.hass.config.units.length_unit == UnitOfLength.MILLIMETERS
                return calculate_rain_amount(count, rain_size, to_mm)
            # Convert temperature sensors to Celsius
            if self.device_class == "temperature":
                return round(fahrenheit_to_celsius(self._data[self._key]), 1)
            return self._data[self._key]
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


def fahrenheit_to_celsius(f):
    """Convert Fahrenheit to Celsius."""
    if f is None:
        return None
    return (f - 32) * 5.0 / 9.0


def calculate_rain_amount(count, rain_size, to_mm):
    """Calculate rain amount based on count, rain_size, and target unit."""
    if to_mm:
        if rain_size == 1:
            return round(count * 0.254, 2)  # 0.01 inch to mm
        elif rain_size == 2:
            return round(count * 0.2, 2)
        elif rain_size == 3:
            return round(count * 0.1, 2)
        elif rain_size == 4:
            return round(count * 0.0254, 3)  # 0.001 inch to mm
    else:
        if rain_size == 1:
            return round(count * 0.01, 3)
        elif rain_size == 2:
            return round(count * 0.00787, 3)  # 0.2 mm to inch
        elif rain_size == 3:
            return round(count * 0.00394, 3)  # 0.1 mm to inch
        elif rain_size == 4:
            return round(count * 0.001, 3)
    return count
