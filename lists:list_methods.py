"""
Lists Methods or Lists Functions
"""
numbers = [5, 2, 1, 7, 4, 4, 20]
numbers.append(20)
numbers.insert(0, 10)
numbers.remove(5)
#numbers.clear()
numbers.pop(4)
numbers.index(2)
numbers.sort()
numbers.reverse()
numbers2 = numbers.copy()
print(numbers)
print(20 in numbers)
print(numbers.count(20))
print(numbers)
print(numbers2)

print("")
print("----------------------------")
print("")

"""
Exercise Section
`Write a program to remove the duplicates in a list`
"""

numericals = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for numeric in numericals:
    if numeric not in uniques:
        uniques.append(numeric)

uniques.sort()
print(uniques)



