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

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} рычит")

class Reptile(Animal):
    def __init__(self, name, age, is_venomous):
        super().__init__(name, age)
        self.is_venomous = is_venomous

    def make_sound(self):
        print(f"{self.name} шипит")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

class Zookeeper:
    def __init__(self, name):
        self.name = name

    def feed_animals(self, animal):
        print(f"{self.name} кормит {animal.name}")

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animals(self, animal):
        print(f"{self.name} лечит {animal.name}")

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Добавлено животное: {animal.name} в зоопарк {self.name}")

    def add_staff(self, staff):
        self.staff.append(staff)
        print(f"Добавлен сотрудник: {staff.name} в зоопарк {self.name}")

    def list_animals(self):
        print(f"Животные в зоопарке {self.name}:")
        for animal in self.animals:
            info = f"- {animal.name} ({animal.age} лет)"
            if isinstance(animal, Bird):
                info += f", цвет: {animal.color}"
            elif isinstance(animal, Mammal):
                info += f", цвет шерсти: {animal.fur_color}"
            elif isinstance(animal, Reptile):
                info += f", является ядовитым: {animal.is_venomous}"
            print(info)

    def list_staff(self):
        print(f"Сотрудники в зоопарке {self.name}:")
        for staff in self.staff:
            print(f"- {staff.name}")

if __name__ == "__main__":

    parrot = Bird("Попугай", 3, "Красный")
    tiger = Mammal("Тигр", 5, "Оранжевый̆")
    snake = Reptile("Змея", 2, True)

    animals = [parrot, tiger, snake]
    animal_sound(animals)

    keeper = Zookeeper("Владимир")
    vet = Veterinarian("Ольга")

    zoo = Zoo("Солнечный остров")
    zoo.add_animal(parrot)
    zoo.add_animal(tiger)
    zoo.add_animal(snake)

    zoo.add_staff(keeper)
    zoo.add_staff(vet)

    zoo.list_animals()
    zoo.list_staff()




