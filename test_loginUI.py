import pytest
from login_page import *

def test_login_valid():
    result = login_ui()
    assert result == True

def test_login_in_valid():
    result = login_ui()
    assert result == True