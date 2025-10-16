from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def main():
    # Chrome 옵션 설정
    options = Options()
    # options.add_argument("--headless")  # 브라우저 숨김 (테스트 완료 후 활성화 가능)
    options.add_argument("--window-size=1920,1080")

    # Chrome 드라이버 실행
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # 1. 커피빈 매장 목록 페이지 접속
        driver.get("https://www.coffeebeankorea.com/store/store.asp")
        time.sleep(1)

        # 2. JavaScript 함수로 매장 상세 팝업 열기
        driver.execute_script("storePop2(363)")
        time.sleep(1.5)

        # 3. 새 창(팝업)으로 전환
        main_window = driver.current_window_handle
        all_windows = driver.window_handles

        for handle in all_windows:
            if handle != main_window:
                driver.switch_to.window(handle)
                break

        # 4. 팝업 내용 파싱
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        # 5. 매장명 추출
        store_name_h2 = soup.select_one('div.store_txt > h2')
        if store_name_h2:
            print("[매장 이름]", store_name_h2.text.strip())
        else:
            print("매장 이름을 찾을 수 없습니다.")

        # 6. 주소, 전화번호 등 추가 정보도 추출 가능
        # 예시: soup.select_one('div.store_txt > table td')

    finally:
        # 모든 창 닫기
        driver.quit()

if __name__ == "__main__":
    main()
