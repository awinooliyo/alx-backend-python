#!/usr/bin/env python3
"""Module for parameterized unit tests.

This module contains unit tests for functions and decorators in the `utils`
module. The tests include:
- Accessing nested maps.
- Fetching JSON data from URLs.
- Caching results using the memoize decorator.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from typing import Dict, Tuple, Union
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test case for the `access_nested_map` function.

    This class tests the behavior of the `access_nested_map` function to
    ensure it correctly traverses nested dictionaries and handles errors
    appropriately.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self,
        nested_map: Dict,
        path: Tuple[str],
        expected: Union[Dict, int]
    ) -> None:
        """Test `access_nested_map` function for correct output.

        Args:
            nested_map (Dict): The nested dictionary to traverse.
            path (Tuple[str]): A tuple of keys to access the nested value.
            expected (Union[Dict, int]): The expected value after traversal.

        Asserts:
            The function output is compared with the expected value.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
        self,
        nested_map: Dict,
        path: Tuple[str],
        exception: Exception
    ) -> None:
        """Test `access_nested_map` function for handling exceptions.

        Args:
            nested_map (Dict): The nested dictionary to traverse.
            path (Tuple[str]): A tuple of keys to access the nested value.
            exception (Exception): The expected exception type.

        Asserts:
            The function raises the expected exception for invalid inputs.
        """
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test case for the `get_json` function.

    This class tests the `get_json` function to ensure it correctly fetches
    JSON data from a URL and handles mock responses properly.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
        self,
        test_url: str,
        test_payload: Dict
    ) -> None:
        """Test `get_json` function for correct output.

        Args:
            test_url (str): The URL to request data from.
            test_payload (Dict): The expected JSON payload
            returned by `get_json`.

        Asserts:
            The function output matches the expected payload and
            `requests.get` is called with the correct URL.
        """
        attrs = {'json.return_value': test_payload}
        with patch(
            'utils.requests.get',
            return_value=Mock(**attrs)
        ) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Test case for the `memoize` decorator.

    This class tests the `memoize` decorator to ensure it caches results and
    avoids redundant computations for the same input.
    """

    def test_memoize(self) -> None:
        """Test `memoize` decorator for caching results.

        This method creates an instance of `TestClass` with a method `a_method`
        that returns a fixed value. The `a_property` method, decorated with
        `memoize`, is tested to ensure `a_method` is called only once and that
        `a_property` returns the cached result on subsequent calls.
        """

        class TestClass:
            """Class to test `memoize` decorator.

            This class contains a method `a_method` that returns a fixed value,
            and a property `a_property` that is decorated with `memoize` to
            cache the result of `a_method`.
            """
            def a_method(self):
                """Method returning a fixed value.

                Returns:
                    int: The fixed value of 42.
                """
                return 42

            @memoize
            def a_property(self):
                """Memoized property returning the result of `a_method`.

                Returns:
                    int: The result of `a_method`, which is 42.
                """
                return self.a_method()

        # Create an instance of TestClass
        instance = TestClass()
        # Patch the instance method `a_method`
        with patch.object(instance, 'a_method') as mock_method:
            # Access the memoized property twice
            instance.a_property
            instance.a_property
            # Ensure that `a_method` was called only once
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
