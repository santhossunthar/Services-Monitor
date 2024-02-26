from httpd_service import HttpdService
from postgres_service import PostgresService
from rabbitmq_service import RabbitmqService
import logging.config
import pathlib
import json

logger = logging.getLogger(__name__)

def setupLogging():
    logConfigFile = pathlib.Path("log_config.json")
    with open(logConfigFile) as logConfig:
        config = json.load(logConfig)
    logging.config.dictConfig(config)

def main():
    try:
        while True:
            httpdServiceStatus = HttpdService.getStatus()
            postgresServiceStatus = PostgresService.getStatus()
            rabbitmqServiceStatus = RabbitmqService.getStatus()
    except Exception as exc:
        logger.error(exc)

if __name__ =="__main__":
    setupLogging()
    main()
