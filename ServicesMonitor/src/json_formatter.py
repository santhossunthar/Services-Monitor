import logging
import json
import datetime

class JSONFormatter(logging.Formatter):
    def __init__(self):
        super().__init__()

    def format(self, record):
        log_data = self.generateLogData(record)
        return json.dumps(log_data, default=str)

    def generateLogData(self, record):
        log_data = {
            "module": record.name,
            "level": record.levelname,
            "message": record.msg,
            "timestamp": datetime.datetime.fromtimestamp(record.created, tz=datetime.timezone.utc).isoformat()
        }

        if hasattr(record, "service_name"):
            log_data["service_name"] = record.service_name

        if hasattr(record, "service_status"):
            log_data["service_status"] = record.service_status

        if hasattr(record, "service_host"):
            log_data["service_host"] = record.service_host

        if record.exc_info is not None:
            log_data["exc_info"] = self.formatException(record.exc_info)

        if record.stack_info is not None:
            log_data["stack_info"] = self.formatStack(record.stack_info)

        return log_data