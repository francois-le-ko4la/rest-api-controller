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

# test if we can reach the server
if my_api.isconnected() is not True:
    print("Server unreachable...")
    exit(1)

# send the request
my_api.request("GET", "/iss-now.json")

# get the request status
if my_api.isrequested() is not True:
    print("Request errot...")
    exit(1)

# use the result
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
    host = "https://graph.facebook.com",
    DEBUG = True
    )

my_fb_api.request("GET", "/v2.12/me/taggable_friends",
    {'fields':'id, name, picture.width(500).height(500).type(large)',
    'limit':'5000'})
friendsList = my_fb_api.get()
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
### RestAPIController

````python
class RestAPIController:
````

><br />
> My REST API Controller <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    <br />
> <br />

#### RestAPIController.__enable_debug
````python
def RestAPIController.__enable_debug(self):
````
><br />
> Enable Debug <br />
> -> connection log <br />
>  <br />
> <b> Args: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   None <br />
>  <br />
> <b> Returns: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   None <br />
> <br />
#### RestAPIController.__isconnected
````python
def RestAPIController.__isconnected(self, timeout=5):
````
><br />
> Test network connection <br />
>  <br />
> <b> Args: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   timeout (int): timeout with a default value. <br />
>  <br />
> <b> Returns: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   bool: The return value. True for success, False otherwise. <br />
> <br />
#### RestAPIController.__init__
````python
def RestAPIController.__init__(self, *args, **kwargs):
````
><br />
> Init the RestAPIController Class <br />
> This function define attributes. <br />
>  <br />
> <b> Args: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   *arg/**kwargs <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   auth (dict) <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   token (dict) <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   host (string) <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   DEBUG (bool) <br />
>  <br />
> <b> Attributes: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   self.__connected (bool) <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   self.__requested (bool) <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   self.__auth (dict) <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   self.__token (dict) <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   self.__debug (bool) <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   self.__host (string) <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   self.__result (dict) <br />
>  <br />
> <b> Returns: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   obj <br />
> <br />
#### RestAPIController.get
````python
def RestAPIController.get(self):
````
><br />
> Get the result <br />
>  <br />
> <b> Args: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   None <br />
>  <br />
> <b> Returns: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   self.__result (dict): REST API response <br />
> <br />
#### RestAPIController.get_item
````python
def RestAPIController.get_item(self, item_key, item_id):
````
><br />
> Get one value <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    <br />
> <br />
#### RestAPIController.isconnected
````python
def RestAPIController.isconnected(self):
````
><br />
> Get connection status <br />
>  <br />
> <b> Args: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   None <br />
>  <br />
> <b> Returns: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   bool: The return value. True for success, False otherwise. <br />
> <br />
#### RestAPIController.isrequested
````python
def RestAPIController.isrequested(self):
````
><br />
> Get request status <br />
>  <br />
> <b> Args: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   None <br />
>  <br />
> <b> Returns: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   bool: The return value. True for success, False otherwise. <br />
> <br />
#### RestAPIController.request
````python
def RestAPIController.request(self, method=None, path=None, args=None):
````
><br />
> API Request <br />
>  <br />
> <b> Args: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   method (str): "GET", "PUT" ... <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   path (str): url = host+path <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   args (dict): HTTP args <br />
>  <br />
> <b> Returns: </b> <br />
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   bool: The return value. True for success, False otherwise. <br />
> <br />
