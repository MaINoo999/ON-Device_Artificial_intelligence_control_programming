# Student 클래스 정의
class Student:
    def __init__(self, name, korean, math, english, science):
        # 생성자 메서드: 학생 객체가 생성될 때 호출되어
        # 이름과 네 과목 점수를 저장함
        self.name = name              # 학생 이름 저장
        self.korean = korean          # 국어 점수 저장
        self.math = math              # 수학 점수 저장
        self.english = english        # 영어 점수 저장
        self.science = science        # 과학 점수 저장

    def get_sum(self):
        # 학생의 총점 계산 메서드
        # 국어, 수학, 영어, 과학 점수를 모두 더해서 반환함
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        # 학생의 평균 점수 계산 메서드
        # 총점을 4과목으로 나누어 반환함
        return self.get_sum() / 4

    def to_string(self):
        # 학생의 정보를 문자열 형태로 반환하는 메서드
        # 이름, 총점, 평균을 탭(\t)으로 구분하여 리턴함
        return "{}\t{}\t{}".format(
            self.name,           # 학생 이름 출력
            self.get_sum(),      # 총점 출력
            self.get_average()   # 평균 출력
        )

# 여러 명의 Student 객체를 리스트로 생성
students = [
    Student("가", 87, 98, 78, 89),
    Student("나", 65, 48, 86, 99),
    Student("다", 90, 80, 70, 100),
    Student("라", 70, 100, 100, 100),
    Student("마", 100, 100, 100, 100),
    Student("바", 100, 100, 100, 100)
]

# 출력할 표의 헤더를 탭(\t)으로 구분해 출력
print("이름", "총점", "평균", sep="\t")

# students 리스트에 있는 각 학생 객체를 반복하면서
# to_string() 메서드를 사용해 한 줄씩 출력
for student in students:
    print(student.to_string())
