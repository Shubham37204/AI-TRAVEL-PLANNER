"""
logger_config.py

This module sets up a logging system for the application.

Logging helps developers track what the application is doing,
record important events, and debug errors. Instead of printing
messages to the console, logs are stored in files so they can
be reviewed later.

What this code does:

1. Creates a directory called 'logs' if it does not already exist.
2. Generates a log file with the current date in its name.
   Example: logs/log_2026-03-14.log
3. Configures the logging system with:
   - Timestamp of the event
   - Log level (INFO, ERROR, etc.)
   - Log message
4. Provides a helper function `get_logger()` that allows different
   modules in the project to create their own logger instance.

This helps maintain structured logs across the entire project.
"""

import logging
import os
from datetime import datetime


# Directory where log files will be stored
LOGS_DIR = "logs"

# Create the logs directory if it does not exist
os.makedirs(LOGS_DIR, exist_ok=True)


# Create a log file with the current date
LOG_FILE = os.path.join(
    LOGS_DIR,
    f"log_{datetime.now().strftime('%Y-%m-%d')}.log"
)


# Configure the logging system
logging.basicConfig(
    filename=LOG_FILE,
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


def get_logger(name):
    """
    Create and return a logger instance for a specific module.

    Parameters
    ----------
    name : str
        Name of the module or component requesting the logger.

    Returns
    -------
    logging.Logger
        A configured logger object that writes logs to the log file.

    Purpose
    -------
    This function allows different parts of the application
    to create their own logger while using the same logging
    configuration.
    """

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger

