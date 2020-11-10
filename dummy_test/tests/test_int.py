import pytest


@pytest.fixture()
def two():
    return 2

def test_basic_int(two):
    assert 2 == two
