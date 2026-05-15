import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Students (name, regNo, laptopModel, serialNumber )")

class Student:
    def __init__(self, db_connection, db_cursor):
        self.conn = db_connection
        self.cursor = db_cursor

    def get_student_details(self):
        name = input("Enter Name: ")
        regNo = input("Enter Regitstration Number: ")
        laptopModel = input("Enter Laptop Model: ")
        serialNumber = input("Enter serial Number: ")

        self.cursor.execute("INSERT INTO Students VALUES (?, ?, ?, ?)", (name, regNo, laptopModel, serialNumber))
        self.conn.commit()
        print("Student details saved Successfully!")


registry = Student(conn, cursor)

while True:
    registry.get_student_details()

    choice = input("Want to keep adding records? (y/n): ")

    if choice != 'y':
     print("End of File")
     break

conn.close()
