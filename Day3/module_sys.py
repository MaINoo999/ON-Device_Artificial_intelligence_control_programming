import sys  # sys 모듈은 파이썬 인터프리터와 관련된 기능을 제공

# 명령줄 인수(argument)를 리스트로 출력
# 예: python script.py arg1 arg2 라고 실행하면 ['script.py', 'arg1', 'arg2'] 출력됨
print(sys.argv)

print("---")

# 현재 윈도우 운영체제의 버전 정보를 출력 (Windows에서만 사용 가능)
print("getwindowsversion():", sys.getwindowsversion())

print("---")

# 파이썬의 저작권 관련 정보 출력
print("copyright:", sys.copyright)

print("---")

# 현재 실행 중인 파이썬 인터프리터의 버전 정보 출력
print("version:", sys.version)

# 프로그램을 강제로 종료 (아래 코드가 더 있어도 실행되지 않음)
sys.exit()
