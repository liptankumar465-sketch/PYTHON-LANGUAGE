# Write your Python code here
print('Using of list!')
print('Store the all students grade in list!')

grades = [] # Empty list

for i in range(3):
  marks = int(input('Enter the mark:- '))
  grade = '' # Empty string

  if marks > 90:
    grade = 'A+'
  elif marks > 80:
    grade = 'A'
  elif marks > 60:
    grade = 'B'
  elif marks > 35:
    grade = 'C'
  else:
    grade = 'fail'

  print(f'Your grade:- {grade}')
  grades.append(grade)

print('All studends grades: ',grades)

