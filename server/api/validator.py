from sanic_api.api import API

from server.entity.api_model import ChatReqModel, FreeLineRespModel


class ChatApi(API):
    json_req: ChatReqModel
    resp: str


class FreeLineApi(API):
    resp: FreeLineRespModel
