import pattern
#! How To Change a List
# ?-----------------------------------------------------
# ? Create a list(1D) or (2D)
my_list = list('python')
print(type(my_list))

print('1D list')
print(my_list)

print('2D list')
my_list2 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
print(my_list2)

# ? append(val) -> Adding New Value At Last Index
pattern.line()
print('1D list')
print('Use of append("s")')
my_list.append('s')
print(my_list)


print('2D list')
print('Use of append([9,10,11])')
my_list2.append([9, 10, 11])
print(my_list2)

# ? insert(idx,val) -> Adding New Value At Any Index
pattern.line()
print('1D list')
print('Use of insert(0,"A")')
my_list.insert(0, 'A')
print(my_list)


print('2D list')
print('Use of [1]insert(3,22)')
my_list2[1].insert(3, 22)
print(my_list2)

# ? pop()/pop(index) -> Removing Last Value / Remove indexed Value
# ? And Return Removed item
pattern.line()
print('1D list')
print('Use of pop()/pop(0)')
last_item = my_list.pop()
first_item = my_list.pop(0)
print(f"""last item: {last_item}
first item: {first_item}
After Remove {my_list}""")


print('2D list')
print('Use of pop()/[1]pop(-1)')
last_row = my_list2.pop()
second_row_last = my_list2[1].pop(-1)
print(f"""last row: {last_row}
second row last item: {second_row_last}
After Removing {my_list2}""")


# ? remove(item)/removes(item) -> Remoing The items in The List
pattern.line()
print('1D list')
print('Use of remove("p")')
my_list.remove('p')
print(my_list)


print('2D list')
print('Use of [2]remove(9)')
my_list2[-1].remove(9)
print(my_list2)

# ? Updataing A list
pattern.line()
print('1D list')
print('Updating A list')
my_list[0] = 'L'
my_list[2] = 'P'
my_list[-1] = 'K'
print(my_list)


print('2D list')
print('Updating A list')
my_list2[-1][-1] = 20
my_list2[-1][-2] = 10
print(my_list2)
