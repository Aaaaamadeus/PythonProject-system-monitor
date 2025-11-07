from loguru import logger
logger.add("monitor.log",rotation="5 MB",level="INFO")

