#[Tweepy] 를 활용한 트위터 내용 긁어오기

import tweepy
import os
import sys
 
 
#API 인증요청
consumer_key = 'bPjzpUBfpk_____________'
consumer_secret = '3VzEZVWo8Hgt________________'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 
#access 토큰 요청
access_token = '118977113-sKFTAs3pzr0dzklKf______________'
access_token_secret = 'g8jcpR8NMQBfgaBraiX___________________'
auth.set_access_token(access_token, access_token_secret)
 
api = tweepy.API(auth)
 
#############################################################
 
location = '%s,%s,%s' % ('35.95', '128.25', '1000km') #검색기준(대한민국)좌표, 반지름
 
keyword = '트럼프 OR 경제' # OR로 검색어 묶어줌 검색어 5개, OR 대문자로
 
#wfile = open(os.getcwd() + '/twitter.txt', mode='w') #쓰기모드
wfile = open('twitter.txt', mode='w') #쓰기모드
 
#twitter 검색 cusor 선언
cursor = tweepy.Cursor(api.search,
            q=keyword,
            since = '2018-11-19',
            count = 100,
            geocode = location,
            include_entities = True)
 
for i, tweet in enumerate(cursor.items()):
    print('{}:{}'.format(i, tweet.text))
    wfile.write('{}:{}'.format(i, tweet.text))
 
wfile.close()
