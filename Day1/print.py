# "안녕"을 3번 출력하는 함수 정의
def print3_times():
    for _ in range(3):
        print("안녕")

# 함수 호출 → "안녕"이 3번 출력됨
print3_times()


# 값을 n번 출력하는 함수 정의
# value: 출력할 문자열 (기본값은 "Hello")
# n: 출력 횟수 (기본값은 1)
def print_n_times(value="Hello", n=1):
    for _ in range(n):
        print(value)

# 아래는 주석 처리된 예시들 (정상 동작)
# print_n_times(value="Hello", n=5)   # "Hello"를 5번 출력
# print_n_times(n=5, value="World")   # "World"를 5번 출력

# 함수 호출 (문제 발생!)
print_n_times(5)
