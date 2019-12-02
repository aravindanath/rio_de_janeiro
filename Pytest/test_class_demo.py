# Structure Tests in a Test Class
import pytest

from Day17_pytest_demo.class_to_test import SomeClassToTest

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class TestClassDemo():

    @pytest.fixture(autouse=True)
    def classSetup(self,oneTimeSetUp):
        # Object of the class
        self.abc = SomeClassToTest(self.value)

    def test_methodA(self):

        result = self.abc.sumNumber(5,5)
        assert result == 11
        print("running method A")

    def test_methodB(self):
        print("Running method B")

# /Users/aravindanathdm/PycharmProjects/PythonSeleniumProject/Day17_pytest_demo