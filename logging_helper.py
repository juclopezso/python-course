import logging


# set the logging name to the module name
logger = logging.getLogger(__name__)
# don't propagate to parent logger
# logger.propagate = False

logger.info('Hello from helper')