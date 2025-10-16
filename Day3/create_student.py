# (선택) 상속할 부모 클래스 Person 정의
class Person:
    def __init__(self):
        print("Person 생성자 호출")

# Student 클래스 정의
class Student(Person):  # Person 클래스를 상속받음
    def __init__(self, name, korean, math, english, science):
        super().__init__()  # 부모 클래스 생성자 호출
        print("Student 생성자 호출")
        # 학생 정보 초기화
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def __del__(self):
        # 객체가 삭제될 때 호출됨 (보통 정리 작업에 사용)
        print(f"{self.name} 학생 객체가 메모리에서 삭제됩니다.")

# Karl이라는 학생 객체 생성
karl = Student(name="Karl", math=100, korean=90, english=100, science=90)

# Karl의 수학 점수 출력
print("Karl의 수학 점수:", karl.math)  # 출력: 100

# 여러 명의 학생 객체를 리스트로 생성
student = [
    Student("가", 87, 98, 78, 89),
    Student("나", 65, 48, 86, 99),
    Student("다", 90, 80, 70, 100),
    Student("라", 70, 100, 100, 100),
    Student("마", 100, 100, 100, 100),
    Student("바", 100, 100, 100, 100)
]

# 첫 번째 학생의 정보 출력
print("첫 번째 학생 정보:")
print("이름:", student[0].name)
print("국어:", student[0].korean)
print("수학:", student[0].math)
print("영어:", student[0].english)
print("과학:", student[0].science)
