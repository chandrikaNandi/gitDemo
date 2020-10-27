# here we test pytest mark(tag) which is similar to Tagging in Cucumber framework and Grouping in TestNG fraework
# some cases where we have to run a selective group of test cases(methods) like smoke or regression we have to use this
import pytest

@pytest.mark.smoke
def test_checkMark1():
    print("Checking selective test cases like smoke")

# if some time execution of some output is required to achieve next method to run instead some error in first method
# we have to run it tagging xfail so that it will only execute correct code and skip the part where code is wrong
# --- UNIQUE FEATURE in PYTEST and not available any other test framework
@pytest.mark.xfail
def test_checkMark2():
    a = 5
    b = 7
    print(a+b)
    assert a + b == 11, "wrong calculation"
