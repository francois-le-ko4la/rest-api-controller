#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""
This script is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3 of the License, or (at your option) any later version.

This script is provided in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
"""

from apicontroller.controller import RestAPIController


print("test 1")
my_api = RestAPIController(host="http://pi.open-notify.org", debug=True)
print(my_api.request("GET", "/iss-now.json"))
print("test 2")
my_api = RestAPIController(host="http://api.open-notify.org", debug=True)
print(my_api.request("GET", "/iss-now.json"))
