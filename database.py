import sqlite3

def getDB():
    database_file = 'test.db'  #change to lapify.db
    con = sqlite3.connect(database_file)
    return con, con.cursor()

def createStudentTable(first_name, last_name, ):