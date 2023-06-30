import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def make_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    return logger
