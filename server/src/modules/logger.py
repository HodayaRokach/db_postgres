import logging
import logging.config

# Configuration definition of logs
logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {"simple": {"format": "%(levelname)s: %(message)s"}},
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "stream": "ext://sys.stdout",
        },
        "file_handler": {
            "class": "logging.FileHandler",
            "formatter": "simple",
            "filename": "my_log.log",
        },
        "error_file_handler": {
            "class": "logging.FileHandler",
            "formatter": "simple",
            "filename": "error_log.log",
            "level": "ERROR",
        },
    },
    "loggers": {
        "root": {
            "level": "DEBUG",
            "handlers": ["stdout", "file_handler", "error_file_handler"],
        }
    },
}


def setup_logger():
    logging.config.dictConfig(logging_config)
    return logging.getLogger("root")
