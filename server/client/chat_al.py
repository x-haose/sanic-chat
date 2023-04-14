import asyncio

from cryptography.hazmat.primitives import hashes

from server.client.chat_muspimerol import ChatMuspimerol


class ChatAils(ChatMuspimerol):
    url = "https://ai.ls/api/generate"

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
        secret_key = "Na3dx_(?qx32l}ep?#:8:mo44;7W\\2W.:nxm"
        sign_text = f"{timestamp}:{message}:{secret_key}:{len(message)}"
        digest = hashes.Hash(hashes.SHA256())
        digest.update(sign_text.encode('utf-8'))
        signature = digest.finalize()
        return signature.hex()


async def main():
    chat = ChatMuspimerol(messagss=[{"role": 'user', "content": "自我介绍"}])
    await chat.request()


if __name__ == '__main__':
    asyncio.run(main())
