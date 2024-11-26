from pathlib import Path
from typing import Any, Dict, List, Optional

import httpx
from httpx import Client, Response


class DiscordClient:
    BASE_URL = "https://discord.com/api/v10"

    token: str
    headers: dict[str, str]

    def __init__(self, token: str):
        self.token = token
        self.headers = {
            "Authorization": f"Bot {self.token}",
            "Content-Type": "application/x-www-form-urlencoded",
        }

    def send_message(
            self,
            channel_id: str,
            content: str,
            mentions: Optional[List[str]] = None,
    ) -> Response:
        url = f"{self.BASE_URL}/channels/{channel_id}/messages"

        data = {"content": content}

        if mentions:
            for mention in mentions:
                data["content"] += f" <@{mention}>"

        with Client() as client:
            response = client.post(url, headers=self.headers, data=data)

            return response

    def delete_message(self, channel_id: str, message_id: str) -> Response:
        url = f"{self.BASE_URL}/channels/{channel_id}/messages/{message_id}"
        with Client() as client:
            response = client.delete(url, headers=self.headers)
            return response

    def get_messages(
            self,
            channel_id: str,
            limit: int = 50,
            before: Optional[str] = None,
            after: Optional[str] = None,
            around: Optional[str] = None,
    ) -> Response:
        url = f"{self.BASE_URL}/channels/{channel_id}/messages"
        params: Dict[str, Any] = {"limit": limit}

        if before:
            params["before"] = before
        if after:
            params["after"] = after
        if around:
            params["around"] = around

        with Client() as client:
            response = client.get(url, headers=self.headers, params=params)
            return response

    def get_message(self, channel_id: str, message_id: str) -> Response:
        url = f"{self.BASE_URL}/channels/{channel_id}/messages/{message_id}"
        with Client() as client:
            response = client.get(url, headers=self.headers)
            return response

    def add_reaction(self, channel_id: str, message_id: str, emoji: str) -> Response:
        url = f"{self.BASE_URL}/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me"
        with Client() as client:
            response = client.put(url, headers=self.headers)
            return response

    def remove_reaction(
            self, channel_id: str, message_id: str, emoji: str, user_id: str
    ) -> Response:
        url = f"{self.BASE_URL}/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/{user_id}"
        with Client() as client:
            response = client.delete(url, headers=self.headers)
            return response

    def edit_message(self, channel_id: str, message_id: str, content: str) -> Response:
        url = f"{self.BASE_URL}/channels/{channel_id}/messages/{message_id}"
        data = {"content": content}
        with Client() as client:
            response = client.patch(url, headers=self.headers, data=data)
            return response

    def get_reactions(self, channel_id: str, message_id: str, emoji: str) -> Response:
        url = f"{self.BASE_URL}/channels/{channel_id}/messages/{message_id}/reactions/{emoji}"
        with Client() as client:
            response = client.get(url, headers=self.headers)
            return response
