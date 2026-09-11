#-------------Case-Match--------------#
#todo: Evaluate a value against multiple values
#todo: runs the code of the first match.

#! Useing Treditional if else
country = "India"
if country == "India":
    print("IND")
elif country == "United states":
    print("US")
elif country == "Egypt":
    print("EG")
elif country == "Germany":
    print("GE")
else:
    print("Unknown Country")

#! Using Case-Match
country = "Ram pur"
match country:
    case "India":
        print("IND")
    case "United states":
        print("US")
    case "Egypt":
        print("EG")
    case "Germany":
        print("GE")
    case _:        #! _: -> default sign
        print("Unkown Country")










