import pytest


@pytest.fixture
def fixture_return_list_of_numbers():
    return [4, 2, 10, 4]


@pytest.fixture
def fixture_return_set():
    a = {'w', 'h', '3', 't'}
    return a


@pytest.fixture
def fixture_return_dictionary():
    d = {'Pavel': 3, 'Misha': 5, 'Gena': 4}
    return d


@pytest.fixture
def fixture_return_string():
    hw = 'hello world'
    return hw
