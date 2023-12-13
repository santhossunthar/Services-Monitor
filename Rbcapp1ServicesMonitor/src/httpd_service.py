import psutil

class HttpdService():
    def getStatus():
        for process in psutil.process_iter(["pid", "name"]):
            if "httpd" in process.info["name"].lower():
                return True
        return False
