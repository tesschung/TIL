from flask import Flask, render_template, request # 사용자의 요청 확인 가능
import requests
from bs4 import BeautifulSoup
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


@app.route('/font_list')
def font_list():
    response = requests.get('http://artii.herokuapp.com/fonts_list')
    pre_tag = soup.select('pre').text.split()
    for font in pre_tag:
        pass

if __name__ == '__main__': 
    app.run(debug=True)
