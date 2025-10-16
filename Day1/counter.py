# 함수 호출 횟수를 세기 위한 전역 변수
counter = 0


# 피보나치 수열을 계산하는 재귀 함수
def f(n: int) -> int:
    print(f'fibonacci number {n}')  # 현재 계산 중인 n을 출력

    global counter  # 전역 변수 counter 사용 선언
    counter += 1  # 함수가 호출될 때마다 1씩 증가

    # 피보나치 수열의 첫 두 항은 1로 고정
    if n in (1, 2):
        return 1
    else:
        # 피보나치 재귀: F(n) = F(n-1) + F(n-2)
        result = f(n - 2) + f(n - 1)
        return result


# 피보나치 수열의 10번째 항을 계산하고 출력
print(f(10))

# 총 몇 번 함수가 호출되었는지 출력
print(f'counter: {counter}')
