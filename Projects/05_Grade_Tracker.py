
#! GRADE TRACKER:
# ?-----------------------------------------------------------------
# todo: Create a Grade Tracker module/function:

def grade_tracker(students: dict) -> None:
    for student, grade in students.items():
        average = sum(grade)/len(grade)
        print(f'student: {student}: {grade} --> avg: {average}')


students = {
    'liptan': [66, 43, 75, 23, 86],
    'sita': [56, 23, 87, 32, 32],
    'gotam': [76, 34, 92, 76, 21]
}

grade_tracker(students=students)
