class Animal:

    def sound(self):

        print("Animal Sound")


class Dog(Animal):

    def sound(self):

        print("Woof")


d = Dog()

d.sound()