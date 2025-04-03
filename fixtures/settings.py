import pytest

from config import Settings


@pytest.fixture(scope="session")
def settings() -> Settings:
    """
    Фикстура создаёт объект с настройками один раз на всю тестовую сессию.

    :return: Экземпляр класса Settings с загруженными конфигурациями.
    """
    return Settings.initialize()
