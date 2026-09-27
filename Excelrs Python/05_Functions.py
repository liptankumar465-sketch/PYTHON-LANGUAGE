# Write your Python code here

# Function for cal grade
def getGrade(mark, name):

    if mark > 90:
        grade = 'A+'
    elif mark > 80:
        grade = 'A'
    elif mark > 60:
        grade = 'B'
    elif mark > 35:
        grade = 'C'
    else:
        grade = 'fail'

    print(f'Your name:- {name}')
    print(f'Your grade:- {grade}')
    st_names_grades.append({name: grade})


def showTopper():
    topper = st_names_grades[0]
    print(topper)


def showfail():
    fail = st_names_grades[1]
    print(fail)


print("Using of functions!")
st_names_grades = []  # init empty

for i in range(2):
    name = input('Enter the name: ')
    mark = int(input('Enter the mark: '))
    getGrade(mark, name)  # calling the function

showTopper()
showfail()
