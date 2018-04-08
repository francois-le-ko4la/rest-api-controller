#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rest_api_controller.rest_api_controller import RestAPIController

print("test 1")
my_api = RestAPIController(host="http://pi.open-notify.org", debug=True)
print(my_api.request("GET", "/iss-now.json"))
print("test 2")
my_api = RestAPIController(host="http://api.open-notify.org", debug=True)
print(my_api.request("GET", "/iss-now.json"))
