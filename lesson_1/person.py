class Person:

    race = "Human"

    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello! My name is", self.name)

    def __str__(self):
        return self.race + " named " + self.name


john = Person("John")
print(john)
john.greet()

Person.race = "Alien"
paul = Person("Paul")

print(john)
print(paul)
