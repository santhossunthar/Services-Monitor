import logging
import logging.handlers
import time
import requests

logger = logging.getLogger(__name__)

class BufferedHttpHandler(logging.handlers.HTTPHandler):
    def __init__(self, buffer_capacity=100, flush_interval=60, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.buffer_capacity = buffer_capacity
        self.flush_interval = flush_interval
        self.buffer = []
        self.last_flush_time = time.time()

    def emit(self, record):
        log_entry = self.format(record)
        self.buffer.append(log_entry)

        if len(self.buffer) >= self.buffer_capacity or time.time() - self.last_flush_time >= self.flush_interval:
            self.flush_buffer()

    def flush_buffer(self):
        if self.buffer:
            try:
                logs = '\n'.join(self.buffer)
                response = requests.post(f"{self.host}{self.url}", logs, headers={
                    "Content-Type": "application/json",
                })
                response.raise_for_status()
            except requests.RequestException as e:
                logger.error(f"Error sending logs: {e}")

            self.buffer = []
            self.last_flush_time = time.time()
