
#!------------------Exploreing & Analyzeing-------------------------#
#! List functions:-
# ?--------------Analyze-----------------#
# todo: 1. max()      # Find extreme high
# todo: 2. min()      # Find extreme low
# todo: 3. sum()      # Find the total
# todo: 4. len()      # Find the length

# ?-------------Explore------------------#
# todo: 5. all()      # Did Everything pass?
# todo: 6. any()      # Did Something  pass?

#! List methods:-
# ?-----------Search & count-------------#
# todo: 1. .count("A")      # How often?
# todo: 2. .index("A")      # Where elem appears?

#! List operators:-
# ?------Membership & Identity----------#
# todo: 1. "A" in ["A","B"] --> True   # Check if elem exists!
# todo: 2. "A" is ["A","B"] --> False  # Check if same object!

# ?------------Comparision--------------#
# todo: 3. ["A","B"] == ["A","B"] --> True
# todo: 4. ["A","B"] >  ["A","B"] --> False


numbers = [4, 2, 5, 3, 1]
print('Max:- ', max(numbers))
print('Min:- ', min(numbers))
print('Sum:- ', sum(numbers))
print('Len:- ', len(numbers))

# todo: all(): returns True if all values are True
print('All:- ', all(numbers))
print('All:- ', all([1, 0, 2]))
print('All:- ', all(['a', '', 'b']))
print('All:- ', all(['a', 'c', 'b']))

# todo: any(): returns True if one values are True
print('Any:- ', any(numbers))
print('Any:- ', any([1, 0, 2]))
print('Any:- ', any(['a', '', 'b']))
print('Any:- ', any(['a', 'c', 'b']))
print('Any:- ', any([0, 0, 0]))

# todo: .count(): returns how many times a value appears in the list
print('Count:- ', numbers.count(5))

# todo: .index(): returns the position of the first occurrence of a value
print('Index:- ', numbers.index(5))

# todo: Use of in : Check if a value exists in a sequence
lis = ['a', 'b', 'c','d']

print('c present in list1: ', 'c' in lis)
print('e present in list1: ', 'e' in lis)

# todo: Use of is : Check if same or not
list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]

print('list1 or list2 same: ', list1 is list2)
print('list1 or list2 same: ', not list1 is list2)

list2 = list1

print('list1 or list2 same: ', list1 is list2)
print('list1 or list2 same: ', not list1 is list2)

# todo: Use of operators:

list1 = [1,3,5]
list2 = [1,3,5]
print('lists are same: ',list1 == list2)
print('lists1 is greater than: ',list1 > list2)

list1 = [2,3,5]
print('lists1 is greater than: ',list1 > list2)
