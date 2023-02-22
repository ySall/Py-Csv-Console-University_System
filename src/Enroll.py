from src.Check import Check
from prettytable import PrettyTable
from src.Decoration import *

class Enroll():
    def __init__(self):
        self.Studentfile = "data/Student.csv"
        self.Departmentfile = "data/Department.csv"
        self.Department = Check(self.Departmentfile)
        self.Student = Check(self.Studentfile)
         
    def EnrollStudent(self):
        student_id = input("Enter Student id: ")
        if not self.Student.CheckID(student_id):
            print("Student does not exist")
            return
        dep_id = input("Enter Department id: ")
        if not self.Department.CheckID(dep_id):	
            print("Department does not exist")
            return
        with open(self.Departmentfile, "r") as f:
            dep_list = [line.strip().split(",") for line in f]
        for dep in dep_list:
            if dep_id == dep[0]:
                dep_name = dep[1]
                break
        with open(self.Studentfile, "r") as f:
            student_list = [line.strip().split(",") for line in f]
        with open("data/Student.csv", "w") as f:
            for student in student_list:
                if student_id != student[0]:
                    f.write(",".join(student) + "\n")
                else:
                    student[-1] = dep_name
                    f.write(",".join(student) + "\n")
        print("Student Enrolled Successfully")

    def Remove(self, stud_id):
        if not self.Student.CheckID(stud_id):
            print("Student does not exist")
            return
        with open(self.Studentfile, "r") as f:
            student_list = [line.strip().split(",") for line in f]
        with open(self.Studentfile, "w") as f:
            for student in student_list:
                if stud_id != student[0]:
                    f.write(",".join(student) + "\n")
                else:
                    student[-1] = "None"
                    f.write(",".join(student) + "\n")
        print("Remove Student from Department Successfully")

    def Display(self):
        dep_id = input("Enter Department id: ")
        if not self.Department.CheckID(dep_id):
            print("Department does not exist")
            return
        dep_list = self.Department.ReadFile()
        for dep in dep_list:
            if dep_id == dep[0]:
                dep_name = dep[1]
                break
        student_list = self.Student.ReadFile()
        display = PrettyTable(["ID", "Name", "Gender", "Date of Birth", "Contact", "Year", "Generation", "Degree", "Department"])
        for student in student_list:
            if dep_name == student[-1]:
                display.add_row(student)
        print(display)

    def EnrollMenu(self):
        while True:
            print("[Enroll Menu]")
            print("1. Enroll Student to Department")
            print("2. Remove A Student from Department")
            print("3. Display all students studying from a department")
            print("4. Return to Main Menu")
            choice = input("Enter Choice: ")
            if choice == "1":
                self.EnrollStudent()
                clearScreen()
            elif choice == "2":
                student_id = input("Enter Student id: ")
                self.Remove(student_id)
                clearScreen()
            elif choice == "3":
                self.Display()
                clearScreen()
            elif choice == "4":
                clear()
                return
            else:
                print("Invalid Choice")