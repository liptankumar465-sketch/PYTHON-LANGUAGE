import copy

import pattern
#! How To Copy A List
# ?------------------------------------------------------------
pattern.line()
# todo: Assignment operator: Use for Normal Copy
# todo: Avoid (=): This Is Risky & Confusing
print('Use of (=)')
list1 = list('liptan')
list2 = list1
print(f"""List1: {list1}
List2: {list2}""")

print('Check There Address: Using (is)')
print("List1 & List2 Address Different: ", list2 is not list1)

pattern.line()
# todo: copy() -> Shallow Copye: Safe For Only (1D) Data Struc
print('Use of copy.copy(original_str)')
original_str = list('liptan')
copy_str = copy.copy(original_str)

print(f"""original_str: {original_str}
copy_str: {copy_str}""")

print('Check There Address: Using (is)')
print("List1 & List2 Address Different: ", original_str is not copy_str)

pattern.line()
# todo: deepcopy() -> Deep Copye: Safe For Both (1D & 2D) Data Struc
print('Use of copy.deepcopy(original_data)')
original_data = list('kumar')
deepcopy_data = copy.deepcopy(original_data)

print(f"""original data: {original_data}
Deep Copy Data: {deepcopy_data}""")

print('Check There Address: Using (is)')
print("List1 & List2 Address Different: ", original_data is not deepcopy_data)
