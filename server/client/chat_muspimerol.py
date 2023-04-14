import asyncio
import time

from cryptography.hazmat.primitives import hashes

from server.client.base import ChatReqtest


class ChatMuspimerol(ChatReqtest):
    url = "https://chat.muspimerol.site/api/generate"

    def generate_data(self):
        """
        生成请求参数
        Returns:

        """
        timestamp = int(time.time() * 1000)
        sign = self.generate_signature(timestamp, self.messagss[-1]['content'] or '')
        data = {
            "messages": self.messagss,
            "pass": None,
            "time": timestamp,
            "sign": sign,
        }
        return data

    @staticmethod
    def generate_signature(timestamp, message: str) -> str:
        """
        生成签名
        Args:
            timestamp: 时间戳
            message: 消息

        Returns:
            返回签名
        """
        secret_key = "undefined"
        sign_text = f"{timestamp}:{message}:{secret_key}"
        digest = hashes.Hash(hashes.SHA256())
        digest.update(sign_text.encode('utf-8'))
        signature = digest.finalize()
        return signature.hex()


async def main():
    chat = ChatMuspimerol(messagss=[{"role": 'user', "content": "自我介绍"}])
    async for msg in chat.request():
        print(msg, end='')


if __name__ == '__main__':
    asyncio.run(main())
