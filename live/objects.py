import random

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


class Student(Person):

    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def greet(self, another_person=None):

        super().greet()
        print("I study ", self.subject)

class Professor(Person):

    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def greet(self, another_person=None):

        super().greet()

        print("I teach ", self.subject)

class Abomination(Student, Professor):
    pass

jack = Student("Jack", 21, "JMC")
jack.grow()
print(jack.age)
tony = Professor("Tony", 55, "Programming")
# jack.greet()
tony.greet()
a = Abomination("Abom", 20, "something")
a.greet()
