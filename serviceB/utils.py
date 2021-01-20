"""Service B utils."""

import os
import sys
import flask
import logging


class RequestIdFilter(logging.Filter):
    """Format LogRecords with request id information."""

    def filter(self, record):
        """Format LogRecords with request id information."""
        if flask.has_request_context():
            if hasattr(flask.g, "request_id"):
                record.request_id = flask.g.request_id
            else:
                record.request_id = "RequestIdNotFound"
        else:
            record.request_id = "NotInRequestContext"
        return True


def configure_logging():
    """Set up the python logging module."""
    # Get the logging level
    level = logging.INFO
    if bool(os.environ.get("DEBUG", False)):
        level = logging.DEBUG

    # Configure the root logger
    root_logger = logging.getLogger("")
    root_logger.setLevel(level)

    # Remove any existing handlers
    for handler in root_logger.handlers:
        handler.close()
        root_logger.removeHandler(handler)

    # Create the request id Formatter
    format = ""
    format += "%(asctime)s"
    format += " %(levelname)7s"
    format += " [ %(request_id)s ]"
    format += " %(name)s:%(funcName)s:%(lineno)d"
    format += " %(message)s"
    formatter = logging.Formatter(fmt=format)

    # Create the request id Filter
    filter = RequestIdFilter()

    # Create the root logger console handler
    console_handler = logging.StreamHandler(stream=sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(level)
    console_handler.addFilter(filter)
    root_logger.addHandler(console_handler)
