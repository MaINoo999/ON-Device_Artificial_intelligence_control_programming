# "basic.txt"라는 이름의 파일을 '쓰기 모드(w)'로 열기
# 파일이 존재하지 않으면 새로 생성되고, 존재하면 기존 내용을 덮어씀
# 인코딩은 한글을 위해 'utf-8' 지정
file = open("basic.txt", "w", encoding='utf-8')

# 문자열을 파일에 작성 (줄바꿈 없이 이어서 작성됨)
file.write("hello Python Programing")
file.write("안녕 파이선...")

# 줄바꿈 문자 추가 (다음 출력은 새 줄에 작성됨)
file.write("\n")

# 새 줄에 문자열 작성
file.write("Hello Python Programing...")

# 줄바꿈 문자 추가
file.write("\n")

# 파일을 닫아서 저장 내용 반영 및 리소스 정리
file.close()
