class  Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} издает звук")

    def eat(self):
        print(f"{self.name} ест")

class Bird(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        print(f"{self.name} чирикает")

