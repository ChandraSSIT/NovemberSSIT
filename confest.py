import pytest


@pytest.fixture(scope="function")
def get_authorization_token():
    # developer will provide an api to get the token
    return "Bearer fd1238058e05068d7f6774fc91cc9ee99d311defac6f770d6e0d2394dd315c97"

# @pytest.fixture()
# def get_application_driver():

