import os
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from web.pages.login import LoginPage
from web.pages.channel import ChannelPage


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def login(driver):
    load_dotenv()

    discord_email = os.getenv("DISCORD_EMAIL")
    discord_password = os.getenv("DISCORD_PASSWORD")

    if discord_email is None or discord_password is None:
        raise ValueError("DISCORD_EMAIL and DISCORD_PASSWORD must be set in .env")

    login_page = LoginPage(driver, email=discord_email, password=discord_password)
    login_page.open()
    login_page.login()


@pytest.fixture(scope="function")
def channel_page(driver, login):
    load_dotenv()
    channel_id = os.getenv("CHANNEL_ID")

    if channel_id is None:
        raise ValueError("CHANNEL_ID must be set in .env")

    channel_page = ChannelPage(driver, channel_id=channel_id)
    channel_page.open()
    yield channel_page
