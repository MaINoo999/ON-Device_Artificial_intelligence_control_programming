import sys

# 인수 개수 확인 (스크립트 이름 제외 최소 3개의 숫자 인수가 필요)
if len(sys.argv) < 4:
    print("사용법: python script.py 숫자1 숫자2 숫자3")
    sys.exit(1)  # 비정상 종료

try:
    # 정수로 변환 후 더하기
    total = int(sys.argv[1]) + int(sys.argv[2]) + int(sys.argv[3])
    print("합계:", total)
except ValueError:
    print("모든 인수는 정수여야 합니다.")
    sys.exit(1)

# Windows OS 버전 정보 출력
print("Windows 버전 정보:", sys.getwindowsversion())

# 파이썬 버전 정보 출력
print("Python 버전 정보:", sys.version_info)
