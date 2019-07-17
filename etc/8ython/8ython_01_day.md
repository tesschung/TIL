[TOC]

# 8ython

## Jupyter notebook 활용전 준비

```bash
설치
$ pip install jupyter

실행
$ jupyter notebook

종료
Ctrl+c

편집툴사용
$ v- ~/bashrc
$ i
$ alias jn="jupyter notebook"
-> jupyternotebook as jn으로 인식
esc
:wq

파일내용을 읽어서 commend 라인에 노출
$ cat .bashrc
$ touch .bash_profile
$ source .bashrc

jupyter notebook 확장프로그램
$ pip install jupyter_contrib_nbextensions
$ pip jupyter contrib nbextensions install --users
```

- Markdown 작성 가능
- 코드블럭 생성하여 코딩 가능
- 코드블럭별 실행 결과 확인 가능
- Jupyter notebook 계속 사용하고자 한다면, Bash를 계속 켜둘것

Nbextensions: tableofcontents

![1563155250202](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1563155250202.png)

## jn 활용법

|                 |             |                       |
| --------------- | ----------- | --------------------- |
| help            | h           | 모든 단축키 확인 가능 |
| run             | ctrl+enter  |                       |
| next code block | shift+enter |                       |























----------note------------

**lambda 인자리스트: 표현식**

```python
g = lambda x: x**2
print(g(8))64
f = lambda x, y: x + y
print(f(4, 4))8
```

람다 정의에는 **"return"**문이 포함되어 있지 않습니다. 

반환값을 만드는 표현식이 있습니다. 

함수가 사용될 수 있는 곳에는 어디라도 람다 정의를 넣을 수 있으며, 위의 예 처럼 변수에 할당하여 사용할 필요는 없습니다.



다음은 람다 함수의 사용법을 보여줍니다.

```python
>>> def inc(n):	return lambda x: x + n

>>> f = inc(2)
>>> g = inc(4)

>>> print(f(12))
14
>>> print(g(12))
16
>>> print(inc(2)(12))
14
```



위의 코드는

inc 함수로 lambda 함수를 즉석에서 생성하고 반환 하는 함수를 정의 

리턴 된 함수는 인수를 작성시 지정된 값만큼 증가



이제 여러 개의 서로 다른 증분 함수를 만들어 변수에 할당 한 다음 서로 독립적으로 사용할 수 있습니다. 

마지막 문장에서 알 수 있듯

lambda 함수를 어떤 변수에 할당할 필요조차 없다. 

즉각적으로 사용할 수 있고

더 이상 필요하지 않을 때 잊어 버릴 수 있습니다.



**1. map() 함수**

람다 함수의 장점은 

map() 함수와 함께 사용될 때 볼 수 있습니다. 

map() 은 두 개의 인수 arguments 를 가지는 함수입니다.

**r = map(function, iterable, ...)**

첫 번째 인자 function 는 함수의 이름 입니다. 

두 번째 인자 iterable은 한번에 하나의 멤버를 반환할 수 있는 객체 입니다.

(list, str, tuple) map() 함수는 function을 iterable의 모든 요소에 대해 적용합니다. 

그리고 function에 의해 변경된 iterator를 반환합니다.

```python
>>> a = [1,2,3,4]
>>> b = [17,12,11,10]
>>> list(map(lambda x, y:x+y, a,b))
[18, 14, 14, 14]
```



**2. filter() 함수**

filter() 함수도 두 개의 인자를 가집니다.

**r = filter(function, iterable)**

filter에 인자로 사용되는 

function은 처리되는 각각의 요소에 대해 Boolean 값을 반환

**True를 반환하면 그 요소는 남게 되고,** 

False 를 반환하면 그 요소는 제거 됩니다.

```python
>>> foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
>>> list(filter(lambda x: x % 3 == 0, foo))
[18, 9, 24, 12, 27]
```



**3. reduce() 함수**

reduce() 함수를 두 개의 필수 인자와 하나의 옵션 인자를 가지는데, function 을 사용해서 iterable을 하나의 값으로 줄입니다. 

initializer 는 주어지면 첫 번째 인자로 추가 된다고 생각하면 됩니다.

**functools.reduce(function, iterable[, initializer])**

예를 들어 **reuce(function, [1,2,3,4,5])** 에서 list 는 **[function(1,2),3,4,5]** 로 하나의 요소가 줄고,

요소가 하나가 남을 때까지 **reduce(function, [function(1,2),3,4,5])** 를 반복합니다.

```python
>>> from functools import reduce
>>> reduce(lambda x,y: x+y, [1,2,3,4,5])15
```

map(), filter()  내장 함수

reduce() 는 외장 함수

