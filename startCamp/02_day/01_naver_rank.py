import requests
from bs4 import BeautifulSoup


url = 'http://www.naver.com'



response = requests.get(url).text
#print(response)

soup = BeautifulSoup(response, 'html.parser')

"""
classs는 '.'으로 접근
ul -> li -> ah_1
'띄어쓰기' 하여 그 다음으로 접근함

'.ah_item .ah_a .ah_k'
ul.li

3) firefox: 오른쪽 클릭 복사 -> CSS선택자
selector ='ul.ah_l:nth-child(5) > li:nth-child(1) > a:nth-child(1) > span:nth-child(2)'
rankings = soup.select(selector)
"""
rankings = soup.select('.ah_item .ah_a .ah_k')
#print(rankings)
#원소만 text화 가능, 때문에 for문으로 정리

for ranking in rankings:
    print(ranking.text) #ranking.get_text()    

"""
<body>
<div class="wrap" id="PM_ID_ct">
<div class="header" role="banner">
<div class="section_navbar">
<div class="area_hotkeyword PM_CL_realtimeKeyword_base" queryid="C1562632612991825765">
<div class="ah_list PM_CL_realtimeKeyword_list_base" aria-hidden="true" queryid="C1562633255956901212"><ul class="ah_l" style="display: block;" data-list="1to10" queryid="C1562632631444788967"><li class="ah_item" data-order="1" queryid="C1562633255869662100"><a class="ah_a" href="https://search.naver.com/search.naver?where=nexearch&amp;query=%EA%B0%80%EC%88%98+%EC%9E%A5%EC%9D%80%EC%88%99%EB%82%98%EC%9D%B4&amp;sm=top_lve&amp;ie=utf8" data-clk="lve.keyword">
<span class="ah_k" queryid="C1562633254263499434">가수 장은숙나이
</span>
</a></li></ul></div></div></div></div>
</div>
</body>
</html>
"""