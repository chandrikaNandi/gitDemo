# in some cases there is a requirement to call the same fixture for multiple times. Instead of calling it from every
# function we can wrap these test cases in a class, calling the fixture through the class
import pytest


@pytest.mark.usefixtures("setupFixture")  # write the anotation globally all methods in the class
class TestFixture:
    def test_fixtureCall(self):  # when we declare method in a class then the mandatory parameter is self
        print("I will run after fixture in class")

    def test_fixtureCall1(self):
        print("I will run after fixture1 in class")

    def test_fixtureCall2(self):
        print("I will run after fixture2 in class")

def test_nofixture():   # method without fixture
    print("i am without fixture")