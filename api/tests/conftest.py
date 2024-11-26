import os

import pytest

from api.client import DiscordClient


@pytest.fixture(scope="session")
def client():
    return DiscordClient(token=os.getenv("DISCORD_BOT_TOKEN"))
