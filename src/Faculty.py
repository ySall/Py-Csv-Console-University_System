from prettytable import PrettyTable
from src.Department import Department
from src.Check import Check
from src.Decoration import *

class Faculty:

    def __init__(self):
        self.file = "data/Faculty.csv"
        self.check = Check(self.file)

    def AddFaculty(self):
        id = input("Enter ID: ")
        if self.check.CheckID(id):
            print("Faculty already exists")
            return
        Name = input("Enter Faculty Name: ").title()
        Dean = input("Enter Dean Name: ").title()
        officeNo = input("Enter Office Room Number: ").upper()
        with open(self.file, "a") as f:
            f.write(id + "," + Name + "," + Dean + "," + officeNo + "\n")
    
    def SearchFaculty(self):
        id = input("Enter ID: ")
        if not self.check.CheckID(id):
            print("Faculty does not exist")
            return
        with open(self.file, "r") as f:
            faculty_list = [line.strip().split(",") for line in f]
        display = PrettyTable(["id", "Name", "Dean", "Office No"])
        for fac_item in faculty_list:
            if id == fac_item[0]:
                display.add_row(fac_item)
                print(display)
                return
                    
    def DeleteFaculty(self):
        id = input("Enter ID: ")
        if not self.check.CheckID(id):
            print("Faculty does not exist")
            return
        with open(self.file, "r") as f:
            facult_list = [line.strip().split(",") for line in f]
        with open(self.file, "w") as f:
            for fac in facult_list:
                if id != fac[0]:
                    f.write(",".join(fac) + "\n")
        department = Department()
        department.check.CreateFile()
        with open(department.file, "r") as f:
            Dep_list = [line.strip().split(",") for line in f]
        for dep in Dep_list:
            if id == dep[-1]:
                department.DeleteDepartment(dep[0])
        print("Faculty deleted")

    def UpdateFaculty(self):
        id = input("Enter ID: ")
        if not self.check.CheckID(id):
            print("Faculty does not exist")
            return
        with open(self.file, "r") as f:
            fac_list = [line.strip().split(",") for line in f]
        with open(self.file, "w") as f:
            for fac in fac_list:
                if id != fac[0]:
                    f.write(",".join(fac) + "\n")
                else:
                    while True:
                        print("[1]. Update Faculty Name")
                        print("[2]. Update Dean Name")
                        print("[3]. Update Office Number")
                        print("[4]. Exit")
                        choice = input("Enter your choice: ")
                        if choice == "1":
                            fac[1] = input("Enter Faculty Name: ").title()
                        elif choice == "2":
                            fac[2] = input("Enter Dean Name: ").title()
                        elif choice == "3":
                            fac[3] = input("Enter Office Room Number: ").upper()
                        elif choice == "4":
                            break
                        else:
                            print("Invalid choice")
                    f.write(",".join(fac) + "\n")
        print("Faculty updated")

    def FacultyMenu(self):
        self.check.CreateFile()
        while True:
            print("[Faculty Menu]\n")
            print("[a]. Add a new faculty")
            print("[b]. Search a faculty")
            print("[c]. Update a faculty")
            print("[d]. Delete a faculty by id")
            print("[e]. Return to main menu")
            choice = input("Enter your choice: ")
            if choice == "a":
                self.AddFaculty()
                clearScreen()
            elif choice == "b":
                self.SearchFaculty()
                clearScreen()
            elif choice == "c":
                self.UpdateFaculty()
                clearScreen()
            elif choice == "d":
                self.DeleteFaculty()
                clearScreen()
            elif choice == "e":
                clear()
                break
            else:
                print("Invalid choice")