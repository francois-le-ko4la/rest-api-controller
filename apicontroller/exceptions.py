#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

 ######  #####   #####    ####   #####
 #       #    #  #    #  #    #  #    #
 #####   #    #  #    #  #    #  #    #
 #       #####   #####   #    #  #####
 #       #   #   #   #   #    #  #   #
 ######  #    #  #    #   ####   #    #

"""


class APIError(Exception):
    """Generic exception for apicontroller"""
    def __init__(self, msg):
        super(APIError, self).__init__(msg)


class APIConnectionError(APIError):
    def __init__(self, original_exception):
        super(APIError, self).__init__("Unable to connect")
        self.original_exception = original_exception


class APIHTTPError(APIError):
    def __init__(self, original_exception):
        super(APIHTTPError, self).__init__("Client Error")
        self.original_exception = original_exception


if __name__ == "__main__":
    import doctest
    doctest.testmod()
