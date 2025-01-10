class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, floors, material):
        self.name = name
        self.floors = floors
        self.material = material

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")


house1 = House("Дом в деревне", 2, "Дерево")
house2 = House("Коттедж", 3, "Кирпич")
house3 = House("Небоскрёб", 50, "Стекло")

print(House.houses_history)

del house2

print(House.houses_history)
