# 빈 딕셔너리(dictionary)를 생성
dictionary = dict()

# 숫자들이 들어있는 리스트
numbers = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]

# numbers 리스트를 순회하면서 각 숫자의 등장 횟수를 딕셔너리에 저장
for number in numbers:
    # numbers.count(number): 리스트에서 해당 숫자가 몇 번 나오는지 세서 딕셔너리에 저장
    dictionary[number] = numbers.count(number)

# 딕셔너리에 저장된 키의 개수(=중복 제거된 숫자의 개수)를 출력
print(f"사용된 숫자의 종류는 {len(dictionary.keys())} 입니다.")

# 딕셔너리에 저장된 숫자별 등장 횟수를 출력 (참고용)
print(f"참고 : {dictionary}")
