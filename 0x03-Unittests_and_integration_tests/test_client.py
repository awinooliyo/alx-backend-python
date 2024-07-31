#!/usr/bin/env python
"""
Module for unittest to test client.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """
    Test case for the `GithubOrgClient` class.
    """

    @parameterized.expand([
        ('google',),
        ('abc',),
    ])
    @patch('client.get_json')
    def test_org(self, org, mock_get_json):
        """
        Test `GithubOrgClient.org` to ensure it returns the correct value.

        Args:
            org (str): The organization name to test.
            mock_get_json (MagicMock): Mocked `get_json` function.
        """
        # Mock `get_json` to return a predefined response
        mock_get_json.return_value = {"org": org}

        # Create a `GithubOrgClient` instance
        client = GithubOrgClient(org)

        # Access the `org` property to trigger the `get_json` call
        result = client.org

        # Verify that `get_json` was called once with the expected argument
        mock_get_json.assert_called_once_with(
                f'https://api.github.com/orgs/{org}'
        )

        # Verify the result is as expected
        self.assertEqual(result, {"org": org})


if __name__ == "__main__":
    unittest.main()
