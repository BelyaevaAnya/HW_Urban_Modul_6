class Human:
    def __init__(self, name, group):
        self.name = name
        super().__init__(group)
        super().about()

    def info(self):
        print(f'Привет! Меня зовут {self.name}')


# Миксины
class StudentGroup:
    def __init__(self, group):
        self.group = group

    def about(self):
        print(f'{self.name} учится в группе {self.group}')


class Student(Human, StudentGroup):
    def __init__(self, name, place, group):
        super().__init__(name, group)
        self.place = place
        super().info()


# human = Human('Денчик')
# print(human.name)
student = Student('Максон', 'Урбан', 'Питон')
student.about()
# Иерархическая цепь наследования
print(Student.mro())
