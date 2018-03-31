#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# rest-api-controller
## Description:
rest-api-controller is a Python package to manage REST API requests.
We provide examples to use it.

The following files comprise the rest-api-controller package:
* LICENSE: The license file. rest-api-controller is released under the terms of
  the GNU General Public License (GPL), version 3.
* README.md: This readme file.
* setup.py: The setuptools setup file. See above for installation instructions
* test_rest_api_controller.py : Test

The package contents itself are in the rest-api-controller directory:
* __ init __.py: Initialization file for the Python package.

## Setup:

    git clone https://github.com/francois-le-ko4la/rest-api-controller.git
    cd rest-api-controller
    sudo ./setup.py install

## Test:

    ./setup.py test

## How to use this Class:

* Import the package

    from rest_api_controller import RestAPIController

* API wo authentication
```python
    import time
    my_api = RestAPIController(host="http://api.open-notify.org",
        DEBUG=True)
    my_api.request("GET", "/iss-now.json")
    obj=my_api.get()
    print(obj)
    print(time.ctime(int(obj['timestamp'])))
    print(obj['iss_position']['longitude'] + ", " +
        obj['iss_position']['latitude'])
```

* API OAuth1 (username / token) - GITHUB
```python
    my_github_api = RestAPIController(
        host = "https://api.github.com",
        auth = ("*** USERNAME ***", "*** TOKEN ***"),
        DEBUG= True
        )
    my_github_api.request("GET", "/user")
    print(my_github_api.get())
```

* OAuth Token - Facebook
```python
    my_fb_api = RestAPIController(
        token=("OAuth", "*** TOKEN ***"),
        #host = "http://httpbin.org/status/404"
        host = "https://graph.facebook.com",
        DEBUG = True
        )

    my_fb_api.request("GET", "/v2.12/me/taggable_friends",
         {'fields':'id, name, picture.width(500).height(500).type(large)',
         'limit':'5000'})
    friendsList = my_fb_api.get()
```
## Note:

This script is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3 of the License, or (at your option) any later version.

This script is provided in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
"""

import json
import logging
import requests


class RestAPIController(object):

    """ My REST API Controller
    """

    def __init__(self, *args, **kwargs):
        """Init the RestAPIController Class
        This function define attributes.

        Args:
            *arg/**kwargs
                auth(dict)
                token(dict)
                host(string)
                DEBUG(bool)

        Attributes:
            self.__connected(bool)
            self.__requested(bool)
            self.__auth(dict)
            self.__token(dict)
            self.__debug(bool)
            self.__host(string)
            self.__result(dict)

        Returns:
            obj

        """
        self.__connected = None
        self.__requested = None
        if 'auth' in kwargs:
            self.__auth = kwargs.pop('auth')
        else:
            self.__auth = None

        if 'token' in kwargs:
            self.__token = kwargs.pop('token')
        else:
            self.__token = None

        if 'DEBUG' in kwargs:
            self.__debug = kwargs.pop('DEBUG')
            if self.__debug:
                self.__enable_debug()
                print("******* DEBUG")
        if 'host' in kwargs:
            self.__host = kwargs.pop('host')
        else:
            print("Host must be provided...")
            exit()
        self.__result = None

    def __enable_debug(self):
        """Enable Debug
        -> connection log

        Args:
            None

        Returns:
            None

        """
        try:
            import http.client as http_client
        except ImportError:
            import httplib as http_client
        http_client.HTTPConnection.debuglevel = 1

        logging.basicConfig()
        logging.getLogger().setLevel(logging.DEBUG)
        requests_log = logging.getLogger("requests.packages.urllib3")
        requests_log.setLevel(logging.DEBUG)
        requests_log.propagate = True

    def request(self, method=None, path=None, args=None):
        """API Request

        Args:
            method(str): "GET", "PUT" ...
            path(str): url = host+path
            args(dict): HTTP args

        Returns:
            True if successful, False otherwise.

        """
        self.__connected = False
        self.__requested = False

        if args is None:
            args = dict()

        if path is not None:
            path = "{host}{path}".format(host=self.__host, path=path)

        if self.__token is not None:
            self.__token = {'Authorization': '{} {}'.format(self.__token[0],
                                                            self.__token[1])}

        if method is None:
            method = 'GET'

        response = requests.request(
            method or "GET",
            path or "",
            params=args,
            headers=self.__token,
            auth=self.__auth)

        try:
            response.raise_for_status()
            self.__connected = True
        except requests.exceptions.HTTPError as error:
            # Whoops it wasn't a 200
            print("Error: " + str(error))
            return False
        try:
            self.__result = json.loads(response.content)
            self.__requested = True
        except ValueError:
            return False
        return True

    def get(self):
        """Get All values

        Args:
            None

        Returns:
            self.__result(dict): REST API response

        """
        return self.__result

    def get_item(self, item_key, item_id):
        """Get one value
        """
        return self.__result[item_key][item_id]

    def get_connect_status(self):
        """Get connection status

        Args:
            None

        Returns:
            self.__connected(bool)

        """
        return self.__connected

    def get_request_status(self):
        """Get request status

        Args:
            None

        Returns:
            self.__requested

        """
        return self.__requested
