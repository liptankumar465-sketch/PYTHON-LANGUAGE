# Write your Python code here
print("Calculate the student grade!")

marks = int(input('Enter the marks:- '))
grade  = ''

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

print('\nYour grade:- ',grade)