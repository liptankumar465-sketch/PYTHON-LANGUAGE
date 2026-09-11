# Ternary operator:
# Syntax -> vari = "T" if condition else  "F"

#! Useing Treditional if else
score = 100
if score >= 90:
    print("A")
else:
    print("F")

#! Using Ternary operator
# ? First way:
print("A") if score >= 90 else print("F")
print("A" if score >= 90 else "F")

# ? Second way:
grad = "A" if score >= 90 else "F"
print(grad)

#! Useing Treditional if else
score = 80
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")

#! Using Ternary operator
print("A" if score >= 90 else "B" if score >= 80 else "C")

grad = "A" if score >= 90 else "B" if score >= 80 else "C"
print(grad)