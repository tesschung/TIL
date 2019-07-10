import requests
from bs4 import BeautifulSoup
import csv

# 1. bithumb 페이지를 가지고 온다.
response = requests.get('https://www.bithumb.com/') # 요청을 보내 응답을 받는다.
# print(response)
html = response.text # 응답받은 객체에서 html 문서를 string으로 가지고 옴
# print(html)

# 2. BeautifulSoup module을 이용하여 string type의 html parsing한다.
soup = BeautifulSoup(html, 'html.parser')


# 3. 각 코인의 정보가 담겨있는 table row 데이터를 list의 형태로 가져온다.
coins = soup.select('.coin_list tr') 
#' tr' 처럼 tr을 띄어쓰기로 접근시 모두 가져옴
#'> tr' 처럼 접근시 바로 다음 것 가져옴
# print(coins)


# 5. csv writer를 이용해서 정보를 저장한다.
with open('coin_info.csv', 'w', encoding='utf-8', newline='') as f:
    csv_writer = csv.writer(f)

    # 4. 각 코인을 순회하며 필요한 정보만 추출한다.
    for coin in coins: #coin == tr
        coinName = coin.select_one('td:nth-child(1) > p > a > strong').text.replace('NEW', '').strip()
        #print(coinname)
        #td:nth-child(1) -> td:nth-child(2) 두번째로 가져옴
        coinPrice = coin.select_one('td:nth-child(2) > strong').text.replace(',','').replace('원','')
        #print(coinPrice)
        data = (coinName, coinPrice) # tuple형식으로 생성
        csv_writer.writerow(data)
        print(data)
