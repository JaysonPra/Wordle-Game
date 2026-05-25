import requests
from config.logging_config import setup_logging
from loguru import logger
from models.models import RandomWord

setup_logging()


def request_api(api_url: str) -> RandomWord | None:
    try:
        response = requests.get(api_url)
    except Exception as e:
        logger.error(f"API Request Failed: {e}")
        return None

    if response.status_code != 200:
        logger.error(f"API responded with status code: {response.status_code}")
        return None

    word_data_list: list[dict[str, str | int]] = response.json()
    if not word_data_list:
        logger.error("API returned an empty list")
        return None

    return RandomWord.model_validate(word_data_list[0])
