'''[HTML Parcing] 청와대 게시판 제목 뽑아오기
[국민청원 게시판 주요 10개 제목 뽑아오기]
 
파싱은 파서를 통해서 처리를 합니다.
 
따라서 API는 파서의 함수를 사용하게 되고 파이썬에서 주로 사용하는
파서는 BeautifulSoup 파서를 사용합니다.
 
Beautiful 파서를 사용하지만 당연히 파이썬에서 제공하는 기초 문자열 처리
함수들은 숙지하고 있어야 합니다.
 
파이썬의 문자열 처리 문법자료는 https://wikidocs.net/13#_9
를 참고하세요.
공식문서는 다음과 같습니다.
https://docs.python.org/2/library/string.html
 
다른 언어를 사용하거나 더 좋은 파서가 나오면 새로운 파서로 변경하여
사용하시면 됩니다.
 
자바스크립트를 파싱하기 위해서는 Seleninum 파서를 사용합니다.
 
'''
#bs4는 뷰티플파서를 뜻하고
#urllib는 HTML 소스를 가져오기 위한 모듈입니다.
 
import bs4
from urllib.request import urlopen
 
#urllib의 urlopen함수를 사용하여 HTML소스를 가져옵니다.
#이를 뷰티플파서의 lxml로 파싱합니다.
src = urlopen('https://www1.president.go.kr/petitions?order=best').read()
src = bs4.BeautifulSoup(src, 'lxml')
 
'''
파이썬 언어를 다룰 때 주의점은 타입을 주의하셔야 합니다.
여러분은 타입 비 지향적인 언어를 사용하였기에 자료의 타입에 취약합니다.
파이썬에서 문자열은 주로 리스트로 처리됩니다. 따라서 리스트를 다루는
문자열 연습을 꼭 하셔야 합니다.
'''
#문자열 변수 생성 - 파이썬은 변수겸 객체가 됩니다.
#대입연산을 위해서 변수를 만드세요.
str = ''
#청와대 HTML코드 중 'cd reply_w'에 제목이 있습니다.
#뷰티플파서의 fild_all함수의 특징은 받아온 자료를 리스트로 만들어 버립니다.
 
for i in range(10):
    str += src.find_all('a', class_='cb relpy_w')[i].text + '|'
 
#소스코드를 str문자열에 담았습니다.
 
#'제목'이라는 글자를 다 제거 하였습니다.
str = str.replace('제목 ','')
#한줄 띄어 쓴 문자를 제거 하였습니다.
str = str.replace('\n','')
#여기서 중요합니다 split로 자르고 나면 문자열이 리스트로
#변환됩니다.
str = str.split('|')
print(len(str))
 
#그냥 찍어 봅니다. 제목만 뽑혀 나옵니다.
for i in range(10):
    print(str[i])
 
#순서를 만들어 주고 싶으면 다음과 같이 가공하거나 .format을 사용하세요.
for i in range(10):
    print( '%d.' % (i+1) +  str[i])
