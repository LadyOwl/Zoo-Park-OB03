import json

class  Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} издает звук")

    def eat(self):
        print(f"{self.name} ест")

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "name": self.name,
            "age": self.age,
            **(
                {"color": self.color} if hasattr(self, "color") else
                {"fur_color": self.fur_color} if hasattr(self, "fur_color") else
                {"is_venomous": self.is_venomous})}


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

    def to_dict(self):
        return {"type": "Zookeeper", "name":self.name}

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animals(self, animal):
        print(f"{self.name} лечит {animal.name}")

    def to_dict(self):
        return {"type": "Veterinarian", "name":self.name}

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

    def save_to_file(self, filename="zoo_data.json"):
        data = {
            "zoo_name": self.name,
            "animals": [animal.to_dict() for animal in self.animals],
            "staff": [person.to_dict() for person in self.staff]
        }
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Данные зоопарка сохранены в {filename}")

    @classmethod
    def load_from_file(cls, filename="zoo_data.json"):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)

            zoo = cls(data["zoo_name"])

            for animal_data in data["animals"]:
                animal_type = animal_data["type"]
                if animal_type == "Bird":
                    animal = Bird(animal_data["name"], animal_data["age"], animal_data["color"])
                elif animal_type == "Mammal":
                    animal = Mammal(animal_data["name"], animal_data["age"], animal_data["fur_color"])
                elif animal_type == "Reptile":
                    animal = Reptile(animal_data["name"], animal_data["age"], animal_data["is_venomous"])
                zoo.animals.append(animal)

            for staff_data in data["staff"]:
                staff_type = staff_data["type"]
                if staff_type == "Zookeeper":
                    staff = Zookeeper(staff_data["name"])
                elif staff_type == "Veterinarian":
                    staff = Veterinarian(staff_data["name"])
                zoo.staff.append(staff)

            print(f"Зоопарк '{zoo.name}' успешно загружен из {filename}!")
            return zoo
        except FileNotFoundError:
            print(f"Файл {filename} не найден. Создан новый зоопарк.")
            return cls("Новый зоопарк")
        except json.JSONDecodeError:
            print(f"Ошибка чтения {filename}. Создан новый зоопарк.")
            return cls("Новый зоопарк")

if __name__ == "__main__":
    zoo = Zoo("Солнечный остров")

    parrot = Bird("Попугай", 3, "Красный")
    tiger = Mammal("Тигр", 5, "Оранжевый̆")
    snake = Reptile("Змея", 2, True)

    animals = [parrot, tiger, snake]
    animal_sound(animals)

    keeper = Zookeeper("Владимир")
    vet = Veterinarian("Ольга")

    zoo.add_animal(parrot)
    zoo.add_animal(tiger)
    zoo.add_animal(snake)

    zoo.add_staff(keeper)
    zoo.add_staff(vet)

    zoo.list_animals()
    zoo.list_staff()

    zoo.save_to_file("zoo_data.json")
    zoo = Zoo.load_from_file("zoo_data.json")
    zoo.list_animals()
    zoo.list_staff()




