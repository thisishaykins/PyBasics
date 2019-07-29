try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(f"Your is {age} and your risk income is valued at {risk}")
except ZeroDivisionError:
    print("Age can not Zero")
except ValueError:
    print('Invalid value')