import random  # 랜덤 값 생성을 위한 모듈 불러오기

# 사용할 한글 문자 리스트 생성
hanguls = list("가나다라마바사아자차카타파하")

# info.csv 파일을 쓰기 모드(w)로 열고, 한글 깨짐 방지를 위해 UTF-8 인코딩 지정
with open("info.csv", "w", encoding="utf-8") as file:
    # 1000명의 데이터를 생성
    for i in range(1000):
        # 한글 리스트에서 랜덤으로 두 글자를 선택하여 이름 생성
        name = random.choice(hanguls) + random.choice(hanguls)

        # 40~99kg 사이의 몸무게를 랜덤으로 생성
        weight = random.randrange(40, 100)

        # 140~199cm 사이의 키를 랜덤으로 생성
        height = random.randrange(140, 200)

        # 생성한 데이터를 CSV 형식으로 파일에 저장
        file.write("{}, {}, {}\n".format(name, weight, height))
