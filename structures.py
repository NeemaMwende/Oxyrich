# squares = []
# for  x in range(10):
#     squares.append(x**2)
# print(squares)

# squares = list(map(lambda x: x**2, range(10)))
# squares = [x**2 for x in range(10)]

# Start with an initial list
fruits = ['apple', 'banana', 'cherry']
print("Initial list:", fruits)

# append(x): Add an item to the end
fruits.append('orange')
print("After append('orange'):", fruits)

# extend(iterable): Extend with multiple items
fruits.extend(['mango', 'grape'])
print("After extend(['mango', 'grape']):", fruits)

# insert(i, x): Insert at index
fruits.insert(2, 'kiwi')
print("After insert(2, 'kiwi'):", fruits)

# remove(x): Remove by value
fruits.remove('banana')
print("After remove('banana'):", fruits)

# pop([i]): Remove by index
last = fruits.pop()
print("After pop() (removed '{}'):".format(last), fruits)

second_item = fruits.pop(1)
print("After pop(1) (removed '{}'):".format(second_item), fruits)

# index(x[, start[, end]]): Find index of item
idx = fruits.index('mango')
print("Index of 'kiwi':", idx)

# count(x): Count occurrences
fruits.append('apple')
count_apples = fruits.count('apple')
print("After appending another 'apple':", fruits)
print("Count of 'apple':", count_apples)

# sort(): Sort the list
fruits.sort()
print("After sort():", fruits)

# reverse(): Reverse the list
fruits.reverse()
print("After reverse():", fruits)

# copy(): Shallow copy
copied_fruits = fruits.copy()
print("Copied list:", copied_fruits)

# clear(): Clear all elements
fruits.clear()
print("After clear():", fruits)
