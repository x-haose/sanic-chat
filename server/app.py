from sanic import Sanic
from sanic.log import logger
from sanic_api.enum import RunModeEnum
from sanic_cors import CORS
from sanic_ext import Extend

from server.settings import settings
from sanic_api import init_api
from sanic_api.utils import auto_blueprint


async def main_process_start(sanic_app: Sanic):
    """
    主进程启动之前调用
    Args:
        sanic_app: application

    Returns:

    """
    sanic_cfg = settings.sanic.dict(by_alias=True)
    sanic_app.config.update(sanic_cfg)
    logger.info(f"{sanic_app.name} 服务启动")


def app_factory():
    """
    app 工厂方法
    Returns:

    """
    app = Sanic(name="test", configure_logging=False)
    app.config.CORS_ORIGINS = '*'
    app.main_process_start(main_process_start)
    auto_blueprint(app, "api")
    init_api(app)

    return app


if __name__ == '__main__':
    app_factory().run(
        single_process=True,
        host=settings.host,
        port=settings.port,
    )
