# Example for fixture Dataload and log file generation

import pytest
from .BaseLogClass import LogClass  # for inheritance parent class should be imported for lof file generation

@pytest.mark.usefixtures("testDataLoad")
class TestFixtureData(LogClass):  # child class should inherit parent class name
    def test_dataloadfixture(self, testDataLoad):  # here we have to pass another mandatory parameter other than "self"
        # is <fixture mathod name> to collect the data from the method
        logprint = self.test_getLogger()  # create an object of test_getLogger() method of parent class
        #print(testDataLoad)
        logprint.info(testDataLoad)  # calling loglevel to write on logfile
        print(testDataLoad[0])
        logprint.warning(testDataLoad[0:2])
        #print(testDataLoad[0:2])

