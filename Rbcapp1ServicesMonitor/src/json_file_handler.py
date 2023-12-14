import json
import socket
from datetime import datetime
import os

class JsonFileHandler:
    def createLog(service, status):
            serviceLog = {
                "service_name": service,
                "service_status": status,
                "service_hostname": socket.gethostname(),
            }
         
            return json.dumps(serviceLog, indent=2)

    def createFile(service, serviceLog):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        folderName = "service_logs"
        fileName = f"{service}-status-@{timestamp}.json"

        if not os.path.exists(folderName):
            os.makedirs(folderName)
        
        with open(os.path.join(folderName, fileName), "w") as serviceLogFile:
            json.dump(serviceLog, serviceLogFile, indent=2)