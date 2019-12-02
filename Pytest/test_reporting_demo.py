# Structure Tests in a Test Class
import pytest

from Day17_pytest_demo.class_to_test import SomeClassToTest

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class TestReportingDemo():

    @pytest.fixture(autouse=True)
    def classSetup(self,oneTimeSetUp):

        self.abc = SomeClassToTest(self.value)

    def test_methodA(self):

        result = self.abc.sumNumber(5,1)
        assert result < 40
        print("running method A")

    def test_methodB(self):
        print("Running method B")

#  py.test -s -v test_reporting_demo.py --browser firefox --html=../output/htmlreport.html