import os;
import pyodbc as pd
class main():
    def __init__(self):
        print(os.getcwd())
        with open('./myenv/sample.sql','r') as sqlfile:
            qry=sqlfile.read()
            #print(pd.drivers())
            try:
                #SQL Server Native Client 11.0
                #pd.connect(connstring='Driver:{SQL Server Native Client 11.0};Server=tcp:itsfidev.database.windows.net,1433;Database=sample;Uid=admin123;Pwd=Ramco@1234;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
                #cnxn = pd.connect('DSN=newdsn;UID=admin123;PWD=Ramco@1234')
                conn = pd.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER=itsfidev.database.windows.net;'
                      'DATABASE=sample;UID=admin123;PWD=Ramco@1234;')
                print(qry)
                cursor = conn.cursor()
                with conn:
                    cursor.execute(qry)
                    rows = cursor.fetchall()
            except Exception as err:
                print(err)
if __name__=='__main__':
    main()