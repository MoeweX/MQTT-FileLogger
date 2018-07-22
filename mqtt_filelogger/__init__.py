# coding=utf-8

from logging.config import dictConfig
import toml
from mqtt_filelogger.Config import Config
import threading

# enable logging
dictConfig(toml.load("../resources/logging.toml"))

# load configuration
CONFIG = Config("../resources/config.toml")


# Synchronize function
def synchronized(func):
    func.__lock__ = threading.Lock()

    def synced_func(*args, **kws):
        with func.__lock__:
            return func(*args, **kws)

    return synced_func
