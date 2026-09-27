# Write your Python code here
print("2 Usese of class!")


class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.grade = ""

    def calculateGrade(self):
        if self.marks > 90:
            self.grade = "A"
        elif self.marks > 80:
            self.grade = "B"
        elif self.marks > 60:
            self.grade = "C"
        else:
            self.grade = "D"

    def displayGrade(self):
        print(self.grade)


st1 = Student('liptan', 89)
st2 = Student('kumar', 56)

st1.calculateGrade()
st1.displayGrade()

st2.calculateGrade()
st2.displayGrade()
