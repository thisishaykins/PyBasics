# Person
#   - name
#   - talk()

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")

haykins = Person("John Doe")
haykins.talk()

akin = Person("Akinshola Samel")
akin.talk()