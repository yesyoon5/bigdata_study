#[Tweepy] 를 활용한 트위터 내용 긁어오기

import tweepy
import os
import sys
 
 
#API 인증요청
consumer_key = 'dUTrMiP1b6nRJklLDUmvc6S39'
consumer_secret = 'qOZV7Q0cK11m2MdikqVBIeMsrJjy4dwGEgcyexI83FxkBO5GCl'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 
#access 토큰 요청
access_token = '1064355030642262016-ryTrSIuZ1mthf09KiuhpdHP3Uvq0x1'
access_token_secret = 'f0KVeYzC5STSNFysqrE4C2Dz8n2oYeuMor2WY4KTigGuX'
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
