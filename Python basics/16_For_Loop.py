# -------------Loops-------------#
# ? Control the flow of code.
# ? Repeat a block of code over and over until a
# ? condition is met.

#! FOR LOOP:
# todo: Go through a group of items one by one to do
# todo: something for each item.

#! Python Iterator:
# todo: An  object that lets you go through items one
# todo: one by one in a sequence.

# ? Basic way:

print("Basic way!")
print("Round: 1")
print("Round: 2")
print("Round: 3")
print("Round: 4")
print("Round: 5")

# ? Using For Loop:

print("\nFor Loop!")
for i in (1, 2, 3, 4, 5):  # ! Sequence is tuple
    print(f"Round: {i}")

# ? Iterates the items:

print("\nIterates the items!")
items = [1, 2, 3, 4, 5]   # ! sequence is list
for item in items:
    print(f"Item: {item}")

# ? Iterates the items:

print("\nIterates the items!")
items = "liptan"   # ! sequence is string
for item in items:
    print(f"Item: {item}")

# ? Iterates the items:

print("\nIterates the for loop 50 times!")
for i in range(1, 50):
    print(f"Round: {i}")

#! Sequence is range(start, stop, step)
# ? By default start = 0, stop = stop - 1, steps = cond/vari.

print("\nRange sequence!")
for i in range(1, 10, 2):
    print(f"Round: {i}")


# -----------Challenge------------#
# First:
print("\nCal the total score!")

scores = [23, 56, 34, 87, 96]
total = 0

for score in scores:
    total += score
    print(f"Current score: {score}")
print("Total score: ", total)

# Second:
print("\nClean the files!")

files = [' Report.csv ','DATA.csv ', ' final.TXT']

for file in files:
    file = file.strip().lower().replace('txt','csv')
    print("Processing: ",file)


