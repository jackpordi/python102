class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self, another_person=None):
        if another_person is None:
            print("Hello, my name is", self.name)
            print("I am ", self.age)
        else:
            print("Hello", another_person.name,
                  "My name is", self.name)
            print("I am ", self.age)


    def grow(self):
        self.age = self.age + 1

    def __repr__(self):
        return "A Person whose name is " + self.name

    def __eq__(self, other):
        return self.name == other.name and \
            self.age == other.age


jack1 = Person("Jack", 21)
jack2 = Person("Jack", 22)

print(jack1 == jack2)
