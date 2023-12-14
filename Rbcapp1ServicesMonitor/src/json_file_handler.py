import json

class JsonFileHandler:
    def createFile(**services):
        for service in services:
            serviceLog = {
                "service_name": services["httpd"],
                "service_status": services["postgres"],
                "service_hostname": services["rabbitmq"],
            }
         
            return json.dumps(serviceLog, indent=2)