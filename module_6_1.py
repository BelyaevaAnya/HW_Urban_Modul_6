class Plant:
    edible = False

    def __init__(self, name: str):
        self.name = name


class Animal:
    alive = True
    fed = False

    def __init__(self, name: str):
        self.name = name

    def eat(self, food: Plant):
        if food.edible:
            self.fed = True
            print(f'{self.name} съел {food.name}')
        else:
            self.alive = False
            print(f'{self.name} не стал есть {food.name}')


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
