from loggers.BaseLogger.BaseLogger import BaseLogger
from os import getenv
import logging


class MainLogger(BaseLogger):

    def __init__(self, logger_name: str):
        self._LOGGER_NAME = logger_name
        super().__init__()
        self._set_env_vars()
        self._setup()

    def _set_env_vars(self) -> bool:
        if self.IS_ENV_EXISTS is not True:
            raise Exception("Cannot find env variables")
        self._FILE_NAME: str = getenv("LOGS_FILE_NAME", "serverLogs")
        return True

    def _setup(self) -> None:
        self.logger = logging.getLogger(self._LOGGER_NAME)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter(self._LOG_FORMAT)
        file_handler = logging.FileHandler(f'{self._FOLDER_NAME}/{self._FILE_NAME}.log')
        self.logger.setLevel(logging.INFO)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def log_info(self, message: str) -> None:
        self.logger.info(message)

    def log_warning(self, message: str) -> None:
        self.logger.warning(message)

    def log_critical(self, message: str) -> None:
        self.logger.critical(message)

    def log_error(self, message: str) -> None:
        self.logger.error(message)
