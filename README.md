# My API Client

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.11-brightgreen.svg)](https://www.python.org/downloads/release)
[![Test PyPI](https://img.shields.io/badge/test--pypi-v0.1.0-blue)](https://test.pypi.org/project/weather-api-client/)

Weather API client application for retrieving and displaying the current weather information using the 
[OpenWeatherMap API](https://openweathermap.org/).

***

## Start
### 1. Installation
install from the site or from the downloaded package

`pip install weather_api_client-<-version->` 

[weather_api_client on test.pypi.org](https://test.pypi.org/project/weather-api-client/)

[weather_api_client on github.com](https://github.com/SaifuliAnna/My_API_Client/blob/main/dist)


### 2. Start the Weather API client
`cli-weather <api_key> <city>`

Replace < api_key > with the [OpenWeatherMap API](https://openweathermap.org/) key and < city > with the desired city.

***

## API Client
### APIClientWeather 

The APIClientWeather class is responsible for processing API requests.

example of the use:
```
from weather_api_client.client import APIClientWeather

api_client = APIClientWeather(api_key='your_api_key')
weather_data = api_client.get_current_weather(city_name='example_city')
print(weather_data)
```

## Main program
The `main.py` script serves as the Weather API client program.

Usage:
```
python main.py <api_key> <city>
```
Replace < api_key > with the [OpenWeatherMap API](https://openweathermap.org/) key and < city > with the desired city.

for example:

`python main.py <api_key> London`

```
Current Weather in London:
Temperature: 278.82 K
Temperature: 6 °C
Description: broken clouds
Wind Speed: 2.06 m/s
Humidity: 85%
```

