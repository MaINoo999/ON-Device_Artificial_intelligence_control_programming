list_number = [52, 273, 32, 72, 100]  # 리스트에 정수 값들 저장

try:
    number_input = int(input("정수 입력>"))  # 사용자로부터 정수 입력 받기
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))  # 입력한 인덱스에 해당하는 리스트 요소 출력

    예외.발생해주세요()  # 의도적으로 예외를 발생시키기 위해서 (이 부분은 실제로 동작하지 않음)
except ValueError as exception:  # 사용자가 정수가 아닌 값을 입력했을 때 발생
    print("정수를 입력해주세요")  # 안내 메시지
    print(type(exception), exception)  # 예외의 타입과 메시지 출력
except IndexError as exception:  # 리스트 인덱스가 범위를 벗어난 경우 발생
    print("리스트의 인덱스를 벗어났습니다.")  # 안내 메시지
    print(type(exception), exception)  # 예외의 타입과 메시지 출력
except Exception as exception:  # 위의 예외 외에 다른 예외가 발생한 경우
    print("미리 파악하지 못한 예외가 발생")  # 안내 메시지
    print(type(exception), exception)  # 예외의 타입과 메시지 출력
