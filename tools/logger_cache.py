import logging
import inspect


def custom_logger(logger_level):
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    c_handler = logging.StreamHandler()
    c_handler.setLevel(logger_level)

    formatter = logging.Formatter("[%(asctime)s] [ALPHA_VANTAGE_API] [%(levelname)s] [%(message)s]",
                                    datefmt="%Y/%m/%d %I:%M:%S %p")
    
    c_handler.setFormatter(formatter)
    logger.addHandler(c_handler)
    return logger


