#!/usr/bin/env python3
"""Unittests and integration test on a cliemt python sript"""

import client
import fixtures

import unittest
from unittest.mock import patch, PropertyMock, MagicMock
from parameterized import parameterized, parameterized_class
from typing import Dict
GithubOrgClient = __import__('client').GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test the github client class"""

    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': 'abc'})
    ])
    @patch('client.get_json')
    def test_org(self, org: str, expected: Dict, mocked_func: MagicMock):
        """Test the org method"""
        mocked_func.return_value = expected
        thing = GithubOrgClient(org)
        self.assertEqual(thing.org, expected)
        mocked_func.assert_called_once_with("https://api.github.com/orgs/{}"
                                            .format(org))

    def test_public_repos_url(self):
        """test the public_repos_url method"""
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mock_pu:
            mock_pu.return_value = {'login':
                                    'google',
                                    'repos_url':
                                    'https://api.github.com/orgs/google/repos'}
            thing = GithubOrgClient('google')
            self.assertEqual(thing._public_repos_url,
                             'https://api.github.com/orgs/google/repos')

    @patch('client.get_json')
    def test_public_repos(self, mocked_json: MagicMock):
        """unitesting the client public repos"""
        mocked_json.return_value = [{'name': 'truth', 'id': 1936771},
                                    {'name': 'ruby-openid-apps-discovery',
                                    'id': 3248507},
                                    {'name': 'autoparse', 'id': 3248531},
                                    {'name': 'anvil-build', 'id': 3975462}]
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mocked_func:
            mocked_func.return_value = {'login': "google",
                                        'repos_url': 'https://www.google.com'}
            thing = GithubOrgClient('google')
            res: list = [repo['name'] for repo in mocked_json.return_value]
            self.assertEqual(thing.public_repos(), res)
            mocked_json.assert_called_once()
            mocked_func.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}},
            "my_license", False)
    ])
    def test_has_license(self, repo: Dict, license_key: str, expected: bool):
        """test for the has licesne attribute"""
        self.assertEqual(GithubOrgClient.has_license(repo,
                                                     license_key), expected)
