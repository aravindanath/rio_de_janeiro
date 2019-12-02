import pytest

# @pytest.yield_fixture(scope="module")
@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request,browser):
    # print("*"*10+"One time setup one before module"+"*"*10)
    print("*" * 10 + "One time setup one before module" + "*" * 10)
    if browser == "chrome":
        value = 10
        print("running on chrome")
    elif browser == "firefox":
        value = 20
        print("running on firefox")

    if request is not None:
        request.cls.value=value

    yield
    print("*" * 10 + "One time setup one after module " + "*" * 10)
    print("Close browser")

@pytest.yield_fixture()
def setUp():
    print("#"*10+"One time setup one before method"+"#"*10)
    # if browser == "chrome":
    #     print("running on chrome")
    # elif browser == "firefox":
    #      print("running on firefox")
    yield
    print("#" * 10 + "One time setup one after method" + "#" * 10)




def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")