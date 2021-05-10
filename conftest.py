"""Pytest conf file with fixture defination
"""
import pytest
from src.helper.load_data import GatherData as api_input


@pytest.fixture
def read_data():
    """Return ref to the GatherData obj as input
    """
    return api_input()

@pytest.fixture
def token(read_data):
    """Return token
    """
    return read_data.get_token()

@pytest.fixture
def header(read_data,token):
    """Return header
    """
    return read_data.get_header(token)

@pytest.fixture
def base_url(read_data):
    """Return base_url
    """
    return read_data.get_base_url()

@pytest.fixture
def order(read_data):
    """Return the list of order
    """
    return read_data.get_order()

@pytest.fixture
def endpoints(read_data):
    """Return all the endpoints
    """
    return read_data.get_endpoints()

@pytest.fixture
def log(read_data):
    """Return ref to logging module
    """
    testlogger = read_data.get_logger()
    logger = testlogger.getLogger(__name__)
    return logger
