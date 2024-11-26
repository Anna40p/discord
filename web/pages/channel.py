from dataclasses import dataclass
from pathlib import Path
from time import sleep
from typing import Literal
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from web.pages.base import BasePage


@dataclass
class Mention:
    type: Literal["user", "role"]
    id: str


class ChannelPage(BasePage):
    channel_id: str

    def __init__(self, driver: WebDriver, channel_id: str):
        super().__init__(driver)
        self.channel_id = channel_id

    @property
    def path(self):
        return f"channels/{self.channel_id}"

    def message_input_locator(self):
        return By.XPATH, '//div[@role="textbox"]'

    def save_edited_message_locator(self):
        return By.LINK_TEXT, "сохранить"

    def attachment_input_locator(self):
        return By.XPATH, '//div[contains(@class, "uploadDropModal")]'

    # def message_list_locator(self):
    #     return By.XPATH, '//ol[@data-list-id="chat-messages"]'

    def message_by_text_locator(self, text: str):
        return (
            By.XPATH,
            f'//li[contains(@class, "messageListItem") and .//div[contains(@id, "message-content")]//span[normalize-space(text())="{text}"]]',
        )

    def message_text_locator(self):
        return (
            By.XPATH,
            '//div[contains(@id, "message-content")]/span',
        )

    def message_by_element_id_locator(self, id: str):
        return (
            By.XPATH,
            f'//li[@id="{id}"]',
        )

    def message_user_mention_locator(self):
        return By.XPATH, '//span[contains(@class, "mention")]'

    def message_role_mention_locator(self):
        return By.XPATH, '//span[contains(@class, "roleMention")]//span'

    def message_edited_locator(self):
        return (
            By.XPATH,
            '//div[contains(@id, "message-content")]//span[contains(@class, "timestamp")]',
        )

    def message_menu_button_locator(self):
        return (
            By.XPATH,
            '//div[contains(@class, "buttonContainer")]/div/div/div[last()]',
        )

    def edit_message_button_locator(self):
        return By.XPATH, '//*[@id="message-actions-edit"]'

    def add_message_recent_reaction_button_locator(self, id: int):
        if not (0 <= id <= 3):
            raise ValueError("id must be between 0 and 3(inclusive)")
        return By.XPATH, f'//div[@id="message-actions-quickreact-{id}"]'

    def message_reactions_locator(self, text: str):
        return (By.XPATH, '//div[contains(@class, "reactionInner")]')

    def delete_message_button_locator(self):
        return By.XPATH, '//*[@id="message-actions-delete"]'

    def delete_message_confirm_button_locator(self):
        return By.XPATH, '//button[@type="submit"]'

    def add_attachment(self, path: str):
        attachment_input = self.wait_for_element(self.attachment_input_locator())
        sleep(1)
        attachment_input.send_keys(path)
        sleep(1)

    def send_message(
            self,
            text: str,
            mentions: list[Mention] = [],
            attachments: list[Path] = [],
    ):
        message_input = self.wait_for_element(self.message_input_locator())
        message_input.send_keys(text)
        sleep(1)
        for mention in mentions:
            message_input.send_keys(Keys.SPACE)
            sleep(1)
            message_input.send_keys(mention.id)
            sleep(1)
            if mention.type == "role":
                message_input.send_keys(Keys.DOWN)
                sleep(1)
            message_input.send_keys(Keys.ENTER)
            sleep(1)

        if len(attachments) > 0:
            attachment_input = self.wait_for_element(self.attachment_input_locator())
            for attachment in attachments:
                attachment_input.send_keys(str(attachment.absolute()))

        message_input.send_keys(Keys.ENTER)

    def open_message_menu_by_id(self, id: str):
        message = self.wait_for_element(self.message_by_element_id_locator(id=id))
        ActionChains(self.driver).click().move_to_element(message).click().perform()
        sleep(1)
        message_menu_button = self.wait_for_element(self.message_menu_button_locator())
        message_menu_button.click()

    def edit_message_by_id(self, id: str, text: str):
        self.open_message_menu_by_id(id)
        edit_message_button = self.wait_for_element(self.edit_message_button_locator())
        ActionChains(self.driver).move_to_element(edit_message_button).perform()
        sleep(1)
        edit_message_button.click()
        message_input = self.wait_for_element(self.message_input_locator())
        sleep(1)
        message_input.send_keys(Keys.CONTROL + 'a')
        message_input.send_keys(Keys.BACKSPACE)
        message_input.send_keys(text)
        message_input.send_keys(Keys.ENTER)
        sleep(2)

    def delete_message_by_id(self, id: str):
        self.open_message_menu_by_id(id)
        delete_message_button = self.wait_for_element(
            self.delete_message_button_locator()
        )
        ActionChains(self.driver).move_to_element(delete_message_button).perform()
        sleep(1)
        delete_message_button.click()

        self.wait_for_element(self.delete_message_confirm_button_locator()).click()

    def get_message_by_text(self, text: str) -> WebElement:
        return self.wait_for_element(self.message_by_text_locator(text=text))

    def get_message_by_element_id(self, id: str) -> WebElement | None:
        return self.find_element(self.message_by_element_id_locator(id=id))

    def get_message_text(self, message: WebElement) -> str:
        return message.find_element(*self.message_text_locator()).text

    def is_message_edited(self, message: WebElement) -> bool:
        return message.find_element(*self.message_edited_locator()).is_displayed()

    def get_message_user_mentions(self, message: WebElement) -> list[WebElement]:
        return message.find_elements(*self.message_user_mention_locator())

    def get_message_role_mentions(self, message: WebElement) -> list[WebElement]:
        return message.find_elements(*self.message_role_mention_locator())
