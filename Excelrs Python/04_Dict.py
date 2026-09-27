# Write your Python code here
print('Using of dict!')

st_names_grades = []  # init empty

for i in range(3):
    name = input('Enter the name: ')
    mark = int(input('Enter the mark: '))
    grade = ''

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

    print(f'Your grade:- {grade}')
    st_names_grades.append({"Name": name, "Grade": grade})

print('Display the st names or grades')
print(st_names_grades)
