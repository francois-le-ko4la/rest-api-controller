#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# apicontroller
## Description:
`apicontroller` is a Python package to manage REST API requests.
We provide examples to use it.

## Setup:
```shell
$ git clone https://github.com/francois-le-ko4la/rest-api-controller.git
$ cd rest-api-controller
$ make install
```

## Test:
```shell
$ make test
```

## Use:

* Import the package
```python
from apicontroller import RestAPIController
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

## Project structure

```
.
├── apicontroller
│   ├── __about__.py
│   ├── controller.py
│   └── __init__.py
├── LICENSE
├── Makefile
├── MANIFEST.in
├── pictures
│   ├── classes_apicontroller.png
│   └── packages_apicontroller.png
├── README.md
├── requirements.txt
├── runtime.txt
├── setup.cfg
├── setup.py
└── tests
    ├── test_doctest.py
    ├── test_pycodestyle.py
    └── use_it.py
```

## Todo:

- [X] Create the project
- [X] Write code and tests
- [X] Test installation and requirements (setup.py and/or Makefile)
- [X] Test code
- [X] Validate features
- [X] Write Doc/stringdoc
- [X] Run PEP8 validation
- [X] Clean & last check
- [X] Release

## License

pytping is distributed under the [GPLv3 license](./LICENSE)

"""

import apicontroller.__about__
from apicontroller.controller import RestAPIController
