from pydantic import BaseModel


class UserState(BaseModel):
    state: int
    level_index: int
    quizz_index: int
    game_mode: int
    correct_answers: int
    mistakes: int
    arts: list


class Level(BaseModel):
    id: int
    title: str
    description: str
    description_image: str
    Arts: list


class Art(BaseModel):
    author: str
    image: str
