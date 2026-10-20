class Animal:

    def __init__(self, name , species , age , gender):
        self.name = name
        self.species = species
        self.age = age
        self.gender = gender

    def get_info(self):
        return f"Name: {self.name}, Species: {self.species}, Age: {self.age}, Gender: {self.gender}"

    def speak(self):
        return "Some generic animal sound"

class Dog(Animal):

    def speak(self):
        print(super().speak())
        print("Woof! Woof!")

Dog1 = Dog("Buddy", "Dog", 3, "Male")
Dog1.speak()
