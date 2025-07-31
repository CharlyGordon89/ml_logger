from ml_logger import get_logger

def test_logger_runs():
    logger = get_logger("test_logger", log_dir="test_logs")
    logger.info("This is a test message")
