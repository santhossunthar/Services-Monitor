import psutil

class RabbitMQService():
    def getStatus():
        for process in psutil.process_iter(["pid", "name"]):
            if "rabbitmq" in process.info["name"].lower():
                return True
        return False