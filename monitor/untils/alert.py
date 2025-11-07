from loguru import logger

def the_alert(message):
    logger.warning(f"⚠ ALERT:{message}")
