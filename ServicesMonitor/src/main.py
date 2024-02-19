from httpd_service import HttpdService
from postqresql_service import PostgreSqlService
from rabbitmq_service import RabbitMQService
import logging.config
import pathlib
import json

def main():
    try:
        while True:
            httpdServiceStatus = HttpdService.getStatus()
            postgreSqlServiceStatus = PostgreSqlService.getStatus()
            rabbitMQServiceStatus = RabbitMQService.getStatus()
    except Exception as exc:
        logger.error(exc)

if __name__ =="__main__":
    logger = logging.getLogger(__name__)
    logConfigFile = pathlib.Path("log_config.json")

    with open(logConfigFile) as logConfig:
        config = json.load(logConfig)

    logging.config.dictConfig(config)
    main()
