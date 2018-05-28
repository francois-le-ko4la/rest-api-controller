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
    """
    Generic exception for apicontroller
    """
    pass


class APIConnectionError(APIError):
    """
    Error: the server is unreachable.
    """
    def __init__(self, host):
        super().__init__("\"{}\" unreachable!".format(host))


class APIHTTPError(APIError):
    """
    Error: bad request.
    """
    def __init__(self, request):
        super().__init__("Request Error : {}.".format(request))


class APIBadHostnameError(APIError):
    """
    Error: hostname is not validated.
    """
    def __init__(self, host):
        super().__init__("\"{}\" is not validated!".format(host))


__all__ = [
    'APIError',
    'APIConnectionError',
    'APIHTTPError',
    'APIBadHostnameError'
]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
