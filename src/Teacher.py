from src.Check import Check
from datetime import datetime
from prettytable import PrettyTable
from src.Decoration import *
from src.CourseAssign import AssignCourses

class Teacher:
    
    def __init__(self):
        self.file_name = "data/Teacher.csv"
        self.assigncoure_file = "data/AssignCourse.csv"
        self.check = Check(self.file_name)
        self.check5 = Check(self.assigncoure_file)
        self.teacher_list = self.check.ReadFile()
    
    def addTeacher(self):
        id = input("Enter Teacher ID: ")
        if self.check.CheckID(id):
            print("Teacher ID already exists in file")
            return
        name = input("Enter Teacher Name: ").title()
        gender = input("Enter Teacher Gender (M/F): ").upper()
        while gender not in ["M", "F"]:
            print("Gender must be M or F")
            gender = input("Enter Teacher Gender(M/F): ").upper()
        if gender ==  "M":
            gender = "Male"
        else:
            gender = "Female"
        print("Date of Birth")
        
        day = input("Enter Day of Birth: ")
        while int(day) not in range(1, 32):
            print("The Day Birth nust be between 1 and 31")
            day = input("Enter Day of Birth: ")
        
        month = input("Enter Month of Birth: ")
        while int(month) not in range(1, 13):
            print("Month must be between 1 and 12")
            month = input("Enter Month of Birth: ")
        
        year = input("Enter Year of Birth: ")
        datetime_object = datetime.strptime(month, "%m")
        month_name = datetime_object.strftime("%b")
        date_of_birth = f"{int(day):02d}-{month_name.upper()}-{year}"
        
        contact = input("Enter Teacher Contact Number: ")
        while not contact.isnumeric():
            print("Contact Number Must Be Numberic: ")
            contact = input("Enter Teacher Contact Number: ")
        contact = contact[:3] + "-" + contact[3:6] + "-" + contact[6:]
        
        address = input("Enter The teacher Address: ")
        with open(self.file_name, "a") as myFile:
            myFile.write(id + "," + name + "," + gender + "," + date_of_birth + "," + contact + "," + address + "\n")
        print("Teacher have been added")
    
    def searchingTeacher(self):
        id = input("Enter Teacher ID: ")
        while not self.check.CheckID(id):
            print("Teacher ID does not exist in file")
            id = input("Enter Teacher ID: ")
        for teach in self.teacher_list:
            if id == teach[0]:
                display = PrettyTable(["ID", "Name", "Gender", "Date of Birth", "Phone Number", "Address"])
                display.add_row(teach)
                print(display)
                return
                
    def updatingTeacher(self):
        self.id = input("Enter Teacher ID: ")
        while not self.check.CheckID(self.id):
            print("Teacher ID does not exist in file, Try againt...!")
            self.id = input("Enter Teacher ID: ")
        with open(self.file_name, "r") as myFile:
            self.teacher_list = [line.strip().split(",") for line in myFile]
        with open(self.file_name, "w") as myFile:
            for self.teacher in self.teacher_list:
                if self.id != self.teacher[0]:
                    myFile.write(",".join(self.teacher) + "\n")
                else:
                    isUpdating = True
                    while isUpdating:
                        print("[1]. Update Teacher Name")
                        print("[2]. Update Teacher Gender")
                        print("[3]. Update Date of Birth")
                        print("[4]. Update Phone Number")
                        print("[5]. Update Address")
                        print("[6]. Exit")
                        choice = input("Enter Your Choice: ")
                        if choice == "1":
                            self.teacher[1] = input("Enter Teacher Name: ").title()
                        elif choice == "2":
                            self.gender = input("Enter Teacher Gender[M/F]: ").upper()
                            while self.gender not in ["M", "F"]:
                                print("Gender must be M or F")
                                self.gender = input("Enter Student Gender[M/F]: ").upper()
                            if self.gender == "M":
                                self.teacher[2] == "Male"
                            else:
                                self.teacher[2] == "Female"
                        elif choice == "3":
                            print("Date of Birth")
                            
                            self.day = input("Enter Day of Birth: ")
                            while int(self.day) not in range(1, 32):
                                print("Day must be between 1 and 31")
                                self.day = input("Enter Day of Birth: ")
                            
                            self.month = input("Enter Month of Birth: ")
                            while int(self.month) not in range(1, 13):
                                print("Month must be between 1 and 12")
                                self.month = input("Enter Month of Birth: ")
                            
                            self.year = input("Enter Year of Birth: ")
                            self.datetime_object = datetime.strptime(self.month, "%m")
                            self.month_name = self.datetime_object.strftime("%b")
                            self.teacher[3] = f"{int(self.day):02d}-{self.month_name.upper()}-{self.year}"
                        elif choice == "4":
                            self.contact = input("Enter Teacher Contact Number: ")
                            while not self.contact.isnumeric():
                                print("Contact Number Must Be Numberic: ")
                                self.contact = input("Enter Teacher Contact Number: ")
                            self.contact = self.contact[:3] + "-" + self.contact[3:6] + "-" + self.contact[6:]
                        elif choice == "5":
                            self.address = input("Enter New Teacher Address: ")
                        elif choice == "6":
                            print("Bye Bye!")
                            isUpdating = False
                        else:
                            print("Invalid Choice")
                        print("Updated Student Successfully")
                    myFile.write(",".join(self.teacher) + "\n")
    
    def displayTeacher(self):
        with open(self.file_name, "r") as myFile:
            self.teacher_list = [line.strip().split(",") for line in myFile]
        self.myTable = PrettyTable(["ID", "Name", "Gender", "Date of Birth", "Phone Number", "Address"])
        for self.teacher in self.teacher_list:
            self.myTable.add_row(self.teacher)
        print(self.myTable)
    
    def deletingTeacher(self):
        self.id = input("Enter Teacher ID: ")
        while not self.check.CheckID(self.id):
            print("Teacher ID does not exist in file, Try againt...!")
            self.id = input("Enter Teacher ID: ")
        with open(self.file_name, "r") as myFile:
            self.teacher_list = [line.strip().split(",") for line in myFile]
        with open(self.file_name, "w") as myFile:
            for self.teacher in self.teacher_list:
                if self.id != self.teacher[0]:
                    myFile.write(",".join(self.teacher) + "\n")
                    
        with open(self.assigncoure_file, "r") as myAssignCourseFile:
            self.teacher_list = [line.strip().split(",") for line in myAssignCourseFile]
        with open(self.assigncoure_file, "w") as myAssignCourseFile:
            for self.teacher in self.teacher_list:
                if self.teacher[0] != self.id:
                    myAssignCourseFile.write(",".join(self.teacher) + "\n")
        print("Teacher Deleted Successfully")

    
    def teacherMenu(self):
        self.check.CreateFile()
        isWorking = True
        while isWorking:
            print("[Teacher Menu]\n")
            print("1. Add Teacher")
            print("2. Search Teacher by ID")
            print("3. Update Teacher")
            print("4. Delete Teacher")
            print("5. Display All Teacher")
            print("6. Display All Courses Taugh by Teacher")
            print("7. Return to Main Menu")
            choice = input("Enter Your Choice: ")
            match choice:
                case "1":
                    self.addTeacher()
                    clearScreen()
                case "2":
                    self.searchingTeacher()
                    clearScreen()
                case "3":
                    self.updatingTeacher()
                    clearScreen()
                case "4":
                    self.deletingTeacher()
                    clearScreen()
                case "5":
                    self.displayTeacher()
                    clearScreen()
                case "6":
                    assigncourse = AssignCourses()
                    assigncourse.display()
                    clearScreen()
                case "7":
                    isWorking = False
                    clearScreen()
                case _:
                    print("Invalid Choice")
                    clearScreen()