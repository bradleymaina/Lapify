import os

def get_serial_number():
    pipe = os.popen('cat /sys/class/dmi/id/product_serial')
    serialNumber = pipe.read().strip()
    return serialNumber

print(f"Serial Number: {get_serial_number()}")

class Student:
    def __init__(self,name, regNo, laptop_model ):
        self.name= name
        self.regNo = regNo
        self.laptop_model = laptop_model

student1 = Student("Bradley", "CO28/404587/2024", "MSI Stealth gs66") 

print(student1.name, student1.regNo, student1.laptop_model)



