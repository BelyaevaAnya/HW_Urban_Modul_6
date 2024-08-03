class _Human:
    head = True
    _legs = True
    __arms = True

    def say_hello(self):
        print('Дарова!')

    def about(self):
        print(self.head)
        print(self._legs)
        print(self.__arms)


class Student(_Human):
    arms = False
    pass
    # head = False
    #
    # def about(self):
    #     print('Я студент')


class Teacher(_Human):
    pass


human = _Human()
human.about()
# True
# True
# True
student = Student()
student.about()
# True
# True
# True
print(dir(human))
# ['_Human__arms', '__class__', '__delattr__', '__dict__', '__dir__',
# '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__',
# '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__',
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
# '__str__', '__subclasshook__', '__weakref__', '_legs', 'about', 'head', 'say_hello']
# __arms в начале
# __arms - имя защищенное от переопределения
print(dir(student))
# ['_Human__arms', '_Student__arms', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
#  '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
#  '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
#  '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_legs', 'about', 'head', 'say_hello']
# __arms - есть и у класса Student и у класса Human
print(student._Human__arms)  # => True
# Human.__arms и student.arms(таких атрибутов не существует)
