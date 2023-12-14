import psutil

class PostgreSqlService():
    def getStatus():
        for process in psutil.process_iter(["pid", "name"]):
            if "postqre" in process.info["name"].lower():
                return True
        return False

