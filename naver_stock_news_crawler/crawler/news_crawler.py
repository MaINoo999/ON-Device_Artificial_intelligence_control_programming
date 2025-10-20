# crawler/news_crawler.py
import requests
from bs4 import BeautifulSoup
import time
from textblob import TextBlob

def crawl_rss_news(keywords=None):
    RSS_CHANNELS = {
        "연합뉴스_경제": "https://www.yna.co.kr/rss/economy.xml",
        "연합뉴스_증권": "https://www.yna.co.kr/rss/stock.xml"  # 현재 404 발생 가능
    }

    all_news = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    for name, rss_url in RSS_CHANNELS.items():
        print(f"=== {name} 크롤링 ===")
        try:
            res = requests.get(rss_url, headers=headers)
            res.raise_for_status()
        except Exception as e:
            print(f"{name} RSS 요청 실패: {e}")
            continue

        soup = BeautifulSoup(res.text, "xml")
        items = soup.find_all("item")
        if not items:
            print(f"{name} 뉴스 없음")
            continue

        for item in items:
            try:
                title = item.title.text.strip()
                link = item.link.text.strip()
                date = item.pubDate.text.strip()
                summary = item.description.text.strip()
                content = summary

                # 키워드 필터링
                keyword_matched = False
                if keywords:
                    if any(k in title or k in content for k in keywords):
                        keyword_matched = True
                    else:
                        continue
                else:
                    keyword_matched = True

                word_count = len(content.split())
                sentiment = TextBlob(content).sentiment.polarity

                all_news.append({
                    "channel": name,
                    "title": title,
                    "link": link,
                    "date": date,
                    "summary": summary,
                    "content": content,
                    "keyword_matched": keyword_matched,
                    "word_count": word_count,
                    "sentiment": sentiment
                })

            except Exception as e:
                print(f"뉴스 아이템 처리 중 오류: {e}")
                continue

        time.sleep(0.5)

    return all_news
