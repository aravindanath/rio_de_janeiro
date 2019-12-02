import pytest

@pytest.yield_fixture()
def setUp():
    print("#"*10+" Before method "+"#"*10)
    yield
    print("*"*10+" After method "+"*"*10)

def test_method1(setUp):
    print("Method one")

def test_method2(setUp):
    print("Method two")



#  py.test -s -v test_Am001.py
#  py.test -s -v Day17_pytest_demo/test_Am001.py