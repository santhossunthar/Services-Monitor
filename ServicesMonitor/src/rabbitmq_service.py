import psutil
import logging.config
import socket
from datetime import datetime
import pathlib
import json

logger = logging.getLogger(__name__)

class RabbitmqService():
    def getStatus():
        for process in psutil.process_iter(["pid", "name"]):
            if "rabbitmq" in process.info["name"].lower():
                logger.info("UP", extra={"service_name": "rabbitmq", "service_host": socket.gethostname()})
                return True
        logger.critical("DOWN", extra={"service_name": "rabbitmq", "service_host": socket.gethostname()})