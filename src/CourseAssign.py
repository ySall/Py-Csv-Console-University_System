from src.Check import Check
from prettytable import PrettyTable
from src.Decoration import *
import csv

class AssignCourses:
    
    def __init__(self):
        self.course_file = "data/Course.csv"
        self.teacher_file = "data/Teacher.csv"
        self.assigncourse_file = "data/AssignCourse.csv"
        self.checkTeacher = Check(self.teacher_file)
        self.checkCourse = Check(self.course_file) 
        
    def AddCourseToTeacher(self):
        self.teacher_id = input("Enter Teacher ID: ")
        while not self.checkTeacher.CheckID(self.teacher_id):
            print("Teacher does not exist")
            self.teacher_id = input("Enter Teacher ID: ")
        with open(self.teacher_file, "r") as myTeacherFile:
            self.teacher_list1 = [line.strip().split(",") for line in myTeacherFile]
            for self.teacher in self.teacher_list1:
                if self.teacher[0] == self.teacher_id:
                    self.teacher_name = self.teacher[1]
            print("Teacher: " + self.teacher_name)
        self.course_id = input("Enter Course ID: ")
        while not self.checkCourse.CheckID(self.course_id):
            print("Course does not exist")
            self.course_id = input("Enter Course ID: ")
        with open(self.course_file, "r") as myCourseFile:
            self.course_list1 = csv.reader(myCourseFile)
            for self.course in self.course_list1:
                if self.course[0] == self.course_id:
                    self.course_name = self.course[1]
            print("Course: " + self.course_name)
        with open(self.assigncourse_file, "a") as myAssignCourseFile:
            myAssignCourseFile.write(self.teacher_id + "," + self.teacher_name + "," + self.course_id + "," + self.course_name + "\n")
            print("Course assigned to teacher")
    
    def display(self):
        with open(self.assigncourse_file, "r") as myAssignCourseFile:
            self.assigncourse_list = csv.reader(myAssignCourseFile)
            self.myTable= PrettyTable(["Teacher ID", "Teacher Name", "Course ID", "Course Name"])
            for self.assigncourse in self.assigncourse_list:
                self.myTable.add_row(self.assigncourse)
            print(self.myTable)
    
    

    def romoveCourseFromTeacher(self):
        self.teacher_id = input("Enter Teacher ID: ")
        while not self.checkTeacher.CheckID(self.teacher_id):
            print("Teacher ID does not exist in file, Try againt...!")
            self.teacher_id = input("Enter Teacher ID: ")
        self.id = input("Enter Course ID: ")
        while not self.checkCourse.CheckID(self.id):
            print("Course ID does not exist in file, Try againt...!")
            self.id = input("Enter Course ID: ")
        with open(self.assigncourse_file, "r") as myAssignCourseFile:
            self.teacher_list = [line.strip().split(",") for line in myAssignCourseFile]
        with open(self.assigncourse_file, "w") as myAssignCourseFile:
            for self.teacher in self.teacher_list:
                if self.teacher[0] != self.teacher_id:
                    myAssignCourseFile.write(",".join(self.teacher) + "\n")
        print("Course removed from teacher")
    
    def menu(self):
        isWorking = True
        while isWorking:
            print("[a]. Add Course To Teacher")
            print("[b]. Display Courses That Assigned To Teacher")
            print("[c]. Remove a Course From a Teacher")
            print("[d]. Return to Main Menu")
            choice = input("Enter your choice: ")
            match choice:
                case "a":
                    self.AddCourseToTeacher()
                    clearScreen()
                case "b":
                    self.display()
                    clearScreen()
                case "c":
                    self.romoveCourseFromTeacher()
                    clearScreen()
                case "d":
                    isWorking = False
                    print("ByeBye!")
                    clearScreen()
                case _:
                    print("Invalid choice, Try again...!")
                    clearScreen()