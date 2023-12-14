from httpd_service import HttpdService
from postqresql_service import PostgreSqlService
from rabbitmq_service import RabbitMQService

if __name__=="__main__":
    print(HttpdService.getStatus())
    print(PostgreSqlService.getStatus())
    print(RabbitMQService.getStatus())
