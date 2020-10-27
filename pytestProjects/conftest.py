# this is FIXTURE example. It is also called SETUP TEARDOWN method
# Fixture is used to opening up some browser, setting up some database instance, creating some configuration properties,
# environment variables. It is like the prerequisite stuffs
import pytest

# fixture example
@pytest.fixture()   # setup fixture to this method means whichever test case call it the fixture method will execute
# before than the calling method
def setupFixtureDemo():
    print("I will run first")
    yield  # it will run at the end of the calling test case execution, it means hold whatever are written after yield
    print("I will run last")


# scope class fixture example
@pytest.fixture(scope="class")  # if we call the fixture before class initialization and yield at the end of all
# test case execution in the class then scope="class"
def setupFixture():
    print("I will run first")
    yield
    print("I will run last")


# data load fixture example
@pytest.fixture()
def testDataLoad():
    # this method to pass all the data to the test case whether it is in list or tuple
    return ["Chandrika", "Nandi", "Python", "selenium"]


# parameterized fixture example
@pytest.fixture(params=[("data1", "param1", "param2"), ("data2", ""), ("data3", "param10")])
def paramfixture(request):  # for parameterized fixture we have to declare an instance called request(it belongs to
    # fixture) in method. Instance will take one data at a time like at first run "data1", second run "data2" like this
    return request.param   # return specific parameter of request instance

