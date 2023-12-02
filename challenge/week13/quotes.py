import os, re
import requests 
import urllib.request as ur #URL 열기
from bs4 import BeautifulSoup as bs #웹페이지 파싱
import operator

url = 'https://quotes.toscrape.com/tag/life/'

html = ur.urlopen(url) #URL 열어서 HTML 가져오기
soup = bs(html.read(), 'html.parser') #HTML 파싱

quotes = soup.find_all('div', {"class":"quote"}) #div태그&&class==quote 찾기

quote_terms = set() #웹페이지에 등장하는 단어들 저장할 집합 생성
term_frequency_dict = {} #단어 빈도 수 저장할 딕셔너리

for quote in quotes:
    quote = quote.find_all('span', {"class":"text"}) #quotes에서 span&&class==text 찾기
    for i in quote: #text인 경우에만 출력
        #print(i.text)
        preprocessed_quote = i.text.lower().split(" ") #소문자화하고 공백 기준으로 쪼개어 preprocessed_quote에 저장
        for j in preprocessed_quote: #소문자화하고 공백 기준으로 쪼개어진 단어 내에서 반복
            quote_terms.add(j) #quote_terms 집합에 소문자화,공백기준으로 쪼개어진 단어들 추가

            if j in term_frequency_dict : #j가 딕셔너리에 존재한다면
                term_frequency_dict[j] += 1 #빈도 수 1 증가
            else : #딕셔너리에 존재하지 않는다면
                term_frequency_dict[j] = 1 #새로운 토큰으로 추가하고 빈도 수 1로 설정

#print(quote_terms)

#print(term_frequency_dict) #단어들의 빈도 수 출력

#단어의 빈도 수를 기준으로 내림차순 정렬
sorted_word_list = sorted(term_frequency_dict.items(), key=operator.itemgetter(1), reverse=True)

for i in range(5) : #빈도 수 상위 5개 단어 출력
    word, count = sorted_word_list[i]
    print(i+1, word, count)