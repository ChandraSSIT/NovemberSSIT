# pytest
# it's testing framework
# it will automatically identify the test files and test classes and test methods
# some standards we need to follow , the file name should start with test_sample
# inside this the method name or class name should start with test
import requests


# import pytest
#  we need install pytest framework
# import pytest
# we can install from pip => this is a package manager

def get_users():
    url = 'https://gorest.co.in/public/v2/users'
    headers = {}
    payload = {}
    response = requests.get(url, headers=headers)
    print(response.status_code)
    result = response.json()

get_users()

#  to execute all the test cases we will use pytest -v
# -v will give complete detailed information about individual test cases
# to execute particular test cases we will use pytest -k testcasename

# mark
# fixture
# confest.py
# parametrize
# xskip
# xfail
