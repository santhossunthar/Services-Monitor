from httpd_service import HttpdService
from postqresql_service import PostgreSqlService

if __name__=="__main__":
    print(HttpdService.getStatus())
    print(PostgreSqlService.getStatus())
