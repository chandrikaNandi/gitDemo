# USEFUL INFORMATION TO REMEMBER ALWAYS WHEN WORKING WITH PYTEST
# any pytest file the naming convention should be test_filename or filename_test

# In pytest whatever code is written it is wrapped in function called pytest methods

# functions have also naming cconvention as filename, like test_functionname, and it is required also when there is
# selective methods which need to run by pytest, so always give some meaningfull name to your methods

# In command prompt we can run specific file with py.test <filename>
# In command prompt -k stands for method names execution(extracts the keyword from method name and match),
# -s stands for logs in output, -v stands for more info <matadata>
def test_pytest1MSG():
    print("first pytest program")

# if more than one methods in A FILE exist then pytest overloads the final one,
# if in Two DIFFERENT FILES have same method then overload will not happen
def test_pytest2Msgs():
    print("second pytest program")
