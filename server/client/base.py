from abc import ABC

from httpx import AsyncClient


class ChatReqtest(ABC):
    url = ""

    def __init__(self, messagss: list[dict]):
        self.messagss = messagss

    async def request(self):
        data = self.generate_data()
        headers = self.generate_headers()
        async with AsyncClient(proxies="http://127.0.0.1:8087", timeout=10) as client:
            async with client.stream("POST", self.url, json=data, headers=headers) as response:
                async for chunk in response.aiter_text():
                    yield chunk

    def generate_headers(self):
        """
        生成请求头
        Returns:

        """
        return {}

    def generate_data(self):
        """
        生成请求参数
        Returns:

        """
        data = {
            "messages": self.messagss,
        }
        return data
