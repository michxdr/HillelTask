from student_group import Student, Group  # Імпортуємо класи з одного файлу

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')

gr.add_student(st1)
gr.add_student(st2)

# Виведення групи
print(gr)

# Перевірка, чи правильне порівняння студентів
assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
assert gr.find_student('Jobs2') is None

# Видалення студента
gr.delete_student('Taylor')

# Виведення після видалення
print(gr)  # Тепер має бути тільки один студент
