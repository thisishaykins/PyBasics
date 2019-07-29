is_hot = True
is_cold = True

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("it's a cold day")
    print("Wear warm cloth")
else:
    print("It's a lovely day")

print("Enjoy your day")
print("  ")

price = 1000000
credit = False

if credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down Payment is ${down_payment}")