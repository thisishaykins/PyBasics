class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        print("You name is " + self.name)

    def getAge(self):
        print("You age is " + self.age)


p1 = Person("Akinshola", "30")

p1.getAge()
p1.getName()
