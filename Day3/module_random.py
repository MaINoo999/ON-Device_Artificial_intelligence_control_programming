import random  # random 모듈을 불러옵니다
print("# random 모듈")

# 0.0 이상 1.0 미만의 임의의 float(실수) 숫자를 반환
print("- random():", random.random())

# 10 이상 20 이하의 임의의 float 숫자를 반환
print("- uniform(10,20):", random.uniform(10, 20))

# 0 이상 10 미만의 정수 중에서 임의의 값을 반환
print("- randrange(10):", random.randrange(10))

# 리스트에서 임의의 요소 하나를 선택
print("- choice([1,2,3,4,5]):", random.choice([1,2,3,4,5]))

# 리스트의 요소들을 섞음 (원본 리스트를 직접 변경하고 반환값은 None)
# 주의: shuffle은 리스트 자체를 변경하므로 출력 시 주의가 필요
sample_list = [1, 2, 3, 4, 5]
random.shuffle(sample_list)
print("- shuffle([1,2,3,4,5]):", sample_list)

# 리스트에서 중복되지 않게 k개의 요소를 랜덤하게 뽑아 리스트로 반환
print("- sample([1,2,3,4,5], k=2):", random.sample([1,2,3,4,5], k=2))
