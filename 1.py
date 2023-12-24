class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self) -> str:
        grades = []
        for cg in self.grades.values():
            grades.extend(cg)
        avg_grade = sum(grades) / len(grades) if len(grades) > 0 else 0
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {avg_grade}\n"
            f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
            f"Завершенные курсы: {', '.join(self.finished_courses)}"
        )

    def add_finish_course(self, course_name):
        if course_name in self.courses_in_progress:
            self.courses_in_progress.remove(course_name)
        self.finished_courses.append(course_name)

    def add_lecturer_grade(self, lecturer, course, grade):
        if (
            isinstance(lecturer, Lecturer)
            and course in lecturer.courses_attached
            and course in self.courses_in_progress
        ):
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self) -> str:
        grades = []
        for cg in self.grades.values():
            grades.extend(cg)
        avg_grade = sum(grades) / len(grades) if len(grades) > 0 else 0
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {avg_grade}"
        )


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self) -> str:
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        if (
            isinstance(student, Student)
            and course in self.courses_attached
            and course in student.courses_in_progress
        ):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"


def get_avg_grade(students, course_name):
    grades = []
    for student in students:
        for k, v in student.grades.items():
            if k != course_name:
                continue
            grades.extend(v)
    return sum(grades) / len(grades) if len(grades) > 0 else 0


# students
student1 = Student("Андрей", "Крылов", "муж")
student1.courses_in_progress += ["Python", "Java"]
student1.add_finish_course("SQL")
student2 = Student("Анна", "Смирнова", "жен")
student2.courses_in_progress += ["Python", "Java"]
student2.add_finish_course("C#")
student2.add_finish_course("Java")

# lecturers
lecturer1 = Lecturer("Михаил", "Новиков")
lecturer1.courses_attached += ["Python", "C#"]
lecturer2 = Lecturer("Сергей", "Квашнин")
lecturer2.courses_attached += ["Java"]

# reviewers
reviewer1 = Reviewer("Дмитрий", "Колесников")
reviewer1.courses_attached += ["Python", "C#"]
reviewer2 = Reviewer("Виолетта", "Лейловна")
reviewer2.courses_attached += ["Python", "Java"]


reviewer1.rate_hw(student1, "Python", 10)
reviewer1.rate_hw(student1, "Python", 7)
reviewer1.rate_hw(student2, "Python", 9)
reviewer2.rate_hw(student1, "Java", 9)
reviewer2.rate_hw(student2, "Python", 4)

student1.add_lecturer_grade(lecturer1, "Python", 10)
student1.add_lecturer_grade(lecturer2, "Java", 9)
student2.add_lecturer_grade(lecturer1, "Python", 7)
student2.add_lecturer_grade(lecturer2, "Java", 5)

students = [student1, student2]
lecturers = [lecturer1, lecturer2]

print(f"Средняя оценка студентов за курс Python: {get_avg_grade(students, 'Python')}")
print(f"Средняя оценка лекторов за курс Python: {get_avg_grade(lecturers, 'Python')}")
