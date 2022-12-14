import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

import logging_helper


# log to 5 different levels
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')

logger = logging.getLogger(__name__)

# Create handlers
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('file.log')

# Configure level and formatter and add it to handlers
stream_handler.setLevel(logging.WARNING) # warning and above is logged to the stream
file_handler.setLevel(logging.ERROR) # error and above is logged to a file

stream_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(stream_format)
file_handler.setFormatter(file_format)

# Add handlers to the logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.warning('This is a warning') # logged to the stream
logger.error('This is an error') # logged to the stream AND the file!

# config from file

# import logging.config
# logging.config.fileConfig('logging.conf')
# logger = logging.getLogger('simpleExample')
# logger.debug('debug message from file config')


# capturing stack trace

try:
  a = [1,2,3]
  val = a[3]
except Exception as e:
  logging.error(e, exc_info=True)

# the same using traceback
import traceback

try:
  a = [1,2,3]
  val = a[3]
except:
  logging.error(f"The error is: {traceback.format_exc()}")

# remember the RotatingFileHandler helps to create logs that are not too big
# also the TimedRotatingFileHandler helps to create logs that are not too big and are rotated at a certain time interval
# also use the json formatter to log in json format