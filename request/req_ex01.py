# https://foss4g.tistory.com/1617

import requests
from bs4 import BeautifulSoup

# 지정한 url에 따른 html_doc을 통해 해당 페이지의 html 확인
r = requests.get('https://search.naver.com/search.naver?query=%EA%B5%AD%EB%A6%BD%EA%B3%B5%EC%9B%90&where=news&ie=utf8&sm=nws_hty')
html_doc = r.text
# print(html_doc)

# html_doc을 Beautiful Soup을 통해 열기
soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())

# for link in soup.find_all('a'):
#     print(link.get('href'))

news_tit = soup.findAll("a", {"class":"news_tit"})
# print(news_tit)

# 네이버 뉴스 제목 파싱
for i in range(len(news_tit)):
    print(news_tit[i].get('title'))