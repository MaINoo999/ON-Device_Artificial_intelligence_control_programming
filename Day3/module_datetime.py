import datetime  # datetime 모듈을 가져옵니다. 날짜와 시간 관련 기능 제공

# 현재 시각 구하기
print("# 현재 시각 출력하기")
now = datetime.datetime.now()  # 현재 날짜와 시간 정보를 가지는 datetime 객체 생성
print(now.year, "년")    # 연도 출력
print(now.month, "월")   # 월 출력
print(now.day, "일")     # 일 출력
print(now.hour, "시")    # 시 출력
print(now.minute, "분")  # 분 출력
print(now.second, "초")  # 초 출력
print()  # 줄 바꿈

# 시간을 다양한 포맷으로 출력
print("# 시간을 포맷에 맞춰 출력하기")

# strftime()을 사용해서 원하는 형식의 문자열로 변환
output_a = now.strftime("%Y/%m/%d %H:%M:%S")
# format()을 사용해서 직접 포맷 구성
output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
)

# strftime()과 format()을 조합해서 한글로 출력
# %Y, %m 등으로 날짜 정보를 가져오고, 그 뒤에 {}에 "년월일시분초" 각각을 삽입
output_c = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초")

# 결과 출력
print(output_a)
print(output_b)
print(output_c)
print()
