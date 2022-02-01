# Logging - Python already comes with powerful built in modules.
# We can quickly login to our application by simple saying import logging

import logging
logging.basicConfig()

logging.debug("This is a debug message")
logging.info("This is a info message")
logging.warning("This is a warning message")
logging.error("This is a error message")
logging.critical("This is a critical message")
# Warning, error and critical message are only printed
