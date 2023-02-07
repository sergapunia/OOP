class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _aver_rating(self):
        _sum = 0
        _counter = 0
        for value in self.grades.values():
            for i in value:
                _sum += i
                _counter += 1
            return round(_sum / _counter, 2)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {self._aver_rating()}\nКурсы в процессе изучения: {",".join(self.courses_in_progress)}\nЗавершенные курсы: {"".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if isinstance(other, Student):
            return self._aver_rating() > other._aver_rating()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_in_progress = []

    def _aver_rating(self):
        _sum = 0
        _counter = 0
        for value in self.grades.values():
            for i in value:
                _sum += i
                _counter += 1
            return round(_sum / _counter, 2)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._aver_rating()}'
        return res

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self._aver_rating() > other._aver_rating()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия:{self.surname}'
        return res

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def summ(people_lst, course):
    lst = []
    for i in people_lst:
        lst += i.grades[course]
    a = sum(lst) / len(lst)
    print(a)

best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

some_student = Student('Mara', 'Kolet', 'female')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']

some_reviewer = Reviewer('Peter', 'Buddy')
some_reviewer.courses_attached += ['Python']

some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 9)

best_lecturer = Lecturer('Tom', 'Raimy')
best_lecturer.courses_in_progress += ['Python']

some_student.courses_attached += ['Python']

some_student.rate_hw(best_lecturer, 'Python', 9)
some_student.rate_hw(best_lecturer, 'Python', 10)
some_student.rate_hw(best_lecturer, 'Python', 9)
some_student.rate_hw(best_lecturer, 'Python', 9)

some_lecturer = Lecturer('Sam', 'Raimy')
some_lecturer.courses_in_progress += ['Python']

some_student.rate_hw(some_lecturer, 'Python', 9)
some_student.rate_hw(some_lecturer, 'Python', 8)
some_student.rate_hw(some_lecturer, 'Python', 9)
some_student.rate_hw(some_lecturer, 'Python', 9)

print(f'Преподователь \n{best_lecturer}')
print()
print(f'Преподователь \n{some_lecturer}')
print()
print(f'Студент \n{best_student}')
print()
print(f'Студент \n{some_student}')
print()
print(f'Ревьюрер \n{some_reviewer}')
print()

print(best_lecturer.__lt__(some_lecturer))
print()
print(best_student.__lt__(some_student))
print()


summ([best_student, some_student], 'Python')
summ([best_lecturer, some_lecturer], 'Python')