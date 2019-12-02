import pytest


def test_method1(oneTimeSetUp,setUp):
    print("Method one")


def test_method2(oneTimeSetUp,setUp):
    print("Method two")

#  py.test -v -s

# py.test -s -v test_conftest__demo*.py

# py.test -s -v test_conftest_demo1.py --browser firefox

# py.test -s -v test_conftest_demo1.py::test_method2  --browser chrome