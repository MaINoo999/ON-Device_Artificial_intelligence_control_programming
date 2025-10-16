# 'result.txt' 파일을 쓰기 모드('w')로 열고, 변수 file에 파일 객체를 할당
# with 구문을 사용하면 파일을 자동으로 닫아줌 → file.close() 불필요
with open('result.txt', 'w', encoding='utf-8') as file:
    # 첫 줄에 "안녕 세상아!"를 작성 (줄바꿈 없음)
    file.write("안녕 세상아!")

    # 줄바꿈 추가
    file.write("\n")

    # 두 번째 줄에 "안드로이드" 작성 후 줄바꿈
    file.write("안드로이드\n")

    # 세 번째 줄에 "OS" 작성 (줄바꿈 없음)
    file.write("OS")
