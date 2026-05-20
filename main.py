import sqlite3

db  = sqlite3.connect("lapify.db")

csr = db.cursor()

csr.execute("CREATE TABLE IF NOT EXISTS Students (reg_no, full_name, email , phone_number ,  school, department )")
csr.execute("CREATE TABLE IF NOT EXISTS Laptops (laptop_id, serial_no, owner_reg_no,  laptop_model, laptop_colour)")
csr.execute("CREATE TABLE IF NOT EXISTS Logs(log_id, laptop_id, reg_no, event, timestamp)")

class Student:
    def __init__(self, db_connection, db_cursor):
        self.db = db_connection
        self.csr = db_cursor

    def get_student_details(self):
        reg_no = input("Enter Registration Number: ")
        name  = input("Enter Full Names: ")
        email = input("Enter student email: ")
        phone_number = input("Enter Phone Number: ")
        school = input("Enter School: ")
        department = input("Enter Department: ")

        self.csr.execute("INSERT INTO Students VALUES (?, ?, ?, ?, ?, ?)", (reg_no, name, phone_number, email,   school, department))
        self.db.commit()
        print("Student details saved Successfully!")

    def get_laptop_details(self):
        laptop_id 
        


registry = Student(db, csr)

while True:
    registry.get_student_details()

    choice = input("Want to keep adding records? (y/n): ")

    if choice != 'y':
     print("End of File")
     break

db.close()


