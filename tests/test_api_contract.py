from config.settings import settings
from models.models import RandomWord
from wordle.word_ingestion import request_api


def test_live_api_matches_contract() -> None:
    response = request_api(settings.api_url)

    assert response is not None

    assert isinstance(response, RandomWord)
