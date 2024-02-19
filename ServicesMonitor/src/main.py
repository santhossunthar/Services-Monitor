from httpd_service import HttpdService
from postqresql_service import PostgreSqlService
from rabbitmq_service import RabbitMQService
from json_file_handler import JsonFileHandler

def main():
    try:
        while True:
            httpdServiceStatus = HttpdService.getStatus()
            postgreSqlServiceStatus = PostgreSqlService.getStatus()
            rabbitMQServiceStatus = RabbitMQService.getStatus()
    except Exception as e:
        pass

if __name__=="__main__":
    main()
