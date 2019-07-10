from flask import Flask # module 호출
import datetime
import random
app = Flask(__name__)

@app.route('/') # @ == decorator, / == endpoint
def hello(): # def 함수 만들기
    return 'Hello SSAFY!!'

@app.route('/ssafy')
def ssafy():
    return 'Hello SSAFY!!!'

@app.route('/dday')
def day():
    today = datetime.datetime.now()
    b_day = datetime.datetime(2019, 1, 15)
    td = b_day - today
    return f'{td.days}일 남았습니다.'

@app.route('/html')
def html():
    return '<h1> This is HTML h1 tag!</h1>'

@app.route('/html_lines')
def html_lines():
    return '''
    <h1>여러줄을 보내봅시다.</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>
    '''

"""
@app.route('/greeting/IU')
def greeting_IU():
    return '반갑습니다. IU 님!'

@app.route('/greeting/ziont')
def greeting_Ziont():
    return '반갑습니다. ZionT 님!'
"""
#<type:input> 원하는 입력값

@app.route('/greeting/<name>') # http://127.0.0.1:5000/greeting/bts
def greeting(name): # name == IU
    return f'반갑습니다! {name} 님!'

@app.route('/cube/<int:number>')
def cube(number):
    return f'{number}의 3 제곱은 {number ** 3} 입니다.' #3제곱

# 실습
@app.route('/lunch/<int:people>')

def lunch(people):
    # 사람수 만큼 메뉴 return
    menu = ['김밥', '짬뽕', '스시', '볶음밥']
    order = random.sample(menu,people)
    return str(order) 

""" 실수:
    new_choice = []
    for a in range(people+1):    
        new_choice.append(random.choice(menu))
    return new_choice
"""

# FLASK_APP=hello.py flask run
# if __name__ == "__main__": import해서 사용하는 경우 or 직접 실행 경우 구분
if __name__ == '__main__': # 접근용 모듈 생성
    app.run(debug=True) # debug=True 설정을 하여 정적이였던 것을 동적으로 변경



