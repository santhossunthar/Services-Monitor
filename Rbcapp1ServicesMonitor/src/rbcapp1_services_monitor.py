from httpd_service import HttpdService
from postqresql_service import PostgreSqlService
from rabbitmq_service import RabbitMQService
from json_file_handler import JsonFileHandler

def run():
    try:
        while True:
            httpdServiceStatus = HttpdService.getStatus()
            postgreSqlServiceStatus = PostgreSqlService.getStatus()
            rabbitMQServiceStatus = RabbitMQService.getStatus()

            if (httpdServiceStatus and postgreSqlService and rabbitMQService):
                applicationStatus = "UP"
            else:
                applicationStatus = "DOWN"

            httpdServiceLog = JsonFileHandler.createLog("httpd", httpdServiceStatus)
            postgreSqlServiceLog = JsonFileHandler.createLog("postgres", postgreSqlServiceStatus)
            rabbitMQServiceLog = JsonFileHandler.createLog("rabbitmq", rabbitMQServiceStatus)

            JsonFileHandler.createFile("httpd", httpdServiceLog)
            JsonFileHandler.createFile("postgres", postgreSqlServiceLog)
            JsonFileHandler.createFile("rabbitmq", rabbitMQServiceLog)
    except Exception as e:
        print(e)

if __name__=="__main__":
    print(run())
