CHANNEL_ID = "1305528721360294001"
BOT_ID = '1286609819137998883'


def test_send_message(client):
    content = "Test message"
    response = client.send_message(CHANNEL_ID, content)
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["content"] == content


def test_send_message_with_mention(client):
    content = "Test message with mention"
    mentions = ["anna_v.v_26918"]
    response = client.send_message(CHANNEL_ID, content, mentions=mentions)
    assert response.status_code == 200
    data = response.json()
    assert f"<@{mentions[0]}>" in data["content"]


def test_send_message_max_length(client):
    content = "a" * 2001
    response = client.send_message(CHANNEL_ID, content)
    assert response.status_code == 400


def test_get_message(client):
    content = "Test message for retrieval"
    send_response = client.send_message(CHANNEL_ID, content)
    assert send_response.status_code == 200
    message_id = send_response.json()["id"]

    get_response = client.get_message(CHANNEL_ID, message_id)
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["content"] == content
    assert data["id"] == message_id


def test_get_messages(client):
    response = client.get_messages(CHANNEL_ID, limit=10)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) <= 10


def test_edit_message(client):
    original_content = "Original message"
    send_response = client.send_message(CHANNEL_ID, original_content)
    assert send_response.status_code == 200
    message_id = send_response.json()["id"]

    edited_content = "Edited message"
    edit_response = client.edit_message(CHANNEL_ID, message_id, edited_content)
    assert edit_response.status_code == 200, edit_response.text
    edited_data = edit_response.json()
    assert edited_data["content"] == edited_content
    assert edited_data["edited_timestamp"] is not None


def test_delete_message(client):
    content = "Message to be deleted"
    send_response = client.send_message(CHANNEL_ID, content)
    assert send_response.status_code == 200
    message_id = send_response.json()["id"]

    delete_response = client.delete_message(CHANNEL_ID, message_id)
    assert delete_response.status_code == 204

    assert client.get_message(CHANNEL_ID, message_id).status_code == 404


def test_add_reaction(client):
    content = "Message for reaction"
    send_response = client.send_message(CHANNEL_ID, content)
    assert send_response.status_code == 200
    message_id = send_response.json()["id"]

    emoji = "%F0%9F%91%8D"
    reaction_response = client.add_reaction(CHANNEL_ID, message_id, emoji)
    assert reaction_response.status_code == 204


def test_remove_reaction(client):
    content = "Message for removing reaction"
    send_response = client.send_message(CHANNEL_ID, content)
    assert send_response.status_code == 200
    message_id = send_response.json()["id"]

    emoji = "%F0%9F%91%8D"
    client.add_reaction(CHANNEL_ID, message_id, emoji)

    remove_response = client.remove_reaction(CHANNEL_ID, message_id, emoji, BOT_ID)
    assert remove_response.status_code == 204


def test_add_multiple_reactions(client):
    content = "Message for multiple reactions"
    send_response = client.send_message(CHANNEL_ID, content)
    assert send_response.status_code == 200
    message_id = send_response.json()["id"]

    emojis = [
        "%F0%9F%91%8D",
        "%F0%9F%91%8E",
        "%F0%9F%98%84",
    ]
    for emoji in emojis:
        reaction_response = client.add_reaction(CHANNEL_ID, message_id, emoji)
        assert reaction_response.status_code == 204


def test_get_reactions(client):
    content = "Message for getting reactions"
    send_response = client.send_message(CHANNEL_ID, content)
    assert send_response.status_code == 200
    message_id = send_response.json()["id"]

    emoji = "%F0%9F%91%8D"
    client.add_reaction(CHANNEL_ID, message_id, emoji)

    get_reactions_response = client.get_reactions(CHANNEL_ID, message_id, emoji)
    assert get_reactions_response.status_code == 200
    reactions_data = get_reactions_response.json()
    assert isinstance(reactions_data, list)
    assert len(reactions_data) > 0
