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

import json
import logging
import requests

class RestAPIController(object):
    """ My REST API Controller
    """
    def __init__(self, *args, **kwargs):
        """Init the class & define args
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
            self._host = kwargs.pop('host')
        else:
            print("Host must be provided...")
            exit()
        self.__result = None

    def __enable_debug(self):
        """Enable Debug
        -> connection log
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
        """
        self.__connected = False
        self.__requested = False
        if args is None:
            args = dict()
        if path is not None:
            path = "{host}{path}".format(host=self._host, path=path)
        if self.__token is not None:
            #args = {**self.token, **args}
            self.__token = {'Authorization':'{} {}'.format(self.__token[0], self.__token[1])}
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
        """
        return self.__result

    def get_item(self, item_key, item_id):
        """Get one value
        """
        return self.__result[item_key][item_id]

    def get_connect_status(self):
        """Get connection status
        """
        return self.__connected

    def get_request_status(self):
        """Get request status
        """
        return self.__requested
