from src.Check import Check
from prettytable import PrettyTable
from src.Enroll import Enroll
from src.Student import Student
from src.Decoration import *

class Department():
    def __init__(self):
        self.file = "data/Department.csv"
        self.check = Check(self.file)

    def AddDepartment(self):
        id = input("Enter Department id: ")
        if self.check.CheckID(id):
            print("Department already exists")
            return 
        Name = input("Enter Department Name: ").title()
        Head = input("Enter Head Name: ").title()
        officeNo = input("Enter Office Room Number: ").upper()
        Facid = input("Enter faculty id: ")
        faculty = Check("data/Faculty.csv")
        if not faculty.CheckID(Facid):
            print("faculty does not exist")
            return    
        with open(self.file, "a") as f:
            f.write(id + "," + Name + "," + Head + "," + officeNo + "," + Facid + "\n")
    
    def SearchDepartment(self):
        id = input("Enter id: ")
        if not self.check.CheckID(id):
            print("Department does not exist")
            return
        dep_list = self.check.ReadFile()
        for dep in dep_list:
            if id == dep[0]:
                display = PrettyTable(["id", "Name", "Head", "Office No", "faculty id"])
                display.add_row(dep)
                print(display)

    def DeleteDepartment(self, id):
        if not self.check.CheckID(id):
            print("Department does not exist")
            return
        with open(self.file, "r") as f:
            Dep_list = [line.strip().split(",") for line in f]
        with open(self.file, "w") as f:
            for dep in Dep_list:
                if id != dep[0]:
                    f.write(",".join(dep) + "\n")
                else:
                    dep_name = dep[1]
        enroll = Enroll()
        with open("data/Student.csv", "r") as f:
            Std_list = [line.strip().split(",") for line in f]
        for std in Std_list:
            if dep_name == std[-1]:
                enroll.Remove(std[0])
                return
        
    def UpdateDepartment(self):
        id = input("Enter id: ")
        if not self.check.CheckID(id):
            print("Department does not exist")
            return
        with open(self.file, "w") as f:
            for dep in self.list:
                if id != dep[0]:
                    f.write(",".join(dep) + "\n")
                else:
                    Name = input("Enter Department Name: ").title()
                    Head = input("Enter Head Name: ").title()
                    officeNo = input("Enter Office Room Number: ").upper()
                    faculty = faculty()
                    Facid = input("Enter faculty id: ")
                    while not faculty.Checkfaculty(Facid):
                        print("faculty does not exist")
                        Facid = input("Enter faculty id: ")
                    f.write(id + "," + Name + "," + Head + "," + officeNo  + "," + Facid + "\n")

    def DisplayDepartment(self):
        faculty = Check("data/Faculty.csv")
        Facid = input("Enter faculty id: ")
        if not faculty.CheckID(Facid):
            print("faculty does not exist")
            return
        display = PrettyTable(["id", "Name", "Head", "Office No", "faculty id"])
        for dep in self.list:
            if self.Facid == dep[-1]:
                display.add_row(dep)
        print(display)

    def DepartmentMenu(self):
        self.check.CreateFile()
        while True:
            print("[Department Menu]\n")
            print("[a]. Add a new department")
            print("[b]. Search a department")
            print("[c]. Delete a department by id")
            print("[d]. Update a department")
            print("[e]. Display all departments belonging to a faculty by faculty id")
            print("[f]. Return to main menu")
            choice = input("Enter your choice: ")
            if choice == "a":
                self.AddDepartment()
                clearScreen()
            elif choice == "b":
                self.SearchDepartment()
                clearScreen()
            elif choice == "c":
                dep = input("Enter id: ")
                self.DeleteDepartment(dep)
                clearScreen()
            elif choice == "d":
                self.UpdateDepartment()
                clearScreen()
            elif choice == "e":
                self.DisplayDepartment()
                clearScreen()
            elif choice == "f":
                clear()
                break
            else:
                print("Invalid choice")
            