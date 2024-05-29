class Person:
    def __init__(self, name, age):
        self.name = name # attribute
        self.age = age # attribute
    def introduce(self): # method
        print(f"Hi my name is {self.name} and I am {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def introduce(self):
        # polymorphism because the method introduce() is overridden
        print(f"Hi my name is {self.name} and I am {self.age} years old. My grade is {self.grade}.")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def introduce(self):
        # print(f"Hi my name is {self.name} and I am {self.age} years old. My subject is {self.subject}.")
        super().introduce() # no polymorphism because we call the method introduce() of the superclass


my_person = Person("John", 15) # Create a Person object named x and print the value of x.
my_person.introduce() # Call the introduce method on the object.
my_student = Student("Pippo", 30, 10)
my_student.introduce()
my_teacher = Teacher("Pluto", 40, "Math")
my_teacher.introduce()
