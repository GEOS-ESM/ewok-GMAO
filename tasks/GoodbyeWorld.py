import sys
import os
import shutil
import time
from solo.logger import Logger
from ewok.runtime import Configuration

logger = Logger(os.environ['EWOK_TASK'])

config = Configuration(sys.argv[1])
print(config)

logger.info(f'Goodbye World: {config.closing_remarks}')

time.sleep(90)

