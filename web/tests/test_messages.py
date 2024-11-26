from web.pages.channel import ChannelPage, Mention


class TestDiscordMessages:
    def test_message(self, channel_page: ChannelPage):
        text_to_send = "Test message"
        channel_page.send_message(text=text_to_send)
        assert channel_page.get_message_by_text(text_to_send).is_displayed()

    def test_message_with_user_mention(self, channel_page: ChannelPage):
        user_to_mention = "@BEE-diploma"
        mentions = [Mention(type="user", id=user_to_mention)]
        text_to_send = "Test message for user mention"

        channel_page.send_message(text=text_to_send, mentions=mentions)
        message = channel_page.get_message_by_text(text_to_send)

        message_user_mentions = channel_page.get_message_user_mentions(message)
        for expected_mention in mentions:
            assert any(
                expected_mention.id == message_mention.text
                for message_mention in message_user_mentions
            )

    def test_message_with_role_mention(self, channel_page: ChannelPage):
        role_to_mention = "@BEE-diploma"
        text_to_send = "Test message for role mention"
        mention = Mention(type="role", id=role_to_mention)
        channel_page.send_message(text=text_to_send, mentions=[mention])
        message = channel_page.get_message_by_text(text_to_send)

        message_role_mentions = channel_page.get_message_role_mentions(message)
        for expected_mention in [mention]:
            assert any(
                expected_mention.id == message_mention.text
                for message_mention in message_role_mentions
            )

    def test_edit_message(self, channel_page: ChannelPage):
        text_to_send = "Test before edit"
        text_to_edit = "Test after edit"

        channel_page.send_message(text=text_to_send)
        message = channel_page.get_message_by_text(text_to_send)
        message_id = message.get_attribute("id")
        assert message_id is not None, "Message ID not found"
        channel_page.edit_message_by_id(message_id, text_to_edit)
        edited_message = channel_page.get_message_by_text(text_to_edit)
        assert edited_message is not None, "Edited message not found"

        edited_message_text = channel_page.get_message_text(edited_message)
        assert edited_message_text == text_to_edit
        assert channel_page.is_message_edited(edited_message)

    def test_delete_message(self, channel_page: ChannelPage):
        text_to_send = "Test for deleting"

        channel_page.send_message(text=text_to_send)
        message = channel_page.get_message_by_text(text_to_send)
        message_id = message.get_attribute("id")
        assert message_id is not None, "Message ID not found"

        channel_page.delete_message_by_id(message_id)
        assert (
                channel_page.get_message_by_element_id(message_id) is None
        ), "Message not deleted"
