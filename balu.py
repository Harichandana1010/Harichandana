class Student:
    school_name = 'ABC school'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print('Student:', self.name, self.age)
        print('School:', self.school_name)
    @classmethod
    def change_school(cls, name):
        print('Previous school name:', cls.school_name)
        cls.school_name = name
        print('School name changed to:', cls.school_name)
    @staticmethod
    def find_notes(subject_name):
        return ['Chapter 1', 'Chapter 2', 'Chapter 3']
jessa = Student('Jessa', 18)
jessa.show()
Student.change_school('XYZ school')
s1 = Student.find_notes('Maths')
print(s1)