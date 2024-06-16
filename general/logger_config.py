import os
from loguru import logger
import config

# Configure loguru to log to a file with daily rotation
log_file_path = os.path.join(config.PATH_LOG, 'AI_PostWave.log')
logger.add(log_file_path, rotation="1 day")

# Optionally, add more configuration for logging to console, setting levels, etc.
logger.info("Logger initialized with daily rotation.")

# Ensure the logger configuration can be imported and used in other modules
def get_logger():
    return logger
