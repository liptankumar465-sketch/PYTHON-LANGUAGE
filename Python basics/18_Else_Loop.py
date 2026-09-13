
# todo: Loop else work when hole loop is iterat.
# todo: If not than else not works.

# ? Check for even number:
items = [1, 3, 4, 7, 9]
for i in items:
    if i % 2 == 0:
        print(f'Even num found: {i}')
        break
else:
    print('All numbers are odd')

# ? Checks Names is None:
names = ['kumar', 'tuda', None, 'ram']

for name in names:
    if name is None:
        print("Found a missing name!")
        break
else:
    print("All names are avaiable!")

# ? Check .CSV files:
files = [
    'data1.csv',
    'report.pdf',
    'data2.csv',
    'report2.csv'
]

for file in files:
    if not file.endswith('.csv'):
        print(f"{file} is not a .CSV")
        break
else:
    print("All files are .CSV")


# ? Check duplicale file present or not in files:
files_list = [
    'data1.csv',
    'report.pdf',
    'data2.csv',
    'data2.csv',
    'report2.csv'
]

for file in files_list:
    if files_list.count(file) > 1:
        print("Duplicat files are present!")
        break
else:
    print("No duplicat files are present!")