class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal):
    # pass
    def bark(self):
        print("Dogs loves Barking in every situation")


class Cat(Mammal):
    def be_annoying(self):
        print("Cats are kinda annoying general")


dog1 = Dog()
dog1.walk()

cat = Cat()
cat.be_annoying()