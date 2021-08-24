"""
Создать класс Student.

Определить атрибуты:

- surname - фамилия
- name - имя
- group - номер группы
- average_score - средний балл

Определить методы:

- инициализатор __init__
- Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
  студентов по среднему баллу

Создать список из 5 объектов класса и вывести его отсортированным по возрастанию
и убыванию.

Вывести студентов, у которых средний балл больше 5
"""


class Student:
    surname: str
    name: str
    group: int
    average_score: int

    def __init__(self, surname: str, name: str, group: int, average_score: int):
        self.surname = surname
        self.name = name
        self.group = group
        self.average_score = average_score

    def __eq__(self, other):
        return self.average_score == other.average_score

    def __ne__(self, other):
        return self.average_score != other.average_score

    def __lt__(self, other):
        return self.average_score < other.average_score

    def __le__(self, other):
        return self.average_score <= other.average_score

    def __gt__(self, other):
        return self.average_score > other.average_score

    def __ge__(self, other):
        return self.average_score >= other.average_score

    def __str__(self):
        return self.name + self.surname


student1 = Student("Pupkin", "Vasya", 1, 5)
student2 = Student("Sexy", "Shmeksy", 2, 4)
student3 = Student("Hleb", "Kolbasa", 3, 8)
student4 = Student("UUU", "AAA", 4, 3)
student5 = Student("Vashe", "Zadrot", 5, 9)
stud_list = [student1, student2, student3, student4, student5]
stud_list.sort()
print(stud_list)
print(stud_list[0].average_score)
print(stud_list[1].average_score)
print(stud_list[2].average_score)
print(stud_list[3].average_score)
print(stud_list[4].average_score)
stud_list.sort(reverse=True)
print(stud_list)
print(stud_list[0].average_score)
print(stud_list[1].average_score)
print(stud_list[2].average_score)
print(stud_list[3].average_score)
print(stud_list[4].average_score)

for i in stud_list:
    if i.average_score > 5:
        print(i)
