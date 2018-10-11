import pytest
from os import path
from crontab_check.process import get_modified_time, run
from logging.config import fileConfig
from logging import getLogger
# from crontab_check.alert import Alert
from datetime import datetime

def pytest_addoption(parser):
    parser.addoption('-f','--tabfile', type=str, dest='crontab_path', required='True',
                    help='the file path of the crontab file')
    parser.addoption('-u', '--user', dest='user', type=str, default='root',
                        help='linux username if the crontab is for specific user')

@pytest.fixture
def f(request):
    return request.config.getoption('--tabfile')

@pytest.fixture
def u(request):
    return request.config.getoption('--user')

@pytest.fixture
def logger():
    print(path.dirname(path.realpath(__file__)) + path.sep + 'crontab_check'+path.sep+'logging.conf')
    with open(path.dirname(path.realpath(__file__)) + path.sep + 'crontab_check'+path.sep+'logging.conf') as f:
        fileConfig(f)
    logger = getLogger()
    logger.debug('test suits started')
    assert logger is not False
    return logger

def test_get_modified_time(logger):
    logger.info('testing get modified time function')
    t = get_modified_time(filepath='/tmp', logger = logger)
    assert t < datetime.now().timestamp()

    # assert get_modified_time(filepath='', logger=logger) is False
    assert get_modified_time('/home/boat') is False