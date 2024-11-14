class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender 
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Этот лектор не ведет курс!"

    def get_average_grade(self):
        if not self.grades:
            return 0
        total_grades = sum(sum(grades) for grades in self.grades.values())
        total_subjects = sum(len(grades) for grades in self.grades.values())
        return total_grades / total_subjects if total_subjects else 0

    def __eq__(self, other):
        if not isinstance(other, Student):
            return "Сравнение возможно только между Студентами"
        return self.get_average_grade() == other.get_average_grade()

    def __lt__(self, other):
        if not isinstance(other, Student):
            return "Сравнение возможно только между Студентами"
        return self.get_average_grade() < other.get_average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return "Сравнение возможно только между Студентами"
        return self.get_average_grade() > other.get_average_grade()

    def __str__(self):
        average_grade = self.get_average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return (f"Студент: {self.name} {self.surname}\n"
                f"Средняя оценка: {average_grade:.2f}\n"
                f"Курсы в процессе: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")


class Lecturer:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_attached = []
        self.grades = {}

    def get_average_grade(self):
        if not self.grades:
            return 0
        total_grades = sum(sum(grades) for grades in self.grades.values())
        total_subjects = sum(len(grades) for grades in self.grades.values())
        return total_grades / total_subjects if total_subjects else 0

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return "Сравнение возможно только между Лекторами"
        return self.get_average_grade() == other.get_average_grade()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return "Сравнение возможно только между Лекторами"
        return self.get_average_grade() < other.get_average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return "Сравнение возможно только между Лекторами"
        return self.get_average_grade() > other.get_average_grade()

    def __str__(self):
        average_grade = self.get_average_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {average_grade:.2f}")


class Reviewer:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender

    def rate_student(self, student, course, grade):
        if isinstance(student, Student):
            if course in student.courses_in_progress or course in student.finished_courses:
                if course in student.grades:
                    student.grades[course].append(grade)
                else:
                    student.grades[course] = [grade]
            else:
                return "Этот курс не находится в списке курсов студента."
        else:
            return "Это не студент!"
        
    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}")


def get_average_grade_for_course(students, course):  # Вычисляем среднюю оценку за курс у Студентов
    total_grades = 0
    total_students = 0
    
    for student in students:
        if course in student.grades:
            total_grades += sum(student.grades[course])
            total_students += len(student.grades[course])
    
    return total_grades / total_students if total_students > 0 else 0


def get_average_grade_for_lecturers(lecturers, course):  # Вычисляем среднюю оценку за курс у Лекторов
    total_grades = 0
    total_lecturers = 0
    
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades += sum(lecturer.grades[course])
            total_lecturers += len(lecturer.grades[course])
    
    return total_grades / total_lecturers if total_lecturers > 0 else 0



# Примеры использования

student1 = Student("Иван", "Исаев", "м")
student2 = Student("Катерина", "Петрова", "ж")

lecturer1 = Lecturer("Павел", "Молибог", "м")
lecturer2 = Lecturer("Мария", "Суркова", "ж")

reviewer1 = Reviewer("Алексей", "Наглый", "м")
reviewer2 = Reviewer("Ольга", "Зверькова", "ж")

student1.courses_in_progress.append("Python")
student2.courses_in_progress.append("Python")
student1.finished_courses.append("Математика")
student2.finished_courses.append("Физика")

lecturer1.courses_attached.append("Python")
lecturer2.courses_attached.append("Python")

reviewer1.rate_student(student1, "Python", 10)
reviewer1.rate_student(student2, "Python", 9)

student1.rate_lecture(lecturer1, "Python", 8)
student2.rate_lecture(lecturer2, "Python", 7)


print(student1)
print()
print(student2)
print()
print(lecturer1)
print()
print(lecturer2)
print()
print(reviewer1)
print()
print(reviewer2)
print()

# Сравнение студентов
print(student1 > student2)  # True или False в зависимости от оценок
print()
print(student1 < student2)  
print()
# Сравнение лекторов
print(lecturer1 > lecturer2)  # True или False в зависимости от оценок
print()
print(lecturer1 < lecturer2)  
print()

# Примеры использования функции 
students = [student1, student2]

average_grade_python = get_average_grade_for_course(students, "Python")
print(f"Средняя оценка Cтудентов за курс 'Python': {average_grade_python:.2f}")
print()

# Примеры использования функции
lecturers = [lecturer1, lecturer2]

average_grade_python_lecturers = get_average_grade_for_lecturers(lecturers, "Python")
print(f"Средняя оценка Лекторов за курс 'Python': {average_grade_python_lecturers:.2f}")
print()