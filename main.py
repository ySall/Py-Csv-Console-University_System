from src.Decoration import *
from src.Faculty import Faculty
from src.Department import Department
from src.Student import Student
from src.Enroll import Enroll
from src.Course import Manage_course
from src.Teacher import Teacher
from src.CourseAssign import AssignCourses

def createMenu():
    clear()
    print("Welcome to the University Management System")
    print("===========================================")
    MainMenu = True
    while MainMenu:
        print("Please select an option from the menu below:\n")
        print("[1]. Manage Faculties\t\t[6]. Manage Teachers")
        print("[2]. Manage Departments\t\t[7]. Assign Course to Teachers")
        print("[3]. Manage Students\t\t[8]. Create Teacher/Student Accounts")
        print("[4]. Enroll Students\t\t[9]. Test login Accounts")
        print("[5]. Manage Courses\t\t[10]. Exit\n")
        choice = input("Enter your choice: ")
        clear()
        if choice == "1":
            faculty = Faculty()
            faculty.FacultyMenu()
        elif choice == "2":
            department = Department()
            department.DepartmentMenu()
        elif choice == "3":
            student = Student()
            student.StudentMenu()
        elif choice == "4":
            enroll = Enroll()
            enroll.EnrollMenu()
        elif choice == "5":
            course = Manage_course()
            course.Course_menu()
        elif choice == "6":
            teacher = Teacher()
            teacher.teacherMenu()
        elif choice == "7":
            courseAssign = AssignCourses()
            courseAssign.menu()
        elif choice == "8":
            pass
        elif choice == "9":
            pass
        elif choice == "10":
            print("\n[Exiting Program]")
            MainMenu = False
        else:
            print("Invalid choice. Please try again.\n")
            clearScreen()

if __name__ == "__main__":
    createMenu()
