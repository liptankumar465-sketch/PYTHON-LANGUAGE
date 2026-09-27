# Write your Python code here
print('Using loop!')
print("Calculate the all students grades!")

nr_of_St = int(input('Enter the total nr of st: '))

student_grades = []

for i in range(nr_of_St):
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

  print('name: ',name)
  print('mark: ',mark)
  student_grades.append({name:grade})

print('All st name and grades!')
print(student_grades)