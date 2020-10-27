import logging
import inspect  # have to import for inspect.stack() method

class LogClass:
    def test_getLogger(self):
        testfilename = inspect.stack()[1][3]  # take the name of the test case(method) and send it to getlogger() method
        logger = logging.getLogger(testfilename)
        #logger = logging.getLogger(__name__)
        #logger = logging.getLogger()  # it shows the output "root:"

        filehandler = logging.FileHandler("logFile.log")

        fileformat = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
        filehandler.setFormatter(fileformat)

        logger.addHandler(filehandler)

        logger.setLevel(logging.DEBUG)
        return logger
