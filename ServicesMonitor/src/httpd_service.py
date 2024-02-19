import psutil
import logging
import socket
from datetime import datetime

timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
fileName = f"httpd-status-@{timestamp}.json"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('{ "service_name":"httpd", "service_status":"%(message)s", ' + ' "service_host":"{}"'.format(socket.gethostname()) + '}')
handler = logging.FileHandler(fileName)
handler.setFormatter(formatter)
logger.addHandler(handler)

class HttpdService():
    def getStatus(self):
        for process in psutil.process_iter(["pid", "name"]):
            if "httpd" in process.info["name"].lower():
                logger.info("UP")
                return True
        logger.info("DOWN")

