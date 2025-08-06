from loguru import logger
import sys

def get_logger():
    logger.remove(0)

    logger.add(sys.stdout, format="[ <cyan>{level}</cyan> ] <cyan>{message}</cyan>", level="DEBUG", filter= lambda l: l['level'].name == "DEBUG")
    logger.add(sys.stderr, format="[ <red>{level}</red> ] <red>{message}</red>", level="ERROR", filter= lambda l: l['level'].name == "ERROR")
    logger.add(sys.stdout, format="[ <green>{level}</green> ] <green>{message}</green>", level="INFO", filter= lambda l: l['level'].name == "INFO")
    logger.add(sys.stderr, format="[ <yellow>{level}</yellow> ] <yellow>{message}</yellow>", level="WARNING", filter= lambda l: l['level'].name == "WARNING")
    logger.add(sys.stderr, format="[ <red><b>{level}</b></red> ] <red><b>{message}</b></red>", level="CRITICAL", filter= lambda l: l['level'].name == "CRITICAL")

    return logger
