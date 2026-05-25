import pytest
from models.models import RandomWord
from pydantic import ValidationError


def test_random_word_validate_success() -> None:
    mock_api_response: dict[str, str | int] = {
        "word": "apple",
        "length": 5,
        "category": "wordle",
        "language": "en",
    }

    validated_model = RandomWord.model_validate(mock_api_response)

    assert isinstance(validated_model, RandomWord)
    assert validated_model.word == "apple"


def test_random_word_validate_failure() -> None:
    mock_api_response: dict[str, str | int] = {
        "word": 12345,
        "unexpected_fieid": "error",
    }

    with pytest.raises(ValidationError):
        RandomWord.model_validate(mock_api_response)
