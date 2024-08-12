import os

from src.modules.logger import setup_logger


LOG_FILE = "my_log.log"
ERROR_LOG_FILE = "error_log.log"


def setup_module(module):
    """Remove log files if they exist."""
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
    if os.path.exists(ERROR_LOG_FILE):
        os.remove(ERROR_LOG_FILE)


def test_logger():
    """Test logging functionality."""
    logger = setup_logger()

    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.critical("Critical message")

    assert os.path.exists(LOG_FILE)
    assert os.path.exists(ERROR_LOG_FILE)

    with open(LOG_FILE, "r") as file:
        logs = file.read()
        assert "Debug message" in logs
        assert "Info message" in logs
        assert "Warning message" in logs
        assert "Error message" in logs
        assert "Critical message" in logs

    with open(ERROR_LOG_FILE, "r") as file:
        error_logs = file.read()
        assert "Error message" in error_logs
        assert "Critical message" in error_logs
        assert "Debug message" not in error_logs
        assert "Info message" not in error_logs
        assert "Warning message" not in error_logs
