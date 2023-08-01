#!/usr/bin/env python3
"""Unittests and untegration tests"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock, MagicMock
import requests
from typing import Dict, Tuple, Union

access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json
memoize = __import__('utils').memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test class for the utils.access_nested map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Dict, path: Tuple,
                               expected: MagicMock) -> None:
        """A function testimg the return values"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Dict,
                                         path: Tuple) -> None:
        """Test for exception"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """Test the get json"""
        method = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**method)) as mock_method:
            self.assertEqual(get_json(test_url), test_payload)
            mock_method.assert_called_once_with(test_url)

    def test_memoize(self) -> Union[int, callable]:
        """Test the memoize function in utils"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_met:
            thing = TestClass()
            self.assertEqual(thing.a_property, 42)
            self.assertEqual(thing.a_property, 42)
            mock_met.assert_called_once()
