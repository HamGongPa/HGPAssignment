class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    
    def get_average(self):
        return self.get_sum() / 4

    def __str__(self):
        return f"{self.name}\t{self.get_sum()}\t{self.get_average()}"    

students = [
    Student(name = "윤인성", korean = 87, math = 98, english = 88, science = 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 95, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 95),
    Student("윤명월", 64, 88, 88, 95),
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    print(str(student))