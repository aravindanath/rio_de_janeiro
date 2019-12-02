"""
file name should start with test
test method name should start with test

py.test test_module.py --> run in module
py.test package/module.py --> run all the testcases in module
py.test package/module.py::test_method --> to run particular method

-s print statement
-v verbose ---> provides more informations

py.test -s -v

"""


import pytest

@pytest.fixture()
def setUp():
    print("Setup one")


def test_method1(setUp):
    print("Method one")


def test_method2(setUp):
    print("Method one")

#  py.test -v -s