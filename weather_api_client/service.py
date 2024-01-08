"""Module for MyAPIService."""
import logging
from typing import Any, Dict, Optional


class APIServiceWeather(object):
    """Class for handling API services."""

    def __init__(self) -> None:
        """Initialize the MyAPIService."""
        self.results: Dict[str, Any] = {}

    def save_result(self, key: str, data: Any) -> None:
        """
        Save result in MyAPIService.

        :param key: str: Identify the result
        :param data: Any: Save the result of a function in the results dictionary
        :return: None
        """
        self.results[key] = data
        logging.info(f'Result saved: {key} - {data}')

    def get_result(self, key: str) -> Optional[Any]:
        """
        Get result from MyAPIService.

        :param key: str: Identify the result
        :return: Any or None
        """
        return self.results.get(key)

    def update_result(self, key: str, data: Any) -> None:
        """
        Update result in MyAPIService.

        :param key: str: Identify the result
        :param data: Any: Updated result data
        :return: None
        """
        if key in self.results:
            self.results[key] = data
            logging.info(f'Result updated: {key} - {data}')

    def delete_result(self, key: str) -> None:
        """
        Delete result from MyAPIService.

        :param key: str: Identify the result to delete
        :return: None
        """
        if key in self.results:
            del self.results[key]
            logging.info(f'Result deleted: {key}')
