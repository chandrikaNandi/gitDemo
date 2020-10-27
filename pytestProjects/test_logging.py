import logging  # to create log file logging class should be imported

# as it is a pytest file we have to wrap every test case(code) in a method

def test_logFileDemo():
    logger = logging.getLogger(__name__)  # retLogger will help to get an object to the logging feature, __name__
    # attribute means log write in log file the file name that is test_logging.py

    filehandler = logging.FileHandler("logFile.log")  # method FileHandler(<filename>)means in which file the log
    # statements are written, basically create a new log file with <filename> at first then append the log statements

    fileformat = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")  # sets the format of the
    # output of log file, asctime = time it's a python keyword

    filehandler.setFormatter(fileformat)  # passes the format info to filehandler.setFormatter() method and then
    # filehandler send it to logger through addHandler(), it is done this via way because addHandler() method has
    # provision to take one argument

    logger.addHandler(filehandler)  # logger object should know in which file log has to be print.so what format and
    # what file should be sent to addHandler() method

    # ordered levels of logs
    logger.setLevel(logging.WARNING)  # it sets the level of logging msg shown, means now it will show from warning
    # level till end and skip debug and error level

    # like print statement only, it will print in one file with levelname tag instead of print in console
    logger.debug("A debug statement is executed")

    logger.info("Information Statement")

    logger.warning("something is in warning mode")

    logger.error("Some Error Occur")

    logger.critical("Critical issue")
