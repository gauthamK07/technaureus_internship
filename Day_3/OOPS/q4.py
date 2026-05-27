class animal():
    def sound(self):
        print("Animal sound")

class dog(animal):
    def sound(self):
        print("Woof")

class cat(animal):
    def sound(self):
        print("Meow")

class cow(animal):
    def sound(self):
        print("Moo")


animal().sound()
dog().sound()
cat().sound()
cow().sound()