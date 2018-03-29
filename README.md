# rest-api-controller
## Description:
rest-api-controller is a Python package to manage REST API requests.
We provide examples to use it.

The following files comprise the rest-api-controller package:
* LICENSE: The license file. rest-api-controller is released under the terms of
  the GNU General Public License (GPL), version 3.
* README.rst: This readme file.
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

## Dev docstring
### Class RestAPIController:
My REST API Controller
    

#### Function RestAPIController.__enable_debug(self):

```
Enable Debug
-> connection log

Args:
    None

Returns:
    None
```

#### Function RestAPIController.__init__(self, *args, **kwargs):

```
Init the RestAPIController Class
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
```

#### Function RestAPIController.get(self):

```
Get All values

Args:
    None

Returns:
    self.__result(dict): REST API response
```

#### Function RestAPIController.get_connect_status(self):

```
Get connection status

Args:
    None

Returns:
    self.__connected(bool)
```

#### Function RestAPIController.get_item(self, item_key, item_id):

```
Get one value
        
```

#### Function RestAPIController.get_request_status(self):

```
Get request status

Args:
    None

Returns:
    self.__requested
```

#### Function RestAPIController.request(self, method=None, path=None, args=None):

```
API Request

Args:
    method(str): "GET", "PUT" ...
    path(str): url = host+path
    args(dict): HTTP args

Returns:
    True if successful, False otherwise.
```


