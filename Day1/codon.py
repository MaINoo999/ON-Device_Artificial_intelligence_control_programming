# 사용자로부터 DNA 염기서열을 입력받음
dna = input("염기 서열을 입력해주세요: ")

# 코돈(3개씩 자른 염기)들을 저장할 리스트
codon_list = []

# 코돈별 등장 횟수를 저장할 딕셔너리
codon_dict = {}

# dna 문자열을 3개씩 잘라서 codon_list에 추가
for i in range(0, len(dna), 3):
    codon_list.append(dna[i:i + 3])

# 코돈 리스트 출력 (디버깅용)
print(codon_list)

# 코돈 리스트를 순회하며, 각 코돈의 길이가 3인지 확인한 후 등장 횟수를 세어 딕셔너리에 저장
for codon in codon_list:
    if len(codon) != 3:
        continue  # 코돈 길이가 3이 아니면 (불완전한 코돈) 건너뜀
    codon_dict[codon] = codon_dict.get(codon, 0) + 1  # 등장 횟수를 누적

# 코돈별 등장 횟수 출력
print(codon_dict)
