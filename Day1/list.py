# 숫자와 리스트가 섞여 있는 리스트
numbers = [1, 2, [3, 4], 5, [6, 7], [8, 9]]

# 중첩된 리스트를 풀어서 저장할 새로운 리스트
new_numbers = []

# numbers 리스트를 하나씩 순회
for number in numbers:
    # 요소가 리스트인 경우 (즉, [3, 4] 같은 경우)
    if type(number) is list:
        print("대상은 리스트 입니다.")
        # 그 리스트 안의 항목들을 하나씩 꺼내서 new_numbers에 추가
        for item in number:
            new_numbers.append(item)
    else:
        # 리스트가 아닌 일반 숫자면 그대로 new_numbers에 추가
        new_numbers.append(number)

# 결과 출력: 중첩 리스트가 풀려 하나의 평탄한 리스트가 됨
print(new_numbers)
