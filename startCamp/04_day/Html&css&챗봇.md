[TOC]

# Html과 css 

### Flask, html, css 연동하여 웹페이지 생성

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




Flask 생성방법

1. 사용자가 들어올 수 있는 경로를 첫째로 정의

   1-1. 

   ```python
   if __name__ == '__main__': # 중심 모듈 생성
       app.run(debug=True) # 동적 디버그
   ```

2. 두번째 이후부터 경로

   2-1. 탬플릿 사용

   ​	2-1-1. render_template 생성한다.

3. 

#### Django



<tesschung>.github.io

bootstrap theme

theme 다운 압축풀기

gitbashhere



#### API : 

(응용 프로그램 프로그래밍 인터페이스)는 응용 프로그램에서 사용할 수 있도록, 

운영 체제나 프로그래밍 언어가 제공하는 기능을 제어할 수 있게 만든 인터페이스를 뜻한다.

font api site:

http://artii.herokuapp.com/



http://artii.herokuapp.com/make 요청 보내는 주소

?**text**=ASCII+art 



http://artii.herokuapp.com/make?text=Helloworld



http://artii.herokuapp.com/make

?**text**=helloworld

&**font**=trek -> http://artii.herokuapp.com/fonts_list



요청한 텍스트가 아닌 정보를 받아서 

보여주기 위한 것

딕셔너리에 담아서 보여주기







##### #### ** 반드시 외워야 하는 개념(사용자 input을 받아서 처리하는 기능)

##### survey

- 설문지폼을 작성했다고 하는 경우, 

- html 필요

- 질문 필요 form

- 작성하기를 요구하는 값이 있을것  name email github.com

- 적을 수 있는 공간이 필요 input

- 다시 작성자에게 해당 값을 돌려줄 것을 명시

  flask에서 제공되는 함수로 사용자가 입력한 값을 꺼낸다 (request 함수)

- 그 후 받은 설문지에 대한 정보를 저장

  이러한 과정을 웹으로 옮기는 작업



##### login

1. 기본 페이지:

2. 로그인 페이지: 

   2-1. render_template하여 로그인 페이지를 준다.  

   2-2. 매개변수(아이디, 비밀번호) 로 사용자가 로그인 요청을 서버에 보낸다.

   2-2-1. 우리의 회원이 맞으면 로그인을 시켜주고, 회원이 맞지 않으면 로그인을 시키지 않는다.

3. 로그인 후 들어가는 페이지:

#### 



##### search





##### font

사용자-아스키아트-text-서버-아스키아트-조합->make->서버-사용자

1. 사용자에게 text 입력받음
2. text를 api에 요청을 보냄
3. 요청 받은 것을 text화 하여 사용자에게 전달하기 위해 생성한 다른 페이지에 해당 text를 출력



1. 랜덤 font로 뽑은 font로 조합해서 
2. 사용자에게 보여주기



##### lotto

1. input 페이지

1-1. 회차 

1-2. 사용자가 선택할 번호

2. 실제 당첨 번호와 비교하여 실제 사용자에게 전달 페이지

865

3 15 22 32 33 45





https://dhlottery.co.kr/common.do?method=main

network -> all

1. https://dhlottery.co.kr/common.do?method=getLottoNumber

![1562833282924](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562833282924.png)

2. https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=865

   Chrome Json Viewer로 확인!

![1562833355795](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562833355795.png)

json



