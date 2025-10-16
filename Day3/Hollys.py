import requests
from bs4 import BeautifulSoup
import pandas as pd

Hollys_stores = []

# 여러 페이지 크롤링
for page in range(1, 6):  # 예: 5페이지까지 크롤링
    url = 'https://www.hollys.co.kr/store/korea/korStore2.do'
    data = {
        'page': page
    }

    response = requests.post(url, data=data)
    soup = BeautifulSoup(response.text, 'html.parser')
    tag_tbody = soup.find('tbody')

    if tag_tbody:
        for store in tag_tbody.find_all('tr'):
            store_td = store.find_all('td')
            if len(store_td) >= 6:
                store_name = store_td[1].text.strip()
                store_sido = store_td[0].text.strip()
                store_address = store_td[3].text.strip()
                store_phone = store_td[5].text.strip()
                Hollys_stores.append([store_name, store_sido, store_address, store_phone])
    else:
        print(f"[!] 페이지 {page}에 데이터가 없습니다.")

# 데이터프레임 변환 및 저장
Hollys_TBL = pd.DataFrame(Hollys_stores, columns=('매장', '도시', '주소', '전화번호'))
Hollys_TBL.to_csv("Hollys_TBL_EXCEL.csv", encoding='utf-8-sig', index=True)
Hollys_TBL.to_csv("Hollys_TBL.csv", encoding='utf-8', index=True)

print(f"[✔] 크롤링 완료: 총 {len(Hollys_stores)}개 매장")
