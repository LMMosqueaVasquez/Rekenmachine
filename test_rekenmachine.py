



import pytest
from rekenmachine import Rekenmachine

@pytest.fixture
def rekenmachine():
    return Rekenmachine()
 
 
def test_summation(rekenmachine):
    assert 10 == rekenmachine.summation(5, 5)
 
 
def test_difference(rekenmachine):
    assert 4 == rekenmachine.difference(8, 4)