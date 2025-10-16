import requests
import os

def download_via_short_url(short_url, save_path):
    response = requests.get(short_url, allow_redirects=True, stream=True)
    final_url = response.url
    print("최종 URL:", final_url)

    if response.status_code != 200:
        print("요청 실패:", response.status_code)
        return

    content_type = response.headers.get('Content-Type', '')
    print("Content-Type:", content_type)

    # 다운로드 파일 저장
    with open(save_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    if os.path.exists(save_path):
        print(f"파일이 저장되었습니다: {save_path}")
    else:
        print(f"저장 실패: {save_path}")

if __name__ == "__main__":
    # 다운로드할 단축 URL 목록
    short_urls = [
        "https://naver.me/GUmnELEe",
        "https://naver.me/xfYD0pTD",
        "https://naver.me/x2cq4ESS"
    ]

    # 원하는 다운로드 경로
    download_folder = r"D:\Code\Python\혼자공부하는_파이썬\web\download"

    # 폴더 없으면 생성
    os.makedirs(download_folder, exist_ok=True)

    saved_files = []

    for i, url in enumerate(short_urls):
        ext = ".ipynb" if i == 2 else ""
        filename = f"downloaded_{i}{ext}"
        save_path = os.path.join(download_folder, filename)
        download_via_short_url(url, save_path)
        saved_files.append(save_path)

    # 다운로드 폴더 열기
    print(f"\n저장된 폴더를 엽니다: {download_folder}")
    os.startfile(download_folder)
