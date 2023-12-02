from loggers.BaseLogger.ILogger.ILogger import ILogger
from logging import Logger
from dotenv import load_dotenv
from os import getenv
import os


class BaseLogger(ILogger):
    _FOLDER_NAME: str
    _FILE_NAME: str

    _LOGGER_NAME: str
    _IS_ENV_LOADED: bool
    _LOG_FORMAT: str

    IS_ENV_EXISTS: bool
    logger: Logger

    def __init__(self):
        self.IS_ENV_EXISTS = BaseLogger._load_env()
        self._set_const_env_vars()
        BaseLogger._create_log_folder(folder_name=self._FOLDER_NAME)

    @staticmethod
    def _load_env() -> bool:
        if load_dotenv() is False:
            return False
        return True

    @staticmethod
    def _create_log_folder(folder_name: str) -> bool:
        if not os.path.exists(f"./{folder_name}"):
            os.makedirs(folder_name)
            return True
        return False

    def _set_const_env_vars(self) -> bool:
        self._FOLDER_NAME: str = getenv("LOGS_FOLDER_NAME", "logs")
        self._LOG_FORMAT: str = getenv("LOG_FORMAT", "| %(levelname)s | %(asctime)s | %(name)s | %(message)s")
        return True

    def _set_env_vars(self) -> bool:
        ...

    def _setup(self) -> None:
        ...

    def log_error(self, message: str) -> None:
        ...
