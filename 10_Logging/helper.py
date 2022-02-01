import logging

logger = logging.getLogger(__name__)
# If we don't want to progate the logger
# By default it is True
logger.propagate = False
logger.info("Hello from helper")