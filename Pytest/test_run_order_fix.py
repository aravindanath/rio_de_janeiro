
"""
https://pytest-ordering.readthedocs.io/en/develop/
"""
import pytest

@pytest.mark.run(order=2)
def test_method1(oneTimeSetUp,setUp):
    print("Method one")

@pytest.mark.run(order=1)
def test_method2(oneTimeSetUp,setUp):
    print("Method two")

@pytest.mark.run(order=3)
def test_method3(oneTimeSetUp,setUp):
    print("Method three")

@pytest.mark.run(order=4)
def test_method4(oneTimeSetUp,setUp):
    print("Method four")

@pytest.mark.run(order=5)
def test_method5(oneTimeSetUp,setUp):
    print("Method five")

@pytest.mark.run(order=6)
def test_method6(oneTimeSetUp,setUp):
    print("Method six")