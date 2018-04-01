#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# rest-api-controller
## Description:
`rest-api-controller` is a Python package to manage REST API requests.
We provide examples to use it.

The following files comprise the `rest-api-controller` package:
* `LICENSE`: The license file. rest-api-controller is released under the terms
of the GNU General Public License (GPL), version 3.
* `README.md`: This readme file.
* `Makefile`: Generic management tasks.
* `setup.py`: Package and distribution management.
* `setup.cfg`: The setuptools setup file.
* `test_rest_api_controller.py` : Test

The package contents itself are in the rest_api_controller directory:
* `__ init __`.py: Initialization file for the Python package.
* `rest_api_controller/rest_api_controller.py`: The code of interest.

## Setup:

    git clone https://github.com/francois-le-ko4la/rest-api-controller.git
    cd rest-api-controller
    sudo make install

## Test:

    sudo make test

## How to use this Class:

* Import the package
```python
    from rest_api_controller import RestAPIController
```

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
"""

__version__ = '0.1_dev'

from .rest_api_controller import RestAPIController
