class Student:
    def __init__(self, name, year, department):
        self.name = name
        self.year = year
        self.department = department
        print("Name:", self.name)
        print("Year:", self.year)
        print("Department:", self.department)

    def detail(self, cgpa, backlogs):
        self.cgpa = cgpa
        self.backlogs = backlogs
        print("CGPA:", self.cgpa)
        print("Backlogs:", self.backlogs)

    def interesting(self, game, field):
        self.game = game
        self.field = field
        print("Game interest:", self.game)
print("detils of student 1")
student1 = Student("Subash", "3rd", "ECE")
student1.detail(8.5, 0)
student1.interesting("Football", "Robotics")
print()
print()
print("detils of student 2")
student2 = Student("devil", "3rd", "EEE")
student2.detail(9, 0)
student2.interesting("basketball", "IOT")
print()
print()
print("detils of student 1")
student3 = Student("LUCIFER", "3rd", "IT")
student3.detail(9.5, 0)
student3.interesting("CRICKET", "FULLSTASK DEVELOPER")

