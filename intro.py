class Student:
    def __init__(self, name, regNo, course, phone, fees):
        self.name = name
        self.regNo = regNo
        self.course = course
        self.phone = phone
        self.paidfees = fees

    def get_name_course(self):  # method
        print(self.name, "is undertaking", self.course, "course")

    def exam_card(self, minimum_fee=10000):
        if minimum_fee > self.paidfees:
            print("you won't seat for the exam pay for the remaining balance of", minimum_fee - self.paidfees)


s1 = Student("jeff angayo", "TUO01-", "python", "0791234", 5000)
print(s1.name)
print(s1.get_name_course())
print(s1.__str__())
print(s1.exam_card())
age = 5
"""inheritance"""


# attributes and methods are inherited
class Pupil(Student):
    """overriding"""

    # defining a method inside a class that inherited properties thus parent class is being overridden
    def __init__(self, location, name, regNo, course, phone, fees):
        super().__init__(name, regNo, course, phone, fees)
        self.location = location

    def getName_loc(self):
        return f"my name is {self.name} and am from {self.location}"


p1 = Pupil("vihiga", "jeff", "TUO1", "mcs", "0791234886", 5000)
print(p1.getName_loc())
