from flask import Flask, render_template, request # 사용자의 요청 확인 가능
import requests
# from bs4 import BeautifulSoup
app = Flask(__name__)


# www.google.com/ search
@app.route('/') # / => root  endpoint
def index():
    return f'''
    안녕하세요? \n
    다음과 같은 경로들이 있습니다. \n
        기본 경로
        1. /greeting/이름
        설문지 경로
        1. /ping
            1-1. /pong
        검색사이트
        1. /google
        2. /naver
        폰트
        1. /ascii_input
        로또
        1. /lotto_input
        '''


@app.route('/greeting/<string:name>')
def greeting(name):
    return render_template('greeting.html', html_name=name)
# f'하이 {name}!'


# survey
@app.route('/ping')
def ping():
    return render_template('ping.html')


@app.route('/pong')
def pong():
    # 사용자가 입력한 값들을 get하여 age값을 age 매개변수에 지정
    age = request.args.get('age')
    return render_template('pong.html', age=age)
# f'Pong! age: {age}'


# google
@app.route('/google')
def google():
    return render_template('google.html')


# naver (https://search.naver.com/search.naver/query=%E3%85%87)
@app.route('/naver')
def naver():
    return render_template('naver.html')


# font
# 1. 사용자가 입력할 수 있는 페이지 생성
@app.route('/ascii_input')
def ascii_input():
    return render_template('ascii_input.html')


# 2. 사용자가 입력한 정보를 저장한다.
@app.route('/ascii_result')
def ascii_result():
    text = request.args.get('text') # Message
    # 3. Ascii Art API를 활용해서 사용자의 input 값을 변경한다.
    # url = 'http://artii.herokuapp.com/make?text='+text
    response = requests.get(f'http://artii.herokuapp.com/make?text={text}')
    # print(response.text) terminal에서 확인 가능
    result = response.text
    return render_template('ascii_result.html', result=result)


# lotto API
@app.route('/lotto_input')
def lotto_input():
    ## 사용자가 입력할 수 있는 페이지만 전달
    return render_template('lotto_input.html')


@app.route('/lotto_result')
def lotto_result():
    ## 사용자 입력값 받기
    lotto_round = request.args.get('round')
    lotto_numbers = request.args.get('numbers').split()
    
    ## 로또 실제 당첨번호 확인
    url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}'
    response = requests.get(url)
    #json 타입의 문서를 python dictionary로 parsing/ json()함수를 사용
    lotto_info = response.json()
    correct = 0
    winner = []
    #real_lotto_list = []
    for num in range(1,7):
        winner.append(str(lotto_info[f'drwtNo{num}']))
    
    ## 번호 교집합 개수 찾기
    if len(lotto_numbers) == 6:     # 사용자가 보낸 숫자가 6개가 맞는지 확인
        matched = 0                 # count용

        for number in lotto_numbers:# 사용자 숫자를 하나씩 확인하면서
            if number in winner:    # 당첨번호에 있는지 확인해서
                matched += 1        # 사용자의 번호가 있다면, 당첨시 matched를 1씩 증가시킨다 
        
        # print(matched)
        if matched == 6:
            result = '1등입니다.'
        elif matched == 5:
            if str(lotto_info['bnusNo']) in lotto_numbers:#bnusNo의 유무로 2등,3등 달라짐
                result = '2등입니다.'
            else:
                result = '3등입니다.'
        elif matched == 4:
            result = '4등입니다.'
        elif matched == 3:
            result = '5등입니다.'
        else:
            result = '꽝입니다...'
    
    else:    
        result = '입력하신 숫자가 6개가 아닙니다.'

    return render_template('lotto_result.html', result=result, lotto_round=lotto_round, lotto_numbers=lotto_numbers, matched=matched)
    #f'{lotto_round}, {lotto_numbers}, {correct} 맞았습니다.'
    
    #https://dhlottery.co.kr/common.do?method=main

"""  로또 코드2        
    # 규칙
    lotto_info['drwtNo5']
    lotto_info['drwtNo1']
    lotto_info['drwtNo2']
    lotto_info['drwtNo3']
    lotto_info['drwtNo4']
    lotto_info['drwtNo6']

'drwtNo6': 32,/
 'drwtNo4': 25,/
  'firstPrzwnerCo': 10, 
  'drwtNo5': 27,/
   'bnusNo': 42, /
   'firstAccumamnt': 18798998250, 
   'drwNo': 860, 
   'drwtNo2': 8, /
   'drwtNo3': 18, /
   'drwtNo1': 4 /

@app.route('/lotto_result')
def lotto_result():
    lotto_round = request.args.get('round')
    my_numbers = request.args.get('numbers').split()
    print(my_numbers)

    url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}'
    response = requests.get(url)
    lotto_info = response.json()    # json 타입의 파일을 python dictionary 로 parsing 해줘

    # print(lotto_info)

    correct = 0

    for i in range(1,7):
        lucky_num = lotto_info[f'drwtNo{i}']

        print(lucky_num)

        #print(str(lucky_num) in my_numbers)

        if str(lucky_num) in my_numbers:
            correct += 1
        

    print(f'{correct}개 맞았습니다')
          
    return f'{correct}개 맞았습니다'
"""

if __name__ == '__main__': 
    app.run(debug=True)
