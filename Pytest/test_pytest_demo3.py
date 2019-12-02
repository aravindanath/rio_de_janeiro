import pytest

@pytest.fixture()
def setUp():
    print("Setup one")


def test_method1(setUp):
    print("Method one")


def test_method2(setUp):
    print("Method one")

#  py.test -v -s
# py.test -s -v test_pytest_demo*.py