from flask import Flask, render_template # module 호출
import datetime
import random
app = Flask(__name__)

# render_template(작성할 탬플릿 이름)

@app.route('/') # @ == decorator, / == endpoint
def hello(): # def 함수 만들기
    # return 'Hello SSAFY!!'
    return render_template('index.html')  
    # templates(반드시! templates)인 이름을 가진 폴더 안에서 index라는 html파일을 찾아 반환해준다


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
    return render_template('greeting.html', html_name=name) # name을 html_name으로 넘겨준다.
    # 변수에 맞게 변환을 시켜주는 함수 -> jinja2


@app.route('/cube/<int:number>')
def cube(number):
    result = number ** 3 # ** 앞뒤 공백 convention
    return render_template('cube.html', html_result=result, html_number=number) # convention


# 실습
@app.route('/lunch/<int:people>')
def lunch(people):
    # 사람수 만큼 메뉴 return
    menu = ['김밥', '짬뽕', '스시', '볶음밥']
    order = random.sample(menu,people)
    return str(order) 


@app.route('/movie')
def movie():
    movies = ['스파이더맨', '앤드게임', '기생충', '알라딘']
    movie = random.choice(movies)
    return render_template('movie.html', html_movie=movie, html_movies=movies)


# FLASK_APP=hello.py flask run
# if __name__ == "__main__": import해서 사용하는 경우 or 직접 실행 경우 구분
if __name__ == '__main__': 
    app.run(debug=True) # debug=True 설정을 하여 정적이였던 것을 동적으로 변경
