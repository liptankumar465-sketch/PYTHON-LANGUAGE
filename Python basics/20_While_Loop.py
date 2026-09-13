
#!---------------While loop--------------------#
# ? Repeats a block of code - over and over as long
# ? as condition is True!

# todo: While condition:

count = 1  # ! Initialization
while count <= 5:  # ! Condition
    print(count)
    count += 1  # ! Updatin


# todo: Take yes from user:

answer = ""
while answer != "yes":
    answer = input("Do you agree?(yes/no): ")

print("Thank you")


# todo: While True:

while True:
    answer = input("Do you agree?(yes/no): ")
    if answer == 'yes':
        break
print("Thank you")

# todo: User only enter password three times:
attempts = 0
is_correct = False
while attempts < 3:
    password = input("Enter your password: ")
    if password == '775411':
        is_correct = True
        break
    attempts += 1
else:
    print("Your attempts are over")

if is_correct:
    print("correct password entered")
