class Student:
    # 클래스 변수: 모든 Student 객체가 공유하는 변수
    count = 0

    def __init__(self, name, korean, math, english, science):
        # 생성자 메서드: 객체가 생성될 때 호출되어
        # 학생 이름과 점수를 각각 저장함
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

        # Student 클래스의 count 변수 1 증가
        # 즉, 생성된 학생 수를 누적 카운트
        Student.count += 1

        # 현재 몇 번째 학생이 생성되었는지 출력
        print("{}번째 학생이 생성되었습니다.".format(Student.count))

# 여러 명의 학생 객체를 리스트에 생성
students = [
    Student("가", 87, 98, 78, 89),
    Student("나", 65, 48, 86, 99),
    Student("다", 90, 80, 70, 100),
    Student("라", 70, 100, 100, 100),
    Student("마", 100, 100, 100, 100),
    Student("바", 100, 100, 100, 100)
]

print()  # 빈 줄 출력

# 지금까지 생성된 총 학생 수 출력
print("현재 생성된 총 학생 수는 {}명입니다.".format(Student.count))
