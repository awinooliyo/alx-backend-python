#!/usr/bin/env python3
"""
Module for parameterized unit test.
"""


import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from typing import Dict
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Class that inherits from unittest.TestCase
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Method to test if the method returns what it is supposed to.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test access_nested_map function for invalid inputs
        that should raise a KeyError.

        Args:
            nested_map (dict): The nested dictionary to access.
            path (tuple): Sequence of keys to traverse the dictionary.
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), repr(path[-1]))


class TestGetJson(unittest.TestCase):
    """
    TestCase class for the get_json function from the utils module.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """
        Test get_json function to ensure it returns the expected result.

        Args:
            test_url (str): The URL to pass to get_json.
            test_payload (dict): The expected
                        JSON payload returned by get_json.
        """
        # Set up the mock to return the test_payload
        attrs = {'json.return_value': test_payload}
        with patch('utils.requests.get',
                   return_value=Mock(**attrs)) as req_get:
            # Call the function with the test URL
            result = get_json(test_url)
            # Check that requests.get was called
            # exactly once with the test_url
            req_get.assert_called_once_with(test_url)
            # Check that the function
            # returned the expected payload
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    TestCase class for the `memoize` decorator from the `utils` module.

    This class tests the `memoize` decorator to ensure it caches results
    correctly, so a decorated method is called only once with the same
    parameters and returns the cached result on subsequent calls.
    """

    def test_memoize(self):
        """
        Test the `memoize` decorator to ensure it caches results.

        This method creates an instance of `TestClass` with a method
        `a_method` that returns a fixed value. The `a_property` method,
        decorated with `memoize`, is tested to ensure `a_method` is
        called only once, and that `a_property` returns the cached result.
        """
        class TestClass:
            """
            Class to test memoization.

            This class has a method `a_method` that returns a fixed value,
            and a memoized property `a_property` that calls `a_method`.
            """
            def a_method(self):
                """
                Method that returns a fixed value of 42.

                Returns:
                    int: The value 42.
                """
                return 42

            @memoize
            def a_property(self):
                """
                Memoized property that calls `a_method` and returns its result.

                Returns:
                    int: The result of `a_method`, which is 42.
                """
                return self.a_method()

        # Create an instance of TestClass
        instance = TestClass()

        # Patch the instance method `a_method`
        with patch.object(
            instance, 'a_method', return_value=42
        ) as mock_method:
            # Access the memoized property twice
            result1 = instance.a_property()
            result2 = instance.a_property()

            # Assert that the result is as expected
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # Ensure that `a_method` was called only once
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
