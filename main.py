class Student:
    students_obj = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.students_obj.append(self)

    def rate_lc(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if 1 <= grade <= 10:
                if course in lector.grades:
                    lector.grades[course] += [grade]
                else:
                    lector.grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            return 'Ошибка'

    def _abs_score_student(self):
        sum_score, count_score = 0, 0
        for score in self.grades.values():
            for i in score:
                sum_score += i
                count_score += 1

        abs_score = sum_score / count_score
        return abs_score

    def _list_courses(self):
        cources_str = ",".join(self.courses_in_progress)
        return cources_str

    def _list_finished_courses(self):
        finished_courses_str = ', '.join(self.finished_courses)
        return finished_courses_str

    def __str__(self):
        return f'''
            Имя: {self.name}
            Фамилия: {self.surname}
            Средняя оценка за домашние задания: {self._abs_score_student():.1f}
            Курсы в процессе изучения: {self._list_courses()}
            Завершенные курсы: {self._list_finished_courses()}
            '''


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    lectors_obj = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        Lecturer.lectors_obj.append(self)

    def _abs_score_lector(self):
        sum_score, count_score = 0, 0
        for score in self.grades.values():
            for i in score:
                sum_score += i
            count_score = len(score)

        abs_score = sum_score / count_score
        return abs_score

    def __str__(self):
        return f'''
            Имя: {self.name}
            Фамилия: {self.surname}
            Средняя оценка за лекции: {self._abs_score_lector():.1f}'''

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('His is not a Lector')
            return
        return self._abs_score_lector() < other._abs_score_lector()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'''
            Имя: {self.name}
            Фамилия: {self.surname}'''

def calc_abs_score(objects, course):
    sum_score, count_score = 0, 0
    for obj in objects:
        for course_name, score in obj.grades.items():
            if course_name == course:
                sum_score += sum(i for i in score)
                count_score += len(score)
    abs_score = sum_score / count_score
    return abs_score


best_student = Student('Andrey', 'Glumov', 'Male')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['C++']

some_student = Student('Cara', 'Devil', 'Famale')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['C++']

some_reviewer = Reviewer('Robo', 'Cop')
some_reviewer.courses_attached += ['Python']
some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 5)

some_reviewer2 = Reviewer('Bat', 'Man')
some_reviewer2.courses_attached += ['Git']
some_reviewer2.rate_hw(best_student, 'Git', 9)
some_reviewer2.rate_hw(some_student, 'Git', 10)

some_lector = Lecturer('Termi', 'Nator')
some_lector.courses_attached += ['Python']
some_lector2 = Lecturer('T', '1000')
some_lector2.courses_attached += ['Git']

best_student.rate_lc(some_lector, 'Python', 10)
best_student.rate_lc(some_lector2, 'Python', 5)
best_student.rate_lc(some_lector, 'Git', 10)
best_student.rate_lc(some_lector2, 'Git', 9)
some_student.rate_lc(some_lector, 'Git', 10)
some_student.rate_lc(some_lector2, 'Git', 9)
best_student.rate_lc(some_lector, 'Git', 1)
best_student.rate_lc(some_lector2, 'Git', 1)

print(some_reviewer)
print(some_lector)
print(some_lector2)
print(some_lector.__lt__(some_lector2))
print(some_lector < some_lector2)
print(some_lector > some_lector2)
print(best_student)

print(f'{calc_abs_score(Student.students_obj, "Git"):.1f}')
print(f'{calc_abs_score(Lecturer.lectors_obj, "Git"):.1f}')
print(f'{calc_abs_score(Lecturer.lectors_obj, "Python"):.1f}')
