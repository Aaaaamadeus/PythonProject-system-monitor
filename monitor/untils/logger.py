from loguru import logger
import os

LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),"..", "logs")
os.makedirs(LOG_DIR, exist_ok=True)

LOG_PATH = os.path.join(LOG_DIR, "monitor.log")
logger.add(
    LOG_PATH,
    rotation="10 MB",    #单个日志大小，大于将切分
    retention="7 days",  #日志保留时间
    encoding="utf-8",    #使用UTF-8编码
    level="INFO",
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level: <8}</level> | "
           "<cyan>{name}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    )        #日志级别

__all__ = ["logger"]
