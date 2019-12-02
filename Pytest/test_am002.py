import pytest

@pytest.yield_fixture()
def setUp():
    print("Before test")
    yield
    print("After test")

def test_method1():
    print("Method one")

def test_method2():
    print("Method two")
