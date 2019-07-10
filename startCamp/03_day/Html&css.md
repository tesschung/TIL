[TOC]

# Html과 css



#### html: 정보의 구조화

```html

```

#이란 css selector이다.

.으로 class 접근가능



클래스와 아이디의 차이점:

클래스는 여러개를 사용할 수 있지만 

아이디는 고유성을 가지므로 한 문서에 한번만 사용



![1562718645246](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562718645246.png)



#### css:cascading style sheets





#### 크롤링

select() list

select_one() 원소 

select('td') tag

select_one('**.**class') class

select_one('**#**아이디값') id



#### [FLASK](http://flask.pocoo.org/)

- 파이썬 웹 어플리케이션 생성 Framwork

- - Django보다 간단 생성
  - flask는 **정적**이다. -> **동적**으로 변경 가능(저장할때마다 서버 자동 재오픈 가능)

```
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
```

```
$ pip install Flask
$ FLASK_APP=hello.py flask run
 * Running on http://localhost:5000/
```





#### Django

