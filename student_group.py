class GroupLimitExceededError(Exception):
    """Виняток, який виникає, коли група перевищує ліміт студентів."""
    pass

class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}"

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Record Book: {self.record_book}"

class Group:
    def __init__(self, number):
        self.number = number
        self.group = []  # Використовуємо список замість множини

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupLimitExceededError("Cannot add more than 10 students to the group.")
        self.group.append(student)  # Додаємо студента в список

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join([str(student) for student in self.group])
        return f'Group number: {self.number}\n{all_students}'

# Створюємо студентів вручну
st1 = Student('Male', 21, 'John', 'Smith', 'AN101')
st2 = Student('Female', 22, 'Emily', 'Johnson', 'AN102')
st3 = Student('Male', 23, 'Michael', 'Williams', 'AN103')
st4 = Student('Female', 24, 'Olivia', 'Brown', 'AN104')
st5 = Student('Male', 25, 'Daniel', 'Davis', 'AN105')
st6 = Student('Female', 26, 'Sophia', 'Miller', 'AN106')
st7 = Student('Male', 27, 'Ethan', 'Wilson', 'AN107')
st8 = Student('Female', 28, 'Charlotte', 'Moore', 'AN108')
st9 = Student('Male', 29, 'James', 'Taylor', 'AN109')
st10 = Student('Female', 30, 'Ava', 'Anderson', 'AN110')
st11 = Student('Male', 31, 'William', 'Thomas', 'AN111')  # Цей студент перевищить ліміт

# Тестування
gr = Group('PD1')

# Додаємо студентів
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)

print(gr)

# Спробуємо додати 11-го студента
try:
    gr.add_student(st11)
except GroupLimitExceededError as e:
    print(f"Error: {e}")

print("\nFinal group:")
print(gr)
