#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3 of the License, or (at your option) any later version.

This script is provided in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
"""
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
from rest_api_controller.rest_api_controller import RestAPIController


class TestRestAPIController(unittest.TestCase):

    """Unittest Class
    """

    def test_rest_api(self):
        """Global test
        """
        my_api = RestAPIController(host="http://api.open-notify.org")
        self.assertTrue(my_api.request("GET", "/iss-now.json"))

    def test_connection(self):
        """Assert connection
        """
        my_api = RestAPIController(host="http://api.open-notify.org")
        my_api.request("GET", "/iss-now.json")
        self.assertTrue(my_api.get_connect_status())

    def test_request(self):
        """Assert request
        """
        my_api = RestAPIController(host="http://api.open-notify.org")
        my_api.request("GET", "/iss-now.json")
        self.assertTrue(my_api.get_request_status())


if __name__ == '__main__':
    """If main...
    """
    print(sys.path)
    unittest.main()
