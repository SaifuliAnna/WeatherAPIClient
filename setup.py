"""Setup module for weather_api_client."""
from setuptools import find_packages, setup

setup(
    name='weather_api_client',
    version='0.2.1',
    author='Ann',
    description=('Weather API client application. This script retrieves and displays the current weather information '
                 'for a given city using the OpenWeatherMap API. '
                 'sage: cli-weather <api_key> <city>'),
    license='MIT',
    long_description_content_type='text/markdown',
    long_description=('Weather API client application for retrieving and displaying the current weather information '
                      'using the [OpenWeatherMap API](https://openweathermap.org/).\n\n'
                      '***\n\n'
                      '## Start\n'
                      '### 1. Installation\n'
                      'install from the site or from the downloaded package\n'
                      '```bash\n'
                      'pip install weather_api_client-<-version->\n'
                      '```\n'
                      '### 2. Start the Weather API client\n'
                      '```bash\n'
                      'cli-weather <api_key> <city>\n'
                      '```\n'
                      'Replace < api_key > with the [OpenWeatherMap API](https://openweathermap.org/) '
                      'key and < city > with the desired city.\n\n'
                      'for example:\n\n'
                      '```bash\n'
                      'cli-weather <api_key> London\n'
                      '```\n\n'
                      '```bash\n'
                      'Current Weather in London:\n'
                      'Temperature: 278.82 K\n'
                      'Temperature: 6 °C\n'
                      'Description: broken clouds\n'
                      'Wind Speed: 2.06 m/s\n'
                      'Humidity: 85%\n'
                      ),
    url='',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'cli-weather = weather_api_client.main:main',
        ],
    },
    include_package_data=True,
)
