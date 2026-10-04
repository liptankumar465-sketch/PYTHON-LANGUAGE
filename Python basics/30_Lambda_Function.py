import pattern
#! LAMBDA FUNCTION:
# ? 1: Create quick & custome logic.
# ? 2: One - line function.
# ? 3: Assist others
#   map(lambda, iterator)
#   filter(lambda, iterator)
#   sort(lambda, iterator)

#! Example:


def square(x): return x*x
print(square(4))

pattern.line()
#! Formate the parise:
print('Useing lambda in map()')
parise = ['$125.64', '$533.53', '$75.235', '$964.32']
formate_parise = map(lambda a: float(a.replace('$', '')), parise)
print('parise: ', parise)
print(list(formate_parise))

pattern.line()
#! Multiples of 3:
print('Useing lambda in filter()')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
multiples_of_three = filter(lambda x: x % 3 == 0, numbers)
print('numbers: ', numbers)
print('multiples of 3: ', list(multiples_of_three))
