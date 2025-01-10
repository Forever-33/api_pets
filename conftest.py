import requests
import pytest

BASE_URL = 'https://petstore.swagger.io/v2/'


# @pytest.fixture(autouse=True, scope='session')
# def session():
#     http_session = requests.Session()
#     yield http_session
#     http_session.close()
