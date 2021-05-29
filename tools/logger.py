import logging


def custom_logger(logger_level):
    "Log de feedback do processo"

    logger = logging.getLogger("logfile.log")
    logger.setLevel(logging.DEBUG)
    c_handler = logging.StreamHandler()
    c_handler.setLevel(logger_level)

    formatter = logging.Formatter("[%(asctime)s] [ALPHA_VANTAGE_API] [%(levelname)s] [%(message)s]",
                                  datefmt="%Y/%m/%d %I:%M:%S %p")

    c_handler.setFormatter(formatter)

    if (logger.hasHandlers()):
        logger.handlers.clear()
    logger.addHandler(c_handler)
    return logger
