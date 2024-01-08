"""Module for MyAPIService."""
from typing import Any, Dict, Optional


class APIServiceWeather(object):
    """Class for handling API services."""

    def __init__(self) -> None:
        """Initialize the MyAPIService."""
        self.result_dict: Dict[str, Any] = {}

    def save_result(self, key: str, result_data: Any) -> None:
        """
        Save result in MyAPIService.

        :param key: str: Identify the result
        :param result_data: Any: Save the result of a function in the results dictionary
        :return: None
        """
        self.result_dict[key] = result_data
        print(f'Result saved: {key} - {result_data}')

    def get_result(self, key: str) -> Optional[Any]:
        """
        Get result from MyAPIService.

        :param key: str: Identify the result
        :return: Any or None
        """
        return self.result_dict.get(key, None)

    def update_result(self, key: str, result_data: Any) -> None:
        """
        Update result in MyAPIService.

        :param key: str: Identify the result
        :param result_data: Any: Updated result data
        :return: None
        """
        if key in self.result_dict:
            self.result_dict[key] = result_data
            print(f'Result updated: {key} - {result_data}')

    def delete_result(self, key: str) -> None:
        """
        Delete result from MyAPIService.

        :param key: str: Identify the result to delete
        :return: None
        """
        if key in self.result_dict:
            self.result_dict.pop(key)
            print(f'Result deleted: {key}')

