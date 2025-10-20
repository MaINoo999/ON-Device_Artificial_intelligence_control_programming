import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import os

# =======================
# 1. 폴더 생성
# =======================
os.makedirs("data", exist_ok=True)

# =======================
# 2. RSS URL 정의
# =======================
rss_urls = {
    "경제": "https://www.yna.co.kr/rss/economy.xml",
    "증권": "https://www.yna.co.kr/rss/market.xml",
}

# =======================
# 3. 오늘부터 7일치 날짜 리스트
# =======================
today = datetime.today()
date_list = [(today - timedelta(days=i)).date() for i in range(7)]

# =======================
# 4. 기존 누적 데이터 불러오기
# =======================
csv_path = "data/rss_news_all.csv"
if os.path.exists(csv_path):
    df_all = pd.read_csv(csv_path, parse_dates=['날짜'])
else:
    df_all = pd.DataFrame(columns=["카테고리", "제목", "날짜"])

# =======================
# 5. 뉴스 수집
# =======================
news_data = []

for category, url in rss_urls.items():
    try:
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.content, "xml")
        items = soup.find_all("item")
        for item in items:
            title = item.title.text
            pubDate = item.pubDate.text
            try:
                date_obj = datetime.strptime(pubDate, "%a, %d %b %Y %H:%M:%S %z").date()
            except:
                continue
            if date_obj in date_list:
                news_data.append({
                    "카테고리": category,
                    "제목": title,
                    "날짜": date_obj
                })
    except requests.exceptions.HTTPError as e:
        print(f"{category} RSS 요청 실패: {e}")

# =======================
# 6. 새 데이터 DataFrame
# =======================
df_new = pd.DataFrame(news_data)

# =======================
# 7. 누적 데이터 업데이트 (중복 제거)
# =======================
df_all = pd.concat([df_all, df_new], ignore_index=True)
df_all.drop_duplicates(subset=['카테고리', '제목', '날짜'], inplace=True)

# =======================
# 8. 최근 7일치 데이터 필터링
# =======================
df_recent = df_all[df_all['날짜'].isin(date_list)]
df_recent.sort_values('날짜', inplace=True)

# =======================
# 9. 날짜별 카테고리 건수 집계
# =======================
df_count = df_recent.groupby(['날짜', '카테고리']).size().unstack(fill_value=0).reset_index()

# =======================
# 10. Excel 저장 + 차트
# =======================
excel_path = "data/rss_news_7days_with_chart.xlsx"
with pd.ExcelWriter(excel_path, engine='xlsxwriter') as writer:
    # 뉴스 제목 시트
    df_recent.to_excel(writer, sheet_name="뉴스_제목", index=False)
    # 뉴스 건수 시트
    df_count.to_excel(writer, sheet_name="뉴스_건수", index=False)

    # 차트 생성
    workbook  = writer.book
    worksheet = writer.sheets["뉴스_건수"]

    chart = workbook.add_chart({'type': 'column'})
    for i, category in enumerate(df_count.columns[1:]):  # 첫 열은 날짜
        chart.add_series({
            'name':       category,
            'categories': ['뉴스_건수', 1, 0, len(df_count), 0],  # 날짜
            'values':     ['뉴스_건수', 1, i+1, len(df_count), i+1],  # 건수
        })

    chart.set_title({'name': '뉴스 카테고리별 일일 건수 (최근 7일)'})
    chart.set_x_axis({'name': '날짜'})
    chart.set_y_axis({'name': '건수'})
    chart.set_style(11)
    worksheet.insert_chart('E2', chart)

# =======================
# 11. 누적 CSV 저장
# =======================
df_all.to_csv(csv_path, index=False, encoding="utf-8-sig")

print(f"✅ Excel 저장 완료: {excel_path} (뉴스 제목, 건수, 차트 포함)")
print(f"✅ 누적 CSV 저장 완료: {csv_path}")
