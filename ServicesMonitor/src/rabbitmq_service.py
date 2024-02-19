import psutil
import logging
import socket
from datetime import datetime

timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
fileName = f"rabbitmq-status-@{timestamp}.json"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('{ "service_name":"rabbitmq", "service_status":"%(message)s", ' + ' "service_host":"{}"'.format(socket.gethostname()) + '}')
handler = logging.FileHandler(fileName)
handler.setFormatter(formatter)
logger.addHandler(handler)

class RabbitMQService():
    def getStatus():
        for process in psutil.process_iter(["pid", "name"]):
            if "rabbitmq" in process.info["name"].lower():
                logger.info("UP")
        logger.info("DOWN")