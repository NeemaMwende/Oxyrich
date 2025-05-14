# squares = []
# for  x in range(10):
#     squares.append(x**2)
# print(squares)

# squares = list(map(lambda x: x**2, range(10)))
# squares = [x**2 for x in range(10)]

# Start with an initial list
# fruits = ['apple', 'banana', 'cherry']
# print("Initial list:", fruits)

# # append(x): Add an item to the end
# fruits.append('orange')
# print("After append('orange'):", fruits)

# # extend(iterable): Extend with multiple items
# fruits.extend(['mango', 'grape'])
# print("After extend(['mango', 'grape']):", fruits)

# # insert(i, x): Insert at index
# fruits.insert(2, 'kiwi')
# print("After insert(2, 'kiwi'):", fruits)

# # remove(x): Remove by value
# fruits.remove('banana')
# print("After remove('banana'):", fruits)

# # pop([i]): Remove by index
# last = fruits.pop()
# print("After pop() (removed '{}'):".format(last), fruits)

# second_item = fruits.pop(1)
# print("After pop(1) (removed '{}'):".format(second_item), fruits)

# # index(x[, start[, end]]): Find index of item
# idx = fruits.index('mango')
# print("Index of 'kiwi':", idx)

# # count(x): Count occurrences
# fruits.append('apple')
# count_apples = fruits.count('apple')
# print("After appending another 'apple':", fruits)
# print("Count of 'apple':", count_apples)

# # sort(): Sort the list
# fruits.sort()
# print("After sort():", fruits)

# # reverse(): Reverse the list
# fruits.reverse()
# print("After reverse():", fruits)

# # copy(): Shallow copy
# copied_fruits = fruits.copy()
# print("Copied list:", copied_fruits)

# # clear(): Clear all elements
# fruits.clear()
# print("After clear():", fruits)

# vec = [-4, -2, 0, 2, 4]
# # create a new list with the values doubled
# [x*2 for x in vec]

# # filter the list to exclude negative numbers
# [x for x in vec if x >= 0]

# # apply a function to all the elements
# [abs(x) for x in vec]

# # call a method on each element
# freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# [weapon.strip() for weapon in freshfruit]

# # create a list of 2-tuples like (number, square)
# [(x, x**2) for x in range(6)]

# the tuple must be parenthesized, otherwise an error is raised
# [x, x**2 for x in range(6)]
#   File "<stdin>", line 1
#     [x, x**2 for x in range(6)]
#      ^^^^^^^
# SyntaxError: did you forget parentheses around the comprehension target?
# flatten a list using a listcomp with two 'for'
# vec = [[1,2,3], [4,5,6], [7,8,9]]
# [num for elem in vec for num in elem]

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
# [[row[i] for row in matrix] for i in range(4)]

# 1. Lists = mutable, ordered, allows duplicates
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]

# 2. Tuple = immutable , ordered, allows duplicates
my_tuple = (1, 2, 3)
print(my_tuple[1])

# 3. Set = mutable, unordered , no duplicates allowed, stores unique items
my_set = {1, 2, 2, 3}
my_set.add(4)
print(my_set)  # {1, 2, 3, 4}

# 4. Dictionary = mutable, unordered, no duplicates allowed, stores key-value pairs
my_dict = {'name': 'Neema', 'age': 23}
print(my_dict['name'])  # Neema
my_dict['location'] = 'Kitui'
print(my_dict)  # {'name': 'Neema', 'age': 23, 'location': 'Kitui'}
my_dict['age'] = 24
print(my_dict)  # {'name': 'Neema', 'age': 24, 'location': 'Kitui'}

# 5. String = immutable, ordered, allows duplicates, slicing, indexing
my_str = "Hello"
print(my_str[0])  # H