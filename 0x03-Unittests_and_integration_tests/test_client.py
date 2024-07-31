#!/usr/bin/env python3
"""
Module for unittest to test the client.
"""
import unittest
from unittest.mock import patch, Mock, PropertyMock, MagicMock
from parameterized import parameterized
from typing import Dict
from client import GithubOrgClient
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """
    Test case for the `GithubOrgClient` class.
    """

    @parameterized.expand([
        ('google', {'login': 'google'}),
        ('abc', {'login': 'abc'}),
    ])
    @patch('client.get_json')
    def test_org(
        self,
        org: str,
        expected_resp: Dict,
        mock_get_json: MagicMock
    ) -> None:
        """
        Test `GithubOrgClient.org` to ensure it returns the correct value.

        Args:
            org (str): The organization name to test.
            expected_resp (Dict): The expected response from `get_json`.
            mock_get_json (MagicMock): Mocked `get_json` function.
        """
        # Mock `get_json` to return a predefined response
        mock_get_json.return_value = expected_resp

        # Create a `GithubOrgClient` instance
        client = GithubOrgClient(org)

        # Access the `org` property to trigger the `get_json` call
        result = client.org

        # Verify that `get_json` was called once with the expected argument
        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org}'
        )

        # Verify the result is as expected
        self.assertEqual(result, expected_resp)

    def test_public_repos_url(self) -> None:
        """
        Test `_public_repos_url` property to ensure it returns the correct URL.

        Uses `patch` as a context manager to mock the `org` property of
        `GithubOrgClient` and verify that `_public_repos_url` returns the
        correct URL based on the mocked payload.
        """
        # Define the known payload for the mock
        mock_payload = {
            'repos_url': 'https://api.github.com/orgs/test_org/repos'
        }

        # Use patch as a context manager to mock the `org` property
        with patch(
            'client.GithubOrgClient.org',
            new_callable=PropertyMock
        ) as mock_org:
            # Set the return value of the mocked `org` property
            mock_org.return_value = mock_payload

            # Create an instance of `GithubOrgClient`
            client = GithubOrgClient('test_org')

            # Access the `_public_repos_url` property
            result = client._public_repos_url

            # Define the expected URL based on the mocked payload
            expected_url = 'https://api.github.com/orgs/test_org/repos'

            # Verify that the result matches the expected URL
            self.assertEqual(result, expected_url)

    @patch('client.get_json')
    @patch(
        'client.GithubOrgClient._public_repos_url',
        new_callable=PropertyMock
    )
    def test_public_repos(
        self,
        mock_public_repos_url: PropertyMock,
        mock_get_json: MagicMock
    ) -> None:
        """
        Test `GithubOrgClient.public_repos` method to ensure it returns the
        correct list of repositories based on the mocked `_public_repos_url`
        and `get_json`.
        """
        # Define the mock payload and URL
        mock_payload = [
            {'name': 'repo1'},
            {'name': 'repo2'},
            {'name': 'repo3'}
        ]
        mock_url = 'https://api.github.com/orgs/test_org/repos'

        # Set up mocks
        mock_public_repos_url.return_value = mock_url
        mock_get_json.return_value = mock_payload

        # Create an instance of `GithubOrgClient`
        client = GithubOrgClient('test_org')

        # Call the `public_repos` method
        repos = client.public_repos()

        # Define the expected result
        expected_repos = ['repo1', 'repo2', 'repo3']

        # Assert that the result is as expected
        self.assertEqual(repos, expected_repos)

        # Assert that the mocked property and method were called once
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with(mock_url)

    @parameterized.expand([
        ({'license': {'key': 'bsd-3-clause'}}, 'bsd-3-clause', True),
        ({'license': {'key': 'bsl-1.0'}}, 'bsd-3-clause', False),
    ])
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """
        Test `GithubOrgClient.has_license` method to ensure it returns
        the correct boolean value indicating if a license key is present.

        Args:
            repo (Dict): The repository data containing license information.
            key (str): The license key to check.
            expected (bool): The expected result of the license check.
        """
        gh_org_client = GithubOrgClient('google')
        client_has_license = gh_org_client.has_license(repo, key)
        self.assertEqual(client_has_license, expected)


if __name__ == '__main__':
    unittest.main()
