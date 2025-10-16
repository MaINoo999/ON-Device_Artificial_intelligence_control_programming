# 'result.txt' 파일을 읽기 모드("r")로 열고, 변수 file에 파일 객체를 할당
# with 구문을 사용하면 블록을 빠져나갈 때 자동으로 파일이 닫힘
with open("result.txt", "r", encoding="utf-8") as file:
    # 파일 전체 내용을 한 번에 읽어서 변수 read_data에 저장
    read_data = file.read()

    # 읽어온 파일 내용을 출력
    print(read_data)
