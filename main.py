import sqlite3
import sys
import os

db  = sqlite3.connect("lapify.db")

csr = db.cursor()

csr.execute("CREATE TABLE IF NOT EXISTS Students (reg_no, full_name, email , phone_number ,  school, department )")
csr.execute("CREATE TABLE IF NOT EXISTS Laptops (serial_no,  laptop_model, laptop_colour)")
csr.execute("CREATE TABLE IF NOT EXISTS Logs(log_id, laptop_id, reg_no, event, timestamp)")

class Student:
    def __init__(self, db_connection, db_cursor):
        self.db = db_connection
        self.csr = db_cursor

    def get_student_details(self):
        print("......ENTER STUDENT DETAILS....")
        reg_no = input("Enter Registration Number: ").strip()
       

        if len(reg_no) != 6:
            print("Invalid registration number!", file = sys.stderr)
            return None

        name  = input("Enter Full Names: ").strip()
        email = input("Enter student email: ").strip()
        phone_number = input("Enter Phone Number: ").strip()
        school = input("Enter School: ").strip()
        department = input("Enter Department: ").strip()

        self.csr.execute("INSERT INTO Students VALUES (?, ?, ?, ?, ?, ?)", (reg_no, name, phone_number, email,   school, department))
        self.db.commit()
        print("Student details saved Successfully...")

    def get_laptop_details(self):
        print("....ENTER LAPTOP DETAILS...")
        serial_no = input("Enter Laptop Serial Number: ").strip()
       # owner_reg_no = 
        laptop_model = input("Enter Laptop Model: ").strip()
        laptop_colour = input("Enter Laptop colour:").strip()
        
        self.csr.execute("INSERT INTO Laptops VALUES (?, ?, ?)", (serial_no, laptop_model, laptop_colour))
        self.db.commit()
        print("Laptop details have been Successfully Updated...")
        
        


registry = Student(db, csr)

while True:
    registry.get_student_details()

    choice = input("Want to keep adding records? (y/n): ")

    if choice != 'y':
     print("End of File")
     break

db.close()


