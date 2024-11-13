from loguru import logger

logger.add('logs/data.log', rotation='10 mb', level='DEBUG')

def get_logger():
    return logger