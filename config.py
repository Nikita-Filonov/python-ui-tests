from typing import Self

from pydantic import HttpUrl, DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        env_nested_delimiter='.'
    )

    app_url: HttpUrl
    headless: bool
    videos_dir: DirectoryPath
    tracing_dir: DirectoryPath
    expect_timeout: float

    @classmethod
    def initialize(cls) -> Self:
        videos_dir = DirectoryPath("./videos")
        tracing_dir = DirectoryPath("./tracing")

        videos_dir.mkdir(exist_ok=True)
        tracing_dir.mkdir(exist_ok=True)

        return Settings(videos_dir=videos_dir, tracing_dir=tracing_dir)
