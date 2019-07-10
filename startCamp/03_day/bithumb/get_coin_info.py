"""
#tableAsset > tbody class="coin_list"
=> tr 리스트 [<tr:btc>...]

with open('coin.csv') as f:
    for coin in coins:
        coinname = coin(tr).select_one('strong')
        f.write(coinname)

1. 시세
2. 이름
"""
import os
import csv
import requests
from bs4 import BeautifulSoup

url = "https://www.bithumb.com/"

response = requests.get(url).text
#print(response)

soup = BeautifulSoup(response, "html.parser")

tbody_list = soup.select_one('tbody')
tr_tags = tbody_list.select('tr')

# tableAsset > tbody
# tr_list = soup.select('.coin_list')
print(tr_tags)

with open("bithum.csv", 'w', encoding='utf-8', newline='') as f:

    for tr_tag in tr_tags:
        coinname = tr_tag.select_one('td p a strong')
        coinname = coinname.text

        coinprice = tr_tag.select_one('.sort_real')
        coinprice = coinprice.text

        f.write(f'{coinname}, {coinprice} \n')

    print(coinname, coinprice)