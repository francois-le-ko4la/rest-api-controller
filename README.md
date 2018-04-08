# rest-api-controller
## Description:
`rest-api-controller` is a Python package to manage REST API requests.
We provide examples to use it.

The following files comprise the `rest-api-controller` package:
* `LICENSE`: The license file. `rest-api-controller` is released under the
terms of the GNU General Public License (GPL), version 3.
* `README.md`: This readme file.
* `Makefile`: Generic management tasks.
* `setup.py`: Package and distribution management.
* `setup.cfg`: The setuptools setup file.
* `test_rest_api_controller.py` : Test

The package contents itself are in the `rest_api_controller` directory:
* `__ init __`.py: Initialization file for the Python package.
* `rest_api_controller/rest_api_controller.py`: The code of interest.

## Setup:
```shell
git clone https://github.com/francois-le-ko4la/rest-api-controller.git
cd rest-api-controller
make install

## Test:
```shell
make test
```

## Use:

* Import the package
```python
from rest_api_controller import RestAPIController
```

* API wo authentication using tests
```python
import time


#init the Class
my_api = RestAPIController(host="http://api.open-notify.org",
    DEBUG=True)

# send the request
result = my_api.request("GET", "/iss-now.json")

# test result
if result is None:
    exit()

# use the result
print(result)
print(time.ctime(int(result['timestamp'])))
print(result['iss_position']['longitude'] + ", " +
    result['iss_position']['latitude'])
```

* API OAuth1 (username / token) - GITHUB
```python
my_github_api = RestAPIController(
    host = "https://api.github.com",
    auth = ("*** USERNAME ***", "*** TOKEN ***"),
    DEBUG= True
    )
my_github_api.request("GET", "/user")
```

* OAuth Token - Facebook
```python
my_fb_api = RestAPIController(
    token=("OAuth", "*** TOKEN ***"),
    host = "https://graph.facebook.com",
    DEBUG = True
    )
my_fb_api.request("GET", "/v2.12/me/taggable_friends",
    {'fields':'id, name, picture.width(500).height(500).type(large)',
    'limit':'5000'})
```

## Todo:

- [X] Create the project
- [X] Write code and tests
- [X] Test installation and requirements (setup.py and/or Makefile)
- [X] Test code
- [X] Validate features
- [X] Write Doc/stringdoc
- [X] Run PEP8 validation
- [ ] Clean & last check
- [ ] Release

## Note:

This script is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3 of the License, or (at your option) any later version.

This script is provided in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

## Dev docstring


### RestAPIController()

````python
class RestAPIController():
````

> <br />
> My REST API Controller<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  <br />
> <br />

#### RestAPIController.__enable_debug(func)

````python
def RestAPIController.__enable_debug(func):
````

> <br />
> Enable Debug<br />
> -> connection log<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  func: decorated function<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  func(self, *args, **kwargs)<br />
> <br />

#### RestAPIController.__isconnected(func, timeout=5)

````python
def RestAPIController.__isconnected(func, timeout=5):
````

> <br />
> Test network connection<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  func: decorated function<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  timeout (int): timeout with a default value.<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  link up: func(self, *args, **kwargs)<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  link down: None<br />
> <br />

#### RestAPIController.__loadjson(func)

````python
def RestAPIController.__loadjson(func):
````

> <br />
> Decorator - take the content from REST API server and provide a JSON<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  func: decorated function<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  json<br />
> <br />

#### RestAPIController.__sendrequest(func)

````python
def RestAPIController.__sendrequest(func):
````

> <br />
> Decorator - Use requests.request and arguments from request()<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  func: decorated function<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  str: The return value (answer).<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Content for success, None otherwise.<br />
> <br />

#### RestAPIController.__init__(self, host, auth=None, token=None, debug=False)

````python
def RestAPIController.__init__(self, host, auth=None, token=None, debug=False):
````

> <br />
> Init the RestAPIController Class<br />
> This function define attributes.<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  host (string)<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  auth (dict)<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  token (dict)<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  debug (bool)<br />
> <br />
> <b>Attributes:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  self.__host (string)<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  self.__auth (dict)<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  self.__token (dict)<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  self.__debug (bool)<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  obj<br />
> <br />

#### RestAPIController.isconnected(self)

````python
def RestAPIController.isconnected(self):
````

> <br />
> Provide a link status between this script & REST API server<br />
> This function is decorated by @__isconnected.<br />
> If the link is down, then decorator will change the value.<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  True<br />
> <br />

#### RestAPIController.request(self, cur_method, cur_path, cur_args=None)

````python
def RestAPIController.request(self, cur_method, cur_path, cur_args=None):
````

> <br />
> Provide all arguments to request.<br />
> This function is decorated by __enable_debug,<br />
> __isconnected, __sendrequest, and __loadjson<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  cur_method (str): "GET", "PUT" ...<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  cur_path (str): url = host+path<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  cur_args (dict): HTTP args<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  dict(): request's args send to decorators<br />
> <br />