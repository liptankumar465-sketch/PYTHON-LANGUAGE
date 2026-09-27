# Write your Python code here
print("3 Usese of class!")


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

    def displayDitails(self):
        print("name: ", self.name)
        print("marks: ", self.marks)
        print("grade: ", self.grade)


Students_list = []

for i in range(2):
    name = input('Enter name: ')
    marks = int(input('Enter name: '))

    st = Student(name, marks)
    st.calculateGrade()

    Students_list.append(st)

for i in range(2):
    Students_list[i].displayDitails()
