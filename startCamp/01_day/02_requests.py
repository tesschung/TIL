#web crawling
import webbrowser
import requests # 서버에서 요청을 받는 모듈
from bs4 import BeautifulSoup # 응답을 분석할 수 있도록 바꿔주는 모듈

"""
1: 원하는 url
"""
query = '/sise/'
search_url = 'https://finance.naver.com'+query
# webbrowser.open(search_url)

"""
2: 서버에서 요청하여 응답(200)받기

response = requests.get(search_url).status_code
- 요청보낸 응답에 대한 상태 확인용 
                                200: 요청성공 400: 에러

response = requests.get(search_url).text
- 200으로 응답 받은 경우 text화
"""
response = requests.get(search_url).text
# print(response) # 200 응답 확인
# print(response.text) # html로 받아오기

# text=str으로 변환시켜 -> html 변수에 저장
# html = response.text

"""
3: 분석가능하도록 저장
"""
# 접근 가능한 것으로 변환 = parser
soup = BeautifulSoup(response, 'html.parser')

"""
4: 원하는 정보 지정
1) window: 12F에서 스타일이 적용된 요소 복사 
 <body><div id="wrap"><div id="newarea"><div id="contentarea"><div class="box_top_submain2"><div class="lft"><ul class="tab_sel1 tab"><li onmouseover="moveIndex('tab_sel1')"><a class="mnu" onclick="clickcr(this,'mqu*k.title','','',event)" href="/sise/sise_index.nhn?code=KOSPI "><span class="num" id="KOSPI_now">2,072.18</span></a></li></ul></div></div></div></div></div></body>

2) crome: 12F에서 copy -> copy selector
 #KOSPI_now

모든 정보 -> list 형태로 반환
want_info = soup.select('selector') 

하나의 정보
want_info = soup.select_one('selector') 
"""
# 코스피에 해당하는 tag 찾아서 가져오기
# id란 유일한 값, 바로 가져올 수 있음
# id로 접근시 #id명
kospi = soup.select_one('#KOSPI_now').text
print(kospi) # 정상출력