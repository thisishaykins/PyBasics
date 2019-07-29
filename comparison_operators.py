"""
If temperature is greater than 30
    it's a hot day
Otherwise if it's less than 10
    It's a cold day
Otherwise
    It's neither hot or cold
"""

temperature = 30

if temperature > 30:
    print("it's a hot day")
elif temperature < 30:
    print("it's a cold day")
else:
    print("It's not a hot day")

print(" ---------------------  ")
"""
If name is less than 3 characters long
    name must be at least 3 characters 
Otherwise if it's more than 50 characters long
    name can be minimum of 50 characters
Otherwise
    name look good!
"""

name = input("Enter your name? ")

if len(name) < 3:
    print("Ooooops, Name must be at least 3 characters")
elif len(name) > 50:
    print("Ooooops, Name must be a maximum of 50 characters")
else:
    print("Name look good! Proceed")