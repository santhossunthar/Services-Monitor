from httpd_service import HttpdService
from postqresql_service import PostgreSqlService
from rabbitmq_service import RabbitMQService
from json_file_handler import JsonFileHandler

def run():
    serviceLog = JsonFileHandler.createFile(
        httpd=HttpdService.getStatus(), 
        postgres=PostgreSqlService.getStatus(), 
        rabbitmq=RabbitMQService.getStatus()
    )

    return serviceLog

if __name__=="__main__":
    print(run())
