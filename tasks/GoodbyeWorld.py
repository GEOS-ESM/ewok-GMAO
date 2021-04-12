import sys
import os
import shutil
import time
from solo.logger import Logger
from ewok.runtime import Configuration

logger = Logger(os.environ['EWOK_TASK'])

config = Configuration(sys.argv[1])
print(config)

logger.info(f'Goodbye World: {config.closing_remarks}, {config.current_cycle}')

time.sleep(90)

