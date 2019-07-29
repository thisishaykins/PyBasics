names = ['John', 'Matthew', 'Ademi', 'Martins', 'Olamide']
names[0] = 'Jon'
print(names[:])

"""
Exercise goes here
"""

numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print(max)