number_of_classes = 10
classes = []

class Class:
    def __init__(self, class_id, students):
        self.class_id = class_id
        self.students= students


class Student:
    def __init__(self, enrollment, present_in_exam):
        self.enrollment = enrollment
        self.present_in_exam = present_in_exam


for i in range(number_of_classes):
    class_id = input("Identificação da turma: ")
    number_of_students = input(int("Número de estudantes: "))
    a_class = Class(get_class_id(), number_of_students)
    classes.append(a_class)
