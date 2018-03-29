#!/usr/bin/env python3

from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
        name='rest-api-controller',
        version='0.1',
        description='The funniest Rest API controller',
        long_description=readme(),
        python_requires='>=3.6',
        classifiers=[
                        'Development Status :: 3 - Alpha',
                        'Environment :: Console',
                        'Programming Language :: Python :: 3.6',
                        'Topic :: REST API :: Social Network / Cloud',
                                                  ],
        url='https://github.com/francois-le-ko4la/rest-api-controller',
        author='Ko4lA',
        author_email='francois@le.ko4la.fr',
        license='',
        packages=['rest_api_controller'],
        test_suite="tests.test_rest_api_controller",
        zip_safe=False
        )

