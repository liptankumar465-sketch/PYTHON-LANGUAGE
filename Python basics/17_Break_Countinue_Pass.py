
# todo:----------------Break----------------------#
# ? It stops the loop immeddiately.
# ? It jumps out and ends the loop right away.

#! Using break statement:
print("Using break")
names = ["rahul", "kumar", "", "pratik"]
for name in names:
    if name == "":
        print("Empty value detected!")
        break
    print(f"Name = {name}")

# todo:---------------Continue------------------#
# ? It skips one loop cycle without stopping the loop.
print("\nUsing continue")
names = ["rahul", "kumar", "", "pratik"]
for name in names:
    if name == "":
        print("Empty value detected!")
        continue
    print(f"Name = {name}")

# todo:-----------------Pass--------------------#
# ? It is a placeholder where nothing happens
print("\nUsing pass")
names = ["rahul", "kumar", "", "pratik"]
for name in names:
    if name == "":
        print("Empty value detected!")
        pass  # todo: Handle empty value
    print(f"Name = {name}")

# ? Handle empty value naxt day:
print("\nHandle pass condition!")
names = ["rahul", "kumar", "", "pratik"]
for name in names:
    if name == "":
        name = name.replace('', "unknown")
    print(f"Name = {name}")

# todo:-----------Challeng------------#
# ? Skip weekends in calender loop:
print('\ncalender loop!')
days = ['sun', 'mon', 'tus', 'wed', 'fri', 'sat',]
weekends = ['sun', 'sat']
for day in days:
    if day in weekends:
        continue
    print(f'Workday: {day}')

# ? Email varification:
print('\nCheck emails!')
emails = [
    'data@gmail.com',
    'baraa@outlook.de',
    'DORP TABLE USERS;',
    'liptan@gmail.com'
]

for email in emails:
    if ';' in email:
        print("SQL Injection: Hacker Attack!")
        break
    print(f'Processing Email: {email}')
