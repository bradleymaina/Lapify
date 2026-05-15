import os

def get_serial_number():
    pipe = os.popen('cat /sys/class/dmi/id/product_serial')
    serialNumber = pipe.read().strip()
    return serialNumber

print(f"Serial Number: {get_serial_number()}")

class Student:
    def student_details(self, name, regNo, laptop_model ):
        self.name = name
        self.regNo = regNo
        self.laptop_model = laptop_model
        

student1 = Student()

student1.name = "Brad"
student1.regNo = "C028/404587/2024"
student1.laptop_model = "MSI Stealth gs66"

print(student1.name)
print(student1.regNo)
print(student1.laptop_model)



