class Human:
    head = True

    # def __init__(self):
    #     self.about()

    def say_hello(self):
        print('Дарова!')


class Student(Human):
    head = False

    def about(self):
        print('Я студент')
    #
    # def say_hello(self):
    #     print('Дарова!')


class Teacher(Human):
# def say_hello(self):
#     print('Дарова!')
    pass

# human_adam = Human()
#
student_adam = Student()
teacher_alex = Teacher()
# print(human_adam.head)
# print(student_adam.head)
# student_adam.about()
student_adam.say_hello()
teacher_alex.say_hello()