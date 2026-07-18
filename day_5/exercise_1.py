class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(self.name + " says 'Have you seen my updog?'")

    def describe(self):
        return self.name + " is a " + self.breed


dog1 = Dog("Barney", "Labrador")
dog2 = Dog("Max", "Poodle")

dog1.bark()
dog2.bark()

print(dog1.describe())
