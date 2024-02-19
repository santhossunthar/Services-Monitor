import psutil
import logging.config
import socket
from datetime import datetime
import pathlib
import json

logger = logging.getLogger(__name__)
logConfigFile = pathlib.Path("log_config.json")

with open(logConfigFile) as logConfig:
    config = json.load(logConfig)

logging.config.dictConfig(config)

class HttpdService():
    def getStatus():
        for process in psutil.process_iter(["pid", "name"]):
            if "httpd" in process.info["name"].lower():
                logger.info("UP", extra={"service_name": "httpd", "service_host": socket.getHostName()})
                return True
        logger.critical("DOWN", extra={"service_name": "httpd", "service_host": socket.getHostName()})

