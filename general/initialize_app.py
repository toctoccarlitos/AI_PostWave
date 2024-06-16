from os import path, makedirs
import config

from general.logger_config import get_logger
logger = get_logger()

def initialize_app_data():
    """
    Initialize the application data path and its internal structure.
    Creates the main app data directory and the logs directory if they do not exist.
    """
    try:
        # Check if the main app data path exists; if not, create it
        if not path.exists(config.PATH_APP_DATA):
            makedirs(config.PATH_APP_DATA)
            logger.info(f"Created main app data directory: {config.PATH_APP_DATA}")

        # Check if the logs path exists; if not, create it
        if not path.exists(config.PATH_LOG):
            makedirs(config.PATH_LOG)
            logger.info(f"Created logs directory: {config.PATH_LOG}")

        # Check if the tmp path exists; if not, create it
        if not path.exists(config.PATH_TMP):
            makedirs(config.PATH_TMP)
            logger.info(f"Created temporary directory: {config.PATH_TMP}")

    except Exception as e:
        # Log any exceptions that occur during the directory creation process
        logger.error(f"An error occurred while initializing app data paths: {e}")