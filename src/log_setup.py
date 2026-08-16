import logging
from logging.handlers import RotatingFileHandler

from config import LOG_ARQUIVO, LOG_NIVEL


def configurar():
    LOG_ARQUIVO.parent.mkdir(parents=True, exist_ok=True)

    handler = RotatingFileHandler(
        LOG_ARQUIVO, maxBytes=5 * 1024 * 1024, backupCount=5, encoding="utf-8"
    )
    handler.setFormatter(logging.Formatter(
        "%(asctime)s %(levelname)-8s %(name)s | %(message)s"
    ))

    logging.basicConfig(level=LOG_NIVEL, handlers=[handler, logging.StreamHandler()])