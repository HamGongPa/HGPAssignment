def create_student(name, korean, math, english, science):
    return {
        "name": name,
        "korean": korean,
        "math": math,
        "english": english,
        "science": science
    }

students = [
    create_student("윤인성", 87, 98, 88, 95),
    create_student("연하진", 92, 98, 96, 98),
    create_student("구지연", 76, 96, 94, 90),
]

print("이름", "총점", "평균", sep="\t")

for student in students:
    score_sum = student["korean"]+student["math"]+ \
    student["english"] + student["science"]

    score_average = score_sum / 4
    print(student["name"], score_sum, score_average, sep="\t")