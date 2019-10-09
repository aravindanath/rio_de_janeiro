import logging



"""
https://docs.python.org/3/library/logging.html

LOG LEVELS
info
warning
error
critical
log
exception

"""

logging.basicConfig(filename="./Rio.log",level=logging.DEBUG,filemode=
                    'w')

logging.info("Hi all today we are learning logging in python")
logging.warning("Hi this is a warning")
logging.debug("Hi all this is debug level log..")
logging.error("hi this is error level log")
logging.exception("hi this exception level")

try:
    a= 10
    b= 10
    div =  a/b
except:
    logging.exception("Zero cant divide")

finally:
    logging.critical("Hi this is critical log")


