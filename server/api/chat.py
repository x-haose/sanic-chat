from sanic import Blueprint, Request
from sanic_api.api.exception import ServerException
from sanic_ext import cors

from server.api.validator import ChatApi, FreeLineApi
from server.client.base import ChatReqtest
from server.entity.line_enum import LineEnum
from server import client

blueprint = Blueprint("chat", url_prefix="/")
blueprint.ctx.desc = "聊天"


@blueprint.post(uri='free_chat')
@cors(origin="*")
async def free_chat(request: Request, api: ChatApi):
    """
    免费线路聊天
    """
    line_dict = {line.name: line for line in LineEnum}
    line: LineEnum = line_dict.get(api.json_req.line_name)
    if not line:
        raise ServerException(message="Invalid Line")

    response = await request.respond()
    line_class = getattr(client, line.value)
    messages = [msg.dict() for msg in api.json_req.messages]
    chat: ChatReqtest = line_class(messagss=messages)
    async for msg in chat.request():
        await response.send(msg)
    await response.eof()


@blueprint.get(uri='free_line')
@cors(origin="*")
async def free_line(_, api: FreeLineApi):
    """
    获取免费线路
    """
    for line in LineEnum:
        api.resp.line_name = line.name
        api.resp.add_data()
    return api.json_resp()
