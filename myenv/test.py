import os;
import pyodbc as pd
class main():
    def __init__(self):
        print(os.getcwd())
        with open('./myenv/sample.sql','r') as sqlfile:
            print(sqlfile.read())
            print(pd.drivers())
            try:
                #SQL Server Native Client 11.0
                #pd.connect(connstring='Driver:{SQL Server Native Client 11.0};Server=tcp:itsfidev.database.windows.net,1433;Database=sample;Uid=admin123;Pwd=Ramco@1234;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
                #cnxn = pd.connect('DSN=newdsn;UID=admin123;PWD=Ramco@1234')
                cnxn = pd.connect('DSN=newdsn;UID=admin123;PWD=Ramco@1234')
            except Exception as err:
                print(err)
if __name__=='__main__':
    main()