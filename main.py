import logging

logger = logging.getLogger(__name__)
log_format: str = "%(asctime)s [%(levelname)s] %(message)s"
logging.basicConfig(format=log_format, level=logging.INFO)

logger.info("Start")
try:
    num: int = 1 / 0
except ZeroDivisionError as e:
    logger.error(e)
logger.info("Finish")
