import os.path
from dotenv import load_dotenv
from os import getenv


def test_is_dotenv_loaded():
    env_file: bool = load_dotenv()
    if env_file is not True:
        assert False
    assert True


def test_is_env_file_exists():
    file: bool = os.path.exists("./.env")
    if file is not True:
        assert False
    assert True


def test_is_file_created():
    load_dotenv()
    LOGS_FOLDER_NAME: str = getenv("LOGS_FOLDER_NAME", "logs")
    is_folder_exists: bool = os.path.isdir(LOGS_FOLDER_NAME)
    if is_folder_exists is not True:
        assert False
    assert True
