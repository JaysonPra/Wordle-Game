from pydantic import BaseModel, Field


class RandomWord(BaseModel):
    word: str = Field(min_length=1)
    length: int = Field(gt=0)
    category: str
    language: str
