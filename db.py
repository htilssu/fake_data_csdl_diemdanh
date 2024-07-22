"""
Connects to a SQL database using pyodbc
"""

import pyodbc

SERVER = 'localhost'
DATABASE = 'QL_DiemDanh'
USERNAME = 'htilssu'
PASSWORD = 'Shuu@2004'

connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};Encrypt=yes;TrustServerCertificate=yes;Connection_Timeout=30;'

conn = pyodbc.connect(connectionString)

if conn is None:
    print("Error: Connection to database failed")

else:
    print("Connection to database successful")
    conn.close()

insert_student_query = "INSERT INTO Student (Id, Name, Email, Phone, Address, Birthday, Sex) VALUES (?,?,?, ?, ?, ?, ?)"
