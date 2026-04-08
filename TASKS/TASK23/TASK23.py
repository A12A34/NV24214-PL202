class Student:
    def __init__(self, nvno, name, student_class):
        self.nvno = nvno
        self.name = name
        self.student_class = student_class

    def learning(self):
        print(f"I belong to the class {self.student_class} learning Programming Language")


s1 = Student("NV001", "Ali", "XII")
s1.learning()
