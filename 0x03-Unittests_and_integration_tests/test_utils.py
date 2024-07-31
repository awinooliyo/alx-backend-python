#!/usr/bin/env python3
"""
Module for parameterized unit test.
"""


import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json


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
    def test_get_json(self, test_url, test_payload):
        """
        Test get_json function to ensure it returns the expected result.
        """
        class Mocked(Mock):
            """
            Class that inherits from Mock.
            """
            def json(self):
                """
                JSON returning a payload.
                """
                return payload

        with patch('requests.get') as MockClass:
            MockClass.return_value = Mocked()
            self.assertEqual(get_json(url), payload)


if __name__ == "__main__":
    unittest.main()
