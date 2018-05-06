#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

  ####    ####   #    #   #####  #####    ####   #       #       ######  #####
 #    #  #    #  ##   #     #    #    #  #    #  #       #       #       #    #
 #       #    #  # #  #     #    #    #  #    #  #       #       #####   #    #
 #       #    #  #  # #     #    #####   #    #  #       #       #       #####
 #    #  #    #  #   ##     #    #   #   #    #  #       #       #       #   #
  ####    ####   #    #     #    #    #   ####   ######  ######  ######  #    #

"""
import json
import logging
from functools import wraps
import requests


class RestAPIController(object):

    """ My REST API Controller

    Use:
        >>> my_api = RestAPIController(host="http://pi.open-notify.org")
        >>> print(my_api.request("GET", "/iss-now.json"))
        Traceback (most recent call last):
        ...
        OSError: Host unreachable
        >>> my_api = RestAPIController(host="http://api.open-notify.org")
        >>> result = my_api.request("GET", "/iss-now.json")
        >>> print(result['message'])
        success
    """

    def __init__(self, host, auth=None, token=None, debug=False):
        """Init the RestAPIController Class
        This function define attributes.

        Args:
            host (string)
            auth (dict)
            token (dict)
            debug (bool)

        Attributes:
            self.__host (string)
            self.__auth (dict)
            self.__token (dict)
            self.__debug (bool)

        Returns:
            obj

        """
        self.__auth = auth
        self.__debug = debug
        self.__host = host
        self.__token = None
        if token is not None:
            self.__token = {'Authorization': '{} {}'.format(token[0],
                                                            token[1])}

    def __isconnected(func, timeout=5):
        """Test network connection

        Args:
            func: decorated function
            timeout (int): timeout with a default value.

        Returns:
            link up: func(self, *args, **kwargs)
            link down: None

        """
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            """ wrapper """
            try:
                requests.get(self.__host, timeout=timeout)
                return func(self, *args, **kwargs)
            except OSError:
                raise OSError("Host unreachable")
        return wrapper

    @__isconnected
    def isconnected(self):
        """
        Provide a link status between this script & REST API server
        This function is decorated by @__isconnected.
        If the link is down, then decorator will change the value.

        Args:
            None

        Returns:
            True

        """
        return True

    def __enable_debug(func):
        """
        Enable Debug
        -> connection log

        Args:
            func: decorated function

        Returns:
            func(self, *args, **kwargs)

        """
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            """ wrapper """
            if self.__debug:
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
            return func(self, *args, **kwargs)
        return wrapper

    def __loadjson(func):
        """
        Decorator - take the content from REST API server and provide a JSON

        Args:
            func: decorated function

        Returns:
            json

        """
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            """ wrapper """
            content = func(self, *args, **kwargs)
            if content is None:
                return None
            try:
                result = json.loads(content)
            except ValueError:
                return None
            return result
        return wrapper

    def __sendrequest(func):
        """
        Decorator - Use requests.request and arguments from request()

        Args:
            func: decorated function

        Returns:
            str: The return value (answer).
            Content for success, None otherwise.

        """

        @wraps(func)
        def wrapper(self, *args, **kwargs):
            """ wrapper """
            args = func(self, *args, **kwargs)
            if args is None:
                return None
            response = requests.request(**args)
            try:
                response.raise_for_status()
                result = response.content
            except requests.exceptions.HTTPError as error:
                print("Error: " + str(error))
            return result
        return wrapper

    @__loadjson
    @__sendrequest
    @__isconnected
    @__enable_debug
    def request(self, cur_method, cur_path, cur_args=None):
        """
        Provide all arguments to request.
        This function is decorated by __enable_debug,
        __isconnected, __sendrequest, and __loadjson

        Args:
            cur_method (str): "GET", "PUT" ...
            cur_path (str): url = host+path
            cur_args (dict): HTTP args

        Returns:
            dict(): request's args send to decorators

        """

        my_request = {'method': cur_method,
                      'url': "{host}{path}".format(host=self.__host,
                                                   path=cur_path)}

        if cur_args is not None:
            my_request['params'] = cur_args
        if self.__auth is not None:
            my_request['auth'] = self.__auth
        if self.__token is not None:
            my_request['headers'] = self.__token

        return my_request
