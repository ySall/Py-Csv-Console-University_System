import pathlib
import csv

class Check():

    def __init__(self, file):
        self.file = file

    def CreateFile(self):
        file = pathlib.Path(self.file)
        if not file.exists ():
            open(self.file, "x").close()

    def ReadFile(self):
        with open(self.file, "r") as file:
            return csv.reader(file)

    def CheckID(self, id):
        with open(self.file, "r") as f:
            ID_list = [line.strip().split(",") for line in f]
        for ID in ID_list:
            if id == ID[0]:
                return True
        return False    