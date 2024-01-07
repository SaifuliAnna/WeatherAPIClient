"""Weather API client application.

This script retrieves and displays the current weather information
for a given city using the OpenWeatherMap API.

Usage:
    python main.py <api_key> <city>
"""

import argparse

# for code
from client import APIClientWeather
from service import APIServiceWeather

# for setup.py
# from weather_api_client.client import APIClientWeather
# from weather_api_client.service import APIServiceWeather


def main():
    parser = argparse.ArgumentParser(description='Weather API Client')
    parser.add_argument('api_key', help='Your OpenWeatherMap API Key')
    parser.add_argument('city', help='City for weather information')
    args = parser.parse_args()

    api_key = args.api_key
    city = args.city

    api_client = APIClientWeather(api_key)
    api_service = APIServiceWeather()

    current_weather = api_client.get_current_weather(city)

    if current_weather:
        api_service.save_result(city, current_weather)

        weather_summary = api_service.analyze_weather(current_weather)
        print(f"Current Weather in {city}:\n{weather_summary}")
    else:
        print(f"No weather information available for {city}.\n")


if __name__ == '__main__':
    main()
