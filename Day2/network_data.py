# 정수를 제곱하는 함수 정의
def square(x):
    return x ** 2

# 함수 호출: 2의 제곱 = 4 출력
print(square(x=2))

# 정수 리스트 생성
v1 = [1, 2, 3, 4]

# 리스트 전체를 square 함수에 map으로 적용 (제곱 계산)
result = map(square, v1)

# map 객체 자체 출력 (메모리 주소)
print(result)

# map 객체 반복 → 제곱 결과 출력: 1 4 9 16
for i in result:
    print(i, end=" ")
print()  # 줄바꿈

# 람다 함수를 사용한 제곱 계산
need1 = lambda x: x ** 2

# map과 lambda를 이용해 [2,4,6,8]의 제곱 리스트 만들기
result2 = list(map(need1, [2, 4, 6, 8]))
print(result2)  # 출력: [4, 16, 36, 64]

# 한 줄짜리 lambda로 세제곱(cube) 리스트 만들기
result3 = list(map(lambda x: x ** 3, [2, 4, 6, 8, 10]))
print(result3)  # 출력: [8, 64, 216, 512, 1000]

# filter를 이용해 0.6보다 큰 숫자만 추출
network = list(filter(lambda x: x > 0.6, [0.1, 0.7, 0.8, 0.3, 0.9, 1.0]))
print(network)  # 출력: [0.7, 0.8, 0.9, 1.0]

# 위에서 필터링한 결과를 파일에 저장
NT_file = open("network_data.txt", 'w', encoding='utf-8')
NT_file.write(str(network))  # 리스트를 문자열로 변환하여 저장
NT_file.close()  # 파일 닫기 (반드시 필요)
