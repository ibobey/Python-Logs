from loggers.ErrorLogger import ErrorLogger
from loggers.MainLogger import MainLogger


if __name__ == "__main__":
    logger = MainLogger("test_logger_1")
    error_logger = ErrorLogger("error_logger_2")

    logger.log_info("selam info")
    logger.log_warning("selam error")
    logger.log_critical("selam critical")

    error_logger.log_error("error occured")
