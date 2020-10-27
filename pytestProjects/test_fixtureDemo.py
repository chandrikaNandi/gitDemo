# this is FIXTURE example. It is also called SETUP TEARDOWN method
# Fixture is used to opening up some browser, setting up some database instance, creating some configuration properties,
# environment variables. It is like the prerequisite stuffs
import pytest

# if the pytest.fixtrue() methods are needed for multiple test cases of multiple files, then writing the same fixture
# code in every file is the redundancy of coding. so to reduce coding and optimise the coding pytest.fixtrue() methods
# should be written in one file called conftest.py to generalized same location where all test files are saved

def test_fixtureCall(setupFixture):  # calling the fixture method by passing <method name> in parameter
    print("I will run after fixture")