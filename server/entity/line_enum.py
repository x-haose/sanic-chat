from sanic_api.enum import EnumBase, EnumField


class LineEnum(EnumBase):
    """
    免费线路的枚举
    """
    LINE_1 = EnumField('ChatAils', desc="免费线路一")
    LINE_2 = EnumField('ChatMuspimerol', desc="免费线路二")
    LINE_3 = EnumField('ChatOhtoai', desc="免费线路三")
