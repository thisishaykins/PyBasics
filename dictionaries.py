"""
Dictionary help to store key:values pairs. It's a robust, extremely important and has alot of application usage in the
real world
"""
customer = {
    "name": "John Doe",
    "age": 25,
    "is_verified": True
}
print(customer["name"])

customer["name"] = "Akinde Akinshola"
customer["birthdate"] = "March 1, 1994"
print(customer.get("name"))
print(customer.get("gender", "Male"))

print("")
print("----------------------------")
print("")

"""
Exercise: 
"""
phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}

output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)
