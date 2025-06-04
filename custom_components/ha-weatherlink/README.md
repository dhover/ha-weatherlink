# Weatherlink Custom Integration

This is a custom integration for the Davis Weatherlink Live device, designed to work with Home Assistant. This integration allows users to monitor and interact with their Weatherlink Live device, providing access to various weather data points.

## Installation

1. Clone this repository to your Home Assistant `custom_components` directory:
   ```
   git clone https://github.com/yourusername/ha-weatherlink.git
   ```

2. Ensure that the `ha-weatherlink` directory is located in the `custom_components` folder of your Home Assistant configuration.

3. Install the required dependencies listed in `requirements.txt`:
   ```
   pip install -r requirements.txt
   ```

## Configuration

To set up the Weatherlink integration, add the following configuration to your `configuration.yaml` file:

```yaml
weatherlink:
  username: YOUR_USERNAME
  password: YOUR_PASSWORD
```

Replace `YOUR_USERNAME` and `YOUR_PASSWORD` with your Weatherlink Live account credentials.

## Usage

Once the integration is set up, you will be able to access various sensor entities representing the data from your Weatherlink Live device. These entities can be used in automations, scripts, and the Home Assistant dashboard.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. Any contributions, bug reports, or feature requests are welcome!

## License

This project is licensed under the MIT License. See the LICENSE file for more details.