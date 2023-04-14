from pydantic import BaseModel, Field
from sanic_api.api.model import ListRespModel


class MessageData(BaseModel):
    """
    消息的数据模型
    """
    role: str = Field('角色')
    content: str = Field('内容')


class ChatReqModel(BaseModel):
    """
    聊天请求体
    """
    line_name: str = Field(title='线路名称')
    messages: list[MessageData] = Field(title='消息列表')


class FreeLineRespModel(ListRespModel):
    """
    获取免费线路响应体
    """
    line_name: str = Field(title='线路名称')
