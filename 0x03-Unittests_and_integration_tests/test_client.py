#!/usr/bin/env python3
"""
Module for unittest to test the client.
"""
import unittest
from unittest.mock import patch, Mock, PropertyMock, MagicMock
from parameterized import parameterized, parameterized_class
from typing import Dict
from requests import HTTPError
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    Test case for the `GithubOrgClient` class.
    """

    @parameterized.expand([
        ('google', {'login': 'google'}),
        ('abc', {'login': 'abc'}),
    ])
    @patch('client.get_json')
    def test_org(self, org: str, expected_resp: Dict,
                 mock_get_json: MagicMock) -> None:
        """
        Test `GithubOrgClient.org` to ensure it returns the correct value.

        Args:
            org (str): The organization name to test.
            expected_resp (Dict): The expected response from `get_json`.
            mock_get_json (MagicMock): Mocked `get_json` function.
        """
        mock_get_json.return_value = expected_resp
        client = GithubOrgClient(org)
        result = client.org
        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org}'
        )
        self.assertEqual(result, expected_resp)

    def test_public_repos_url(self) -> None:
        """
        Test `_public_repos_url` property to ensure it returns the correct URL.

        Uses `patch` as a context manager to mock the `org` property of
        `GithubOrgClient` and verify that `_public_repos_url` returns the
        correct URL based on the mocked payload.
        """
        mock_payload = {
            'repos_url': 'https://api.github.com/orgs/test_org/repos'
        }
        with patch(
            'client.GithubOrgClient.org',
            new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = mock_payload
            client = GithubOrgClient('test_org')
            result = client._public_repos_url
            expected_url = 'https://api.github.com/orgs/test_org/repos'
            self.assertEqual(result, expected_url)

    @patch('client.get_json')
    @patch(
        'client.GithubOrgClient._public_repos_url',
        new_callable=PropertyMock
    )
    def test_public_repos(self, mock_public_repos_url: PropertyMock,
                          mock_get_json: MagicMock) -> None:
        """
        Test `GithubOrgClient.public_repos` method to ensure it returns the
        correct list of repositories based on the mocked `_public_repos_url`
        and `get_json`.
        """
        mock_payload = [
            {'name': 'repo1'},
            {'name': 'repo2'},
            {'name': 'repo3'}
        ]
        mock_url = 'https://api.github.com/orgs/test_org/repos'
        mock_public_repos_url.return_value = mock_url
        mock_get_json.return_value = mock_payload
        client = GithubOrgClient('test_org')
        repos = client.public_repos()
        expected_repos = ['repo1', 'repo2', 'repo3']
        self.assertEqual(repos, expected_repos)
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with(mock_url)

    @parameterized.expand([
        ({'license': {'key': 'bsd-3-clause'}}, 'bsd-3-clause', True),
        ({'license': {'key': 'bsl-1.0'}}, 'bsd-3-clause', False),
    ])
    def test_has_license(self, repo: Dict, key: str,
                         expected: bool) -> None:
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


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Performs integration tests for the `GithubOrgClient` class.
    """
    @classmethod
    def setUpClass(cls) -> None:
        """
        Sets up class fixtures before running tests.
        """
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """
        Tests the `public_repos` method.
        """
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        """
        Tests the `public_repos` method with a license.
        """
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """
        Removes the class fixtures after running all tests.
        """
        cls.get_patcher.stop()


if __name__ == '__main__':
    unittest.main()
