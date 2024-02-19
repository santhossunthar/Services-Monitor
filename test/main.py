import logging.config
import pathlib
import json

logger = logging.getLogger(__name__)

def main():
    lc = pathlib.Path("log_config.json")

    with open(lc) as c:
        config = json.load(c)

    logging.config.dictConfig(config)

    logger.info("info msg", extra={"service_name":"httpd", "service_status": "UP"})


if __name__=="__main__":
    main()