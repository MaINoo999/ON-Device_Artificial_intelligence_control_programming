# 연합뉴스 RSS 뉴스 자동 수집 및 시각화

> Python을 활용해 연합뉴스 경제·증권 뉴스 RSS를 자동으로 수집하고,  
> 최근 7일치 데이터를 분석·시각화하여 Excel과 차트로 확인할 수 있는 프로젝트

---

## 프로젝트 개요

- 연합뉴스의 **경제·증권 뉴스 RSS**를 수집
- 최근 7일치 뉴스 데이터를 기준으로 **제목, 날짜, 카테고리** 저장
- 데이터 분석 및 **Excel 시트 + 차트 시각화**
- Python 기반 자동화 스크립트로 수집과 시각화 모두 가능

---

## 주요 기능

| 기능 | 설명 |
|------|------|
| RSS 뉴스 수집 | 경제/증권 뉴스 RSS를 요청하고 XML 파싱 |
| 데이터 정리 | 뉴스 제목, 날짜, 카테고리 기반 DataFrame 생성 |
| 최근 7일 뉴스 필터링 | 수집 데이터 중 최근 7일 뉴스만 추출 |
| Excel 저장 | 뉴스 제목 시트, 날짜별 카테고리 건수 시트, 차트 포함 |
| 시각화 | Excel 내 차트로 일별 뉴스 건수 확인 가능 |

---

## 기술 스택

- **Python 3.11 이상**
- 주요 라이브러리:
  - `requests` : RSS 요청
  - `BeautifulSoup` : XML 파싱
  - `pandas` : 데이터 처리 및 Excel 저장
  - `xlsxwriter` : Excel 차트 생성
  - `datetime` : 날짜 계산
- 한글 폰트 지원: `malgun.ttf` (Windows 기준)

---

## 실행 방법

1. 저장소 클론

git clone [https://github.com/MaINoo999/ON-Device_Artificial_intelligence_control_programming/tree/main/naver_stock_news_crawler]
