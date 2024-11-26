import os
from time import sleep

import pytest
from api.client import DiscordClient


@pytest.fixture(scope="session")
def client():
    return DiscordClient(token=os.getenv("DISCORD_BOT_TOKEN"))


@pytest.fixture(scope="function", autouse=True)
def timeout():
    sleep(2)
