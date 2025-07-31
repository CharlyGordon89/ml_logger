"""
Reusable logging setup for ML projects.
Logs are written to both console and timestamped log files.
"""

import os
import sys
import logging
from datetime import datetime
from pathlib import Path

from rich.logging import RichHandler


def get_logger(name: str = "ml_logger",
               log_dir: str = "logs",
               log_level: int = logging.INFO) -> logging.Logger:
    """
    Creates and returns a logger instance with rich console + file logging.
    
    Args:
        name (str): Name of the logger (default: "ml_logger").
        log_dir (str): Directory to save log files.
        log_level (int): Logging level (e.g., logging.INFO).
    
    Returns:
        logging.Logger: Configured logger instance.
    """
    # Create log directory if not exists
    Path(log_dir).mkdir(parents=True, exist_ok=True)

    # Format log filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file_path = os.path.join(log_dir, f"{name}_{timestamp}.log")

    # Formatter
    fmt = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"

    # Create handlers
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setFormatter(logging.Formatter(fmt, datefmt))

    console_handler = RichHandler(rich_tracebacks=True)
    console_handler.setFormatter(logging.Formatter(fmt, datefmt))

    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # Avoid double logging in Jupyter
    logger.propagate = False

    return logger
