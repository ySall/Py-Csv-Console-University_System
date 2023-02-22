from src.Check import Check	
from prettytable import PrettyTable

class Manage_course:
  def __init__(self):
    self.file = "data/Course.csv"
    self.check = Check(self.file)
        
  def addCourse(self):
    id = input("Enter Course id: ")
    if self.check.CheckID(id):
        print("Course already exists")
        return
    courseName = input("Enter Course: ")
    credit = input("Enter Course Credit: ")
    type = input("Enter Course Type (lecture or Lab):: ")
    with open(self.file, "a") as file:
      file.write(f"{id},{courseName},{credit},{type}\n")
      
  def search_course(self):
    id = input("Enter ID: ")
    lines = self.check.ReadFile()
    for line in lines:
      if line[0] == id:
        display = PrettyTable(["id", "Course", "Credit", "Type"])
        display.add_row(line)
        print(display)
        return
    print("Course not found")
  
  def update_course(self):
    id = input("Enter ID: ")
    if not self.check.CheckID(id):
        print("Course does not exist")
        return
    courseName = input("Enter Course: ")
    credit = input("Enter Course Credit: ")
    type = input("Enter Course Type:: ")
    lines = self.check.ReadFile()
    with open(self.file, "w") as file:
      for line in lines:
        if line[0] != id:
          file.write(line)
        else:
          file.write(f"{id}, {courseName}, {credit}, {type}")
        
  def delete_course(self):
    id = input("Enter ID: ")
    if not self.check.CheckID(id):
        print("Course does not exist")
        return
    lines = self.check.ReadFile()
    with open(self.file, "w") as file:
      for line in lines:
        if line[0] != id:
            file.write(line) 
    print("Course deleted")
  
  def Course_menu(self):
    not_end = True
    self.check.CheckFile()
    while not_end:
      print("[a]. Add a new Course")
      print("[b]. Search a Course by id")
      print("[c]. Delete Course by id")
      print("[d]. Update Course")
      print("[e]. Return to main menu")
      choice = input("Enter Choice:: ")
      match choice:
        case "a":
          self.addCourse()
        case "b":
          self.search_course()
        case "c":
          self.delete_course()
        case "d":
          self.update_course()
        case "e":
          not_end = False
        case _: 
          print("Invalid Choice")