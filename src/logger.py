import os
import logging
from datetime import datetime

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
LOG_PATH = os.path.join(LOG_DIR, LOG_FILE)

logging.basicConfig(
    filename=LOG_PATH,
    format='[ %(asctime)s ] %(levelname)s %(message)s',
    level=logging.INFO
)

logging.info("Logging has started")
