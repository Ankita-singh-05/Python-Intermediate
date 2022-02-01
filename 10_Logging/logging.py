# Logging - Python already comes with powerful built in modules.
# We can quickly login to our application by simple saying import logging

import logging
from time import asctime
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    datefmt="%m/%d/%Y %H:%M:%S")

logging.debug("This is a debug message")
logging.info("This is a info message")
logging.warning("This is a warning message")
logging.error("This is a error message")
logging.critical("This is a critical message")
# Warning, error and critical message are only printed
import helper
