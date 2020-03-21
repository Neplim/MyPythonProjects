import pyodbc

server = "HomeSQLServer"
database = "TestDb"
login = "sa"
password = "A173042a"
connection = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+login+';PWD='+password)
cursor = connection.cursor()
SQLQuery1 = "SELECT * FROM dbo.NewTestID;"
cursor.execute(SQLQuery1)
SQLQuery2 = "SELECT * FROM dbo.NewTestID"
cursor.execute(SQLQuery2)
cursor.commit()
connection.close()