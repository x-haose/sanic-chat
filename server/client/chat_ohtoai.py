import asyncio

from server.client.base import ChatReqtest


class ChatOhtoai(ChatReqtest):
    url = "https://chat.ohtoai.com/api/chat-stream"

    def generate_headers(self):
        return {"path": "v1/chat/completions"}

    def generate_data(self):
        data = {
            "messages": self.messagss,
            "stream": True,
            "model": "gpt-3.5-turbo",
            "temperature": 1,
            "presence_penalty": 0
        }
        return data


async def main():
    chat = ChatOhtoai(messagss=[{"role": 'user', "content": "自我介绍"}])
    await chat.request()


if __name__ == '__main__':
    asyncio.run(main())
