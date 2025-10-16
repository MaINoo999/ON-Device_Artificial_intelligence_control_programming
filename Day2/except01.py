try:
    # 사용자로부터 정수 입력을 받음
    number_input_a = int(input("정수 입력> "))  # 예: "10" 입력 시 → 10으로 변환

    # 반지름 출력
    print("원의 반지름:", number_input_a)

    # 원의 둘레 계산: 2πr
    print("원의 둘레:", 2 * 3.14 * number_input_a)

    # 원의 넓이 계산: πr²
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)

# 예외 발생 시 실행되는 블록
except Exception as exception:
    # 예외의 자료형 출력 (예: <class 'ValueError'>)
    print("type(exception)", type(exception))

    # 예외 메시지 출력 (예: invalid literal for int() with base 10: 'abc')
    print("exception", exception)
