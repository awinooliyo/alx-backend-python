#!/usr/bin/env python3
"""
Module for parameterized unit test.
"""


import unittest
from parameterized import parameterized
from utils import access_nested_map


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


if __name__ == "__main__":
    unittest.main()
