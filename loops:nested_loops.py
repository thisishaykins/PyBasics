"""
Adding one loop into another loop
"""
for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")

print("")
print("----------------------------")
print("")

numbers = [5, 2, 5, 2, 2]
for number in numbers:
    print(number * "*")

print("")
print("----------------------------")
print("")

numbers = [5, 2, 5, 2, 2]
for number in numbers:
    output = ''
    for count in range(number):
        output += '*'
    print(output)
