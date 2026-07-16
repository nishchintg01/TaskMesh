"""
Logging Module
"""

import sys
import json
import logging
from app.core.config import settings


class Logger(logging.Logger):
    """
    Class to Handle TaskMesh Application Logging 

    Args:
        logging (logging): Inherits Python Logging Module
    """
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }

    STREAM_FORMAT = "%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s"

    def __init__(self, name: str, level: str = settings.log_level) -> None:
        super().__init__(name, level)

        # 1. Define a standardized log format
        formatter = logging.Formatter(self.STREAM_FORMAT)

        # 2. Setup Console (Stream) Handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        self.addHandler(console_handler)
