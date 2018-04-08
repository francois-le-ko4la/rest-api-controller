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
    def test_badurl(self):
        my_api = RestAPIController(host="http://zefzkekjflze.fzerjf")
        self.assertFalse(my_api.isconnected())
    
    def test_request(self):
        my_api = RestAPIController(host="http://api.open-notify.org")
        self.assertTrue(my_api.request("GET", "/iss-now.json") is not None)

if __name__ == '__main__':
    """If main...
    """
    unittest.main()
