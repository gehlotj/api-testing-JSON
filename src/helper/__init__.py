import logging
from os import path

BASE_DIR    = path.abspath('.')
LOG_FILE    = 'logs/tests.log'

logging.basicConfig(filename=path.join(BASE_DIR,LOG_FILE),\
filemode='w', format='%(name)s - %(levelname)s - %(message)s',level=logging.INFO)
