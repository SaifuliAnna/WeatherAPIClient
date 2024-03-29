"""Module for MyAPIClient."""
from typing import Any, Dict

import requests

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
API_KEY_PARAM = 'appid'


class APIClientWeather(object):
    """Class for handling API requests."""

    def __init__(self, api_key: str) -> None:
        """Initialize the MyAPIClient."""
        self.api_key = api_key
        self.base_url = BASE_URL

    def get_current_weather(self, city_name: str) -> Dict[str, Any]:
        """
        Get the current weather for a city.

        :param city_name: str: Specify the city name to get weather data for
        :return: A dictionary with the weather information
        """
        request_params = {'q': city_name, API_KEY_PARAM: self.api_key}

        try:
            response = requests.get(self.base_url, params=request_params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            print(f'Error fetching weather data for {city_name}.\nTry another name, please...')
            return {}
