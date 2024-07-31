#!/usr/bin/env python3
"""
Module for unittest to test client.
"""

import unittest
from urllib import response
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
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

    def test_public_repos_url(self):
        """
        Test `_public_repos_url` property to ensure
        it returns the correct URL.
        Uses `patch` as a context manager to mock
        the `org` property of
        `GithubOrgClient` and verify that
        `_public_repos_url` returns the
        correct URL based on the mocked payload.
        """
        # Define the known payload for the mock
        mock_payload = {
            "repos_url": "https://api.github.com/orgs/test_org/repos"
        }

        # Use patch as a context manager to mock the `org` property
        with patch(
                'client.GithubOrgClient.org',
                new_callable=PropertyMock
        ) as mock_org:
            # Set the return value of the mocked `org` property
            mock_org.return_value = mock_payload

            # Create an instance of `GithubOrgClient`
            client = GithubOrgClient("test_org")

            # Access the `_public_repos_url` property
            result = client._public_repos_url

            # Define the expected URL based on the mocked payload
            expected_url = "https://api.github.com/orgs/test_org/repos"

            # Verify that the result matches the expected URL
            self.assertEqual(result, expected_url)


if __name__ == "__main__":
    unittest.main()
