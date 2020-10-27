# here assert takes two parameters. One condition and other is AssertError msg.
# if assert returns TRUE the msg will not shown
import pytest  # to use @pytest we have to import pytest

@pytest.mark.skip  # to skip a test case which have some functional or verification problem
def test_checkAssert():
    msg = "chandrika"
    assert msg == "chan", "This is a wrong information. Test error"

# although assert returns False and pytest shows error in runtime, but it will check all the test methods till end


@pytest.mark.smoke  # to mark a test smoke
def test_CheckMsg():
    print("After the error occured the test run is check all the files there")


