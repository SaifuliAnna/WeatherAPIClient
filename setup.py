from setuptools import find_packages, setup

VERSION = '0.2.4'

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='weather_api_client',
    version=VERSION,
    author='Ann',
    description='Weather API client application.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/SaifuliAnna/WeatherAPIClient',
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
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        "Source": "https://github.com/SaifuliAnna/WeatherAPIClient",
    },
    python_requires=">=3.11",
)
