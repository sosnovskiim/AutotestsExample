import logging
import re

class SecretMasker(logging.Filter):
    def filter(self, record):
        msg = record.getMessage()
        msg = re.sub(r'7SKD9z', '***', msg)
        msg = re.sub(r'sosnovskiim@ya\.ru', 's***@ya.ru', msg)
        record.msg = msg
        record.args = ()
        return True

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
        handler.setFormatter(formatter)
        handler.addFilter(SecretMasker())
        logger.addHandler(handler)
    return logger
