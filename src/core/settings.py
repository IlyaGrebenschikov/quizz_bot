from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import DirectoryPath

from pathlib import Path

from functools import lru_cache


class SettingsEnv(BaseSettings):
    root_dir: DirectoryPath = Path(__file__).parent.parent.parent
    model_config = SettingsConfigDict(
        env_file=f'{root_dir}/.env',
        env_file_encoding='utf-8',
    )

    BOT_TOKEN: str


class SettingsToken(SettingsEnv):
    @property
    def get_token(self) -> str:
        return self.BOT_TOKEN


class Settings:
    env: SettingsEnv = SettingsEnv()
    token: SettingsToken = SettingsToken()


@lru_cache(typed=True)
def get_settings() -> Settings:
    return Settings()
