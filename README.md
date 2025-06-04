# ha-weatherlink

This project is a custom integration for the Davis Weatherlink Live device, designed to work with Home Assistant. It allows users to monitor and interact with weather data collected by the Weatherlink Live device.

## Features

- Real-time weather data monitoring
- Sensor entities for various weather parameters
- Easy configuration and setup

## Installation

1. Clone this repository to your Home Assistant `custom_components` directory:
   ```
   git clone https://github.com/yourusername/ha-weatherlink.git
   ```

2. Ensure that the `weatherlink` directory is located in the `custom_components` folder of your Home Assistant installation.

3. Install the required dependencies listed in `requirements.txt`:
   ```
   pip install -r requirements.txt
   ```

## Configuration

To set up the Weatherlink integration, add the following to your `configuration.yaml` file:

```yaml
weatherlink:
  username: YOUR_USERNAME
  password: YOUR_PASSWORD
```

Replace `YOUR_USERNAME` and `YOUR_PASSWORD` with your Weatherlink Live account credentials.

## Usage

Once the integration is set up, you will be able to see various sensor entities in your Home Assistant dashboard. These sensors will provide real-time updates on weather conditions.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.