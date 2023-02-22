from src.Check import Check
from datetime import datetime
from prettytable import PrettyTable
from src.Decoration import *

class Student():
    def __init__(self):
        self.file = "Student.csv"
        self.check = Check(self.file)
        
    def AddStudent(self):
        id = input("Enter Student id: ")
        if self.check.CheckID(id):
            print("Student ID already exists")
            return
        name = input("Enter Student Name: ").title()
        gender = input("Enter Student Gender(M/F): ").upper()
        while gender not in ["M", "F"]:
            print("Gender must be M or F")
            gender = input("Enter Student Gender(M/F): ").upper()
        if gender == "M":
            gender = "Male"
        else:
            gender = "Female"
        print("Date of Birth")
        day = input("Enter Day: ")
        while int(day) not in range(1, 32):
            print("Day must be between 1 and 31")
            day = input("Enter Day: ")
        month = input("Enter Month: ")
        while int(month) not in range(1, 13):
            print("Month must be between 1 and 12")
            month = input("Enter Month: ")
        year = input("Enter Year: ")
        datetime_object = datetime.strptime(month, "%m")
        month_name = datetime_object.strftime("%b")
        DoB=f"{int(day):02d}-{month_name.upper()}-{year}"
        contact = input("Enter Student Contact Number: ")
        while not contact.isnumeric():
            print("Contact Number must be numeric")
            contact = input("Enter Student Contact Number: ")
        contact = contact[:3] + "-" + contact[3:6] + "-" + contact[6:]
        Year = input("Enter Year of Student: ")
        while int(Year) not in range(1, 5):
            print("Year must be between 1 and 4")
            Year = input("Enter Year of Study: ")
        generation = input("Enter Generation: ")
        print("Input BD as Bachelor Degree or MD as Master Degree")
        degree = input("Enter Degree: ").upper()
        while degree not in ["BD", "MD"]:
            print("Degree must be BD or MD")
            degree = input("Enter Degree: ").upper()
        if degree == "BD":
            degree = "Bachelor Degree"
        else:
            degree = "Master Degree"
        with open(self.file, "a") as f:
            f.write(id + "," + name + "," + gender + "," + DoB + "," + contact + "," + Year + "," + generation + "," + degree + "," + "None" + "\n")
        print("Student Added")

    def SearchStudent(self):
        id = input("Enter Student ID: ")
        if not self.check.CheckID(id):
            print("Student ID does not exist")
            return
        for stu in self.list:
            if id == stu[0]:
                display = PrettyTable(["ID", "Name", "Gender", "Date of Birth", "Contact", "Year", "Generation", "Degree", "Department"])
                display.add_row(stu)
                print(display)

    def UpdateStudent(self):
        id = input("Enter Student ID: ")
        if not self.check.CheckID(id):
            print("Student ID does not exist")
            return
        student_list = self.check.ReadFile()
        with open(self.file, "w") as f:
            for stu in student_list:
                if id != stu[0]:
                    f.write(",".join(stu) + "\n")
                else:
                    while True:
                        print("1. Update Name")
                        print("2. Update Gender")
                        print("3. Update Date of Birth")
                        print("4. Update Contact Number")
                        print("5. Update Year of Student")
                        print("6. Update Generation")
                        print("7. Update Degree")
                        print("8. Exit")
                        choice = input("Enter Choice: ")
                        match choice:
                            case "1":
                                stu[1] = input("Enter Student Name: ").title()
                            case "2":
                                gender = input("Enter Student Gender(M/F): ").upper()
                                while gender not in ["M", "F"]:
                                    print("Gender must be M or F")
                                gender = input("Enter Student Gender(M/F): ").upper()
                                if gender == "M":
                                    stu[2] = "Male"
                                else:
                                    stu[2] = "Female"
                            case "3":
                                print("Date of Birth")
                                day = input("Enter Day: ")
                                while int(day) not in range(1, 32):
                                    print("Day must be between 1 and 31")
                                    day = input("Enter Day: ")
                                month = input("Enter Month: ")
                                while int(month) not in range(1, 13):
                                    print("Month must be between 1 and 12")
                                    month = input("Enter Month: ")
                                year = input("Enter Year: ")
                                datetime_object = datetime.strptime(month, "%m")
                                month_name = datetime_object.strftime("%b")
                                DoB=f"{int(day):02d}-{month_name.upper()}-{year}"
                                stu[3] = DoB
                            case "4":
                                contact = input("Enter Student Contact Number: ")
                                while not contact.isnumeric():
                                    print("Contact Number must be numeric")
                                    contact = input("Enter Student Contact Number: ")
                                contact = contact[:3] + "-" + contact[3:6] + "-" + contact[6:]
                                stu[4] = contact
                            case "5":
                                Year = input("Enter Year of Student: ")
                                while int(Year) not in range(1, 5):
                                    print("Year must be between 1 and 4")
                                    Year = input("Enter Year of Study: ")
                                stu[5] = Year
                            case "6":
                                generation = input("Enter Generation: ")
                                stu[6] = generation
                            case "7":
                                print("Input BD as Bachelor Degree or MD as Master Degree")
                                degree = input("Enter Degree: ").upper()
                                while degree not in ["BD", "MD"]:
                                    print("Degree must be BD or MD")
                                    degree = input("Enter Degree: ").upper()
                                if degree == "BD":
                                    degree = "Bachelor Degree"
                                else:
                                    degree = "Master Degree"
                                stu[7] = degree
                            case "8":
                                break
                            case _:
                                print("Invalid Choice")
                        f.write(",".join(stu) + "\n")

    def DeleteStudent(self):
        id = input("Enter Student ID: ")
        if not self.check.CheckID(id):
            print("Student ID does not exist")
            return
        with open(self.file, "w") as f:
            for stu in self.list:
                if id != stu[0]:
                    f.write(",".join(stu) + "\n")
        print("Deleted Student Successfully")
    
    def DisplayStudent(self):
        display = PrettyTable(["ID", "Name", "Gender", "Date of Birth", "Contact", "Year", "Generation", "Degree", "Department"])
        for stu in self.list:
            display.add_row(stu)
        print(display)

    def StudentMenu(self):
        self.check.CheckFile()
        while True:
            print("[Student Menu]\n")
            print("1. Add Student")
            print("2. Search Student")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. Display  All Student")
            print("6. Return to Main Menu")
            choice = input("Enter Choice: ")
            match choice:
                case "1":
                    self.AddStudent()
                    clearScreen()
                case "2":
                    self.SearchStudent()
                    clearScreen()
                case "3":
                    self.UpdateStudent()
                    clearScreen()
                case "4":
                    self.DeleteStudent()
                    clearScreen()
                case "5":
                    self.DisplayStudent()
                    clearScreen()
                case "6":
                    clear()
                    break
                case _:
                    print("Invalid Choice")