[TOC]



## site

| #    | links                                                  | description                      |
| ---- | ------------------------------------------------------ | -------------------------------- |
|      | typora                                                 |                                  |
| 1    | https://typora.io/                                     |                                  |
| 2    | https://gist.github.com/ihoneymon/652be052a0727ad59601 |                                  |
|      | python                                                 |                                  |
| 1    | https://www.python.org/downloads/windows/              | python official site             |
|      | python module                                          |                                  |
| 1    | https://wikidocs.net/79                                | python wikidocs site             |
| 2    | https://docs.python.org/3.7/library/random.html        | random                           |
|      | python study reference                                 |                                  |
| 1    | https://dojang.io/mod/page/view.php?id=2307            |                                  |
| 2    | https://wikidocs.net/16043                             |                                  |
|      | API                                                    |                                  |
| 1    | https://www.data.go.kr/dataset/15000581/openapi.do     | 대기오염정보 조회 서비스API      |
|      | NLP                                                    |                                  |
| 1    | http://wikidocs.net/21667                              | 딥러닝을 이용한 자연어 처리 입문 |



## git bash 사용법

| name                   | meaning                            | description                   |      | method           | example                              |
| ---------------------- | ---------------------------------- | ----------------------------- | ---- | ---------------- | ------------------------------------ |
| ls                     | list                               | 현재 디렉토리 내용들을 나열   |      |                  |                                      |
| cd                     | change directory                   | 현재 작업하는 디렉토리로 변경 |      | cd 폴더명        | cd Documents/                        |
| code .                 | start vscode                       |                               |      |                  |                                      |
| mkdir                  | make directory                     | 새로운 디렉토리 생성          |      |                  |                                      |
| echo                   |                                    | 문자열 출력                   |      | echo 문자열 출력 |                                      |
| rm                     | remove                             | 파일 지우기                   |      |                  |                                      |
| exit                   |                                    | 터미널 종료                   |      |                  |                                      |
| control+l              | reset                              |                               |      |                  |                                      |
| rm -r 폴더명/          |                                    |                               |      |                  |                                      |
| touch 원하는 폴더명.py | make a project in python           | 파이썬파일생성                |      |                  |                                      |
| python -V              | check the version of such language |                               |      |                  |                                      |
| echo "string"          |                                    |                               |      |                  | $ echo "hello world"<br/>hello world |
| history                |                                    | 사용한 모든 명령어 확인       |      |                  |                                      |
| ls -l                  |                                    |                               |      |                  |                                      |

## vscode project 생성 에디터 사용법

| name                                             | meaning  | description |      | method | example |
| ------------------------------------------------ | -------- | ----------- | ---- | ------ | ------- |
| control + ~                                      | terminal |             |      |        |         |
| control + p +shift -> terminal select -> gitbash |          |             |      |        |         |



## Typora 사용법

Content

([TOC]로 목차 자동 생성)

[TOC]



Headings(1~6, 글자앞 #)

# # H1

## ## H2

### ### H3

#### #### H4

##### ##### H5

###### ###### H6



Emphasis

**Information Bold**  (앞뒤 별표**, control+B)

*Information Italic* (앞뒤 별표*, control+i)



원본확인

control+/ 



Blockquotes

`soup` (앞뒤 백탭`)



Codeblock (```python+enter)

```python
import random
menu = ['점심', '저녁']
choice = random.choice(menu)
print(choice) #점심 or 저녁
```



Image (![이미지명](이미지주소))

![심슨](https://t1.daumcdn.net/cfile/tistory/247DFA4358B1426A31)



Table

(Control+T)

| header   |      |      |      |      |      |
| -------- | ---- | ---- | ---- | ---- | ---- |
| contents |      |      |      |      |      |
|          |      |      |      |      |      |



Blacklist

(enter 2번으로 종료가능)

* (*+space)

1. (number list)



Link([naver]( 해당주소))

[네이버](http://www.naver.com)



<h1>html tag도 작성 가능<h1>
</h1>
</h1>





## 기본함수 정리

|      | 함수/모듈명          | 함수/모듈2명                                        | description                                                  | example                                                      |
| ---- | -------------------- | --------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
|      | 연산자               | +                                                   | 더하기                                                       |                                                              |
|      |                      | -                                                   | 빼기                                                         |                                                              |
|      |                      | *                                                   | 곱하기                                                       |                                                              |
|      |                      | **2                                                 | 제곱                                                         |                                                              |
|      |                      | /                                                   | 나눗셈                                                       |                                                              |
|      |                      | **                                                  | 거듭제곱                                                     |                                                              |
|      |                      | %                                                   | 모듈러, 나머지를 구한다. a =10 b = 3 인 경우 a%b는 1         |                                                              |
|      | 논리                 | x and y                                             | True if both the operands are true                           |                                                              |
|      |                      | x or y                                              | True if either of the operands is true                       |                                                              |
|      |                      | not x                                               | True if operand is false (complements the operand)           |                                                              |
|      |                      | x > y                                               | Greater that - True if left operand is greater than the right |                                                              |
|      |                      | x < y                                               | Less that - True if left operand is less than the right      |                                                              |
|      |                      | x == y                                              | Equal to - True if both operands are equal                   |                                                              |
|      |                      | x != y                                              | **Not equal to** - True if operands are not equal            |                                                              |
|      |                      | x >= y                                              | Greater than or equal to - True if left operand is greater than or equal to the right |                                                              |
|      |                      | x <= y                                              | Less than or equal to - True if left operand is less than or equal to the right |                                                              |
|      | 자료형               | `int`                                               | 정수                                                         |                                                              |
|      |                      | `float`                                             | 실수                                                         |                                                              |
|      |                      | `bool`                                              | True/False                                                   |                                                              |
|      |                      | `str`                                               | string                                                       |                                                              |
|      |                      | `list`                                              | list                                                         |                                                              |
|      |                      | `tuple`                                             | tuple                                                        |                                                              |
|      |                      | `set`                                               | set                                                          |                                                              |
|      |                      | `dict`                                              | dictionary                                                   |                                                              |
|      | 문자열 함수          | `len(값)`                                           |                                                              | quote = "my best careet partner"<br/>len(quote)              |
|      |                      | `index(찾을 문자)`                                  |                                                              |                                                              |
|      |                      | `upper()/lower()`                                   |                                                              | quote.upper()                                                |
|      |                      | `replace(바꿀문자, 새문자)`                         |                                                              | filename.replace('SAMSUNG_', 'SSAFY_')                       |
|      |                      | `count(target문자)`                                 |                                                              |                                                              |
|      |                      | `strip()`                                           |                                                              | .strip()                                                     |
|      |                      | `lstrip()`                                          |                                                              |                                                              |
|      |                      | `rstrip()`                                          |                                                              |                                                              |
|      |                      | `split(기준문자)`                                   |                                                              |                                                              |
|      |                      | `join`                                              |                                                              | ",".join(score_list)                                         |
|      | 리스트 함수          | `append(값) `                                       | 요소 추가하기                                                | empty_list.append(1)                                         |
|      |                      | `extend(리스트)`                                    |                                                              | empty_list.extend([1,2])                                     |
|      |                      | `insert(인덱스, 값)`                                | 특정 인덱스에 요소추가                                       | empty_list.insert(0, 100)                                    |
|      |                      | `index(값)`                                         | 특정값의 인덱스 구하기                                       | a.index(3)                                                   |
|      |                      | ` count(값)`                                        | 특정값의 개수구하기                                          | a.count(2)                                                   |
|      |                      | `reverse()`                                         | 순서 뒤집기                                                  | a.reverse()                                                  |
|      |                      | ` pop(인덱스)`                                      | 리스트 요소삭제                                              | num = empty_list.pop(0)                                      |
|      |                      | ` remove(값)`                                       | 리스트 특정값을 찾아 삭제                                    | empty_list.remove(2)                                         |
|      |                      | `sort(), sort(reverse=False)`                       | 정렬하기(오름차순)                                           | a.sort()                                                     |
|      |                      | `sort(reverse=True)`                                | 정렬하기(내림차순)                                           | a.sort(reverse=True)                                         |
|      |                      |                                                     | 중복값제거                                                   | 1. python의 자료형 중 set 을 이용한 방법   set으로 변환 후 다시 list화 -> set은 1) 중복허용x 2) 순서가 존재x |
|      | 딕셔너리 기능        | `setdefault(키, 값)`                                | 키-값 쌍 추가하기                                            |                                                              |
|      |                      | `update({키:값})`                                   | 키-값 수정하기                                               |                                                              |
|      |                      | ` clear()`                                          | 모든 값 삭제                                                 |                                                              |
|      |                      | ` pop(키,기본값)`                                   | 키로 딕셔너리 항목삭제                                       |                                                              |
|      | 딕셔너리 할당과 복사 | `copy()`                                            | 딕셔너리 복사                                                |                                                              |
|      |                      | `deepcopy()`                                        | 중첩 딕셔너리의 경우                                         |                                                              |
|      |                      | `.items()`                                          | .items()로 key, value 가져오기                               |                                                              |
|      |                      | `.keys()`                                           | key만 가져오기                                               |                                                              |
|      |                      | `.values()`                                         | value만 가져오기                                             |                                                              |
|      |                      |                                                     |                                                              |                                                              |
|      |                      |                                                     |                                                              |                                                              |
|      |                      |                                                     |                                                              |                                                              |
|      |                      |                                                     |                                                              |                                                              |
|      |                      |                                                     |                                                              |                                                              |
|      |                      |                                                     |                                                              |                                                              |
|      |                      |                                                     |                                                              |                                                              |
|      |                      |                                                     |                                                              |                                                              |
|      |                      |                                                     |                                                              |                                                              |
|      |                      |                                                     |                                                              |                                                              |
|      |                      | `map(사용하고자 하는 함수,반복으로 돌리고 싶은 것)` |                                                              |                                                              |
|      |                      |                                                     |                                                              |                                                              |
|      |                      |                                                     |                                                              |                                                              |
|      |                      | sum([1,3,4])                                        |                                                              | #8                                                           |
|      |                      | len([1,3,4])                                        |                                                              | #3                                                           |
|      |                      | max([1,3,4])                                        |                                                              | #4                                                           |
|      |                      | min([1,3,4])                                        |                                                              | #1                                                           |
|      |                      | `round(float숫자)`                                  | 반올림                                                       |                                                              |
|      |                      |                                                     |                                                              |                                                              |
|      |                      |                                                     |                                                              |                                                              |
|      |                      |                                                     |                                                              |                                                              |
|      |                      |                                                     |                                                              |                                                              |



## 함수/모듈 정리

|      | 모듈명   | 함수/모듈2명                                        | description                                                  | example                                                      |
| ---- | -------- | --------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
|      | `random` | `random`                                            |                                                              |                                                              |
|      |          | `random.choice(seq)`                                | Return a random element from the non-empty sequence seq. If seq is empty, raises IndexError. |                                                              |
|      |          | `random.sample(seq,number)`                         |                                                              |                                                              |
|      | `os`     | `os`                                                | os가 할 수 있는 기능을 가져와서 python에서 실행              |                                                              |
|      |          | `os.system(str)`                                    |                                                              | cmd = 'echo "Hello World"'                                   |
|      |          | `os.chdir(r'path')`                                 | change file directory                                        | os.chdir(r'C:\Users\student\TIL\startCamp\02_day\file_handling') |
|      |          |                                                     |                                                              |                                                              |
|      |          | `os.listdir(path)`                                  | 특정 경로의 모든 파일의 이름을 가지고옴                      |                                                              |
|      |          | `os.path.splitext(filename)`                        | 확장자만 따로 분리                                           |                                                              |
|      |          | `os.rename(filename, f'SAMSUNG_{filename}')`        | rename a file or a directory                                 | # 첫번째 인자로 넘어간 이름을, 두번째 인자로 넘어간 이름으로 바꾼다. |
|      | `csv`    |                                                     |                                                              |                                                              |
|      |          | `csv.writerow(string)`                              |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      | `flask`  |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      | `jinja2` | `render_template('파일명.html', 전달변수=원래변수)` |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |
|      |          |                                                     |                                                              |                                                              |

### 내장함수 정리: 외울함수

| 모듈명 | 함수/모듈2명                                       | description                                                  | example                                                      |
| ------ | -------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
|        | [abs](https://wikidocs.net/32#abs)                 | abs(x)는 어떤 숫자를 입력받았을 때, 그 숫자의 절댓값을 돌려주는 함수이다. | abs(-3) -> 3                                                 |
|        | [all](https://wikidocs.net/32#all)                 | all(x)는 반복 가능한(iterable) 자료형 x를 입력 인수로 받으며 이 x가 모두 참이면 True, 거짓이 하나라도 있으면 False를 돌려준다. | all([1, 2, 3, 0]) -> False                                   |
|        | [any](https://wikidocs.net/32#any)                 | any(x)는 x 중 하나라도 참이 있으면 True를 돌려주고, x가 모두 거짓일 때에만 False를 돌려준다. all(x)의 반대이다. | any([0, ""]) -> False 리스트 자료형 [0, ""]의 요소 0과 ""은 모두 거짓이므로 False를 돌려준다. any([1, 2, 3, 0]) -> True 리스트 자료형 [1, 2, 3, 0] 중에서 1, 2, 3이 참이므로 True를 돌려준다. |
|        | [chr](https://wikidocs.net/32#chr)                 | chr(i)는 아스키(ASCII) 코드 값을 입력받아 그 코드에 해당하는 문자를 출력하는 함수이다. | chr(97) -> 'a'                                               |
|        | [dir](https://wikidocs.net/32#dir)                 |                                                              |                                                              |
|        | [divmod](https://wikidocs.net/32#divmod)           |                                                              |                                                              |
|        | **[enumerate](https://wikidocs.net/32#enumerate)** | enumerate는 "열거하다"라는 뜻이다. 이 함수는 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 돌려준다. | for i, name in enumerate(['body', 'foo', 'bar']): ...     print(i, name) |
|        | [eval](https://wikidocs.net/32#eval)               |                                                              |                                                              |
|        | [filter](https://wikidocs.net/32#filter)           |                                                              |                                                              |
|        | [hex](https://wikidocs.net/32#hex)                 |                                                              |                                                              |
|        | [id](https://wikidocs.net/32#id)                   |                                                              |                                                              |
|        | [isinstance](https://wikidocs.net/32#isinstance)   |                                                              |                                                              |
|        | [map](https://wikidocs.net/32#map)                 |                                                              |                                                              |
|        | [oct](https://wikidocs.net/32#oct)                 |                                                              |                                                              |
|        | [open](https://wikidocs.net/32#open)               |                                                              |                                                              |
|        | [ord](https://wikidocs.net/32#ord)                 |                                                              |                                                              |
|        | [pow](https://wikidocs.net/32#pow)                 |                                                              |                                                              |
|        | [sorted](https://wikidocs.net/32#sorted)           |                                                              |                                                              |
|        | [zip](https://wikidocs.net/32#zip)                 |                                                              |                                                              |
|        |                                                    |                                                              |                                                              |
|        |                                                    |                                                              |                                                              |
|        |                                                    |                                                              |                                                              |
|        |                                                    |                                                              |                                                              |
|        |                                                    |                                                              |                                                              |
|        |                                                    |                                                              |                                                              |
|        |                                                    |                                                              |                                                              |
|        |                                                    |                                                              |                                                              |
|        |                                                    |                                                              |                                                              |
|        |                                                    |                                                              |                                                              |
|        |                                                    |                                                              |                                                              |
|        |                                                    |                                                              |                                                              |
|        |                                                    |                                                              |                                                              |
|        |                                                    |                                                              |                                                              |
|        |                                                    |                                                              |                                                              |
|        |                                                    |                                                              |                                                              |
|        |                                                    |                                                              |                                                              |
|        |                                                    |                                                              |                                                              |
|        |                                                    |                                                              |                                                              |
|        |                                                    |                                                              |                                                              |
|        |                                                    |                                                              |                                                              |
|        |                                                    |                                                              |                                                              |
|        |                                                    |                                                              |                                                              |
|        |                                                    |                                                              |                                                              |
|        |                                                    |                                                              |                                                              |
|        |                                                    |                                                              |                                                              |
|        |                                                    |                                                              |                                                              |
|        |                                                    |                                                              |                                                              |
|        |                                                    |                                                              |                                                              |
|        |                                                    |                                                              |                                                              |





[이스케이프 코드란?]**

문자열 예제에서 여러 줄의 문장을 처리할 때 백슬래시 문자와 소문자 n을 조합한 `\n` 이스케이프 코드를 사용했다. 이스케이프 코드란 프로그래밍할 때 사용할 수 있도록 미리 정의해 둔 "문자 조합"이다. 주로 출력물을 보기 좋게 정렬하는 용도로 사용한다. 몇 가지 이스케이프 코드를 정리하면 다음과 같다.

| 코드   | 설명                                                    |
| ------ | ------------------------------------------------------- |
| `\n`   | 문자열 안에서 줄을 바꿀 때 사용                         |
| `\t`   | 문자열 사이에 탭 간격을 줄 때 사용                      |
| `\\`   | 문자 `\`를 그대로 표현할 때 사용                        |
| `\'`   | 작은따옴표(`'`)를 그대로 표현할 때 사용                 |
| `\"`   | 큰따옴표(`"`)를 그대로 표현할 때 사용                   |
| `\r`   | 캐리지 리턴(줄 바꿈 문자, 현재 커서를 가장 앞으로 이동) |
| `\f`   | 폼 피드(줄 바꿈 문자, 현재 커서를 다음 줄로 이동)       |
| `\a`   | 벨 소리(출력할 때 PC 스피커에서 '삑' 소리가 난다)       |
| `\b`   | 백 스페이스                                             |
| `\000` | 널 문자                                                 |



**왼쪽 정렬**

```
>>> "{0:<10}".format("hi")
'hi        '
```

`:<10` 표현식을 사용하면 치환되는 문자열을 왼쪽으로 정렬하고 문자열의 총 자릿수를 10으로 맞출 수 있다.

**오른쪽 정렬**

```
>>> "{0:>10}".format("hi")
'        hi'
```

오른쪽 정렬은 `:<` 대신 `:>`을 사용하면 된다. 화살표 방향을 생각하면 어느 쪽으로 정렬되는지 바로 알 수 있을 것이다.

**가운데 정렬**

```
>>> "{0:^10}".format("hi")
'    hi    '
```

`:^` 기호를 사용하면 가운데 정렬도 가능하다.

# ToyProject 사용방법

1. 내고 싶은 문제가 있다면 폴더를 만듭니다.
   (문제 제시 시 본인의 **이름 혹은 닉네임** 명시)
2. 폴더 안에 txt 형식으로 문제를 저장합니다.
3. follower들은 문제를 각자 풀어 자신만의 답안을 만듭니다.
   (제출 시에 **닉네임-제출 날짜**로 제목 통일할게요!)
4. 답안을 제출할 때는 반드시 Pull을 받은 후에 Push 해주세요.
5. **다른 사람의 답안은 수정, 삭제 금지!! 열어보는 것도 가급적 github에서만!**

------

### 알고리즘 공부 사이트 모음

[Codingbat](https://codingbat.com/python): 처음 시작하기에 좋음. 코드 돌아가는 과정을 보여줘서 내가 어디서 틀렸는지 알 수 있음

[Checkio](https://checkio.org/): *강추*.디자인 예쁨. 연습문제 다수, 게임처럼 레벨 및 포인트가 있어서 재미있음. 솔루션 및 다른 사람 코드 peer review 가능

[백준 온라인 저지](https://www.acmicpc.net/): 알고리즘 공부하면 제일 먼저 생각나는 사이트. 거의 모든 문제 있음. **삼성 역량 테스트 모음 등**

[삼성 SW expert academy](https://swexpertacademy.com/main/main.do): 삼성에서 만든 알고리즘 사이트. 삼성 역량 테스트 상시 시험을 볼 수 있음

[HackerRank](https://www.hackerrank.com/dashboard): 영문판 알고리즘 연습 사이트. 영어실력 향상도 덤



*****

# 0712 마스터할list

OOP 공부!!!!

XLNET comparison with BERT

https://arxiv.org/abs/1906.08237

https://www.notion.so/XLNet-Generalized-Autoregressive-Pretraining-for-Language-Understanding-19-06-25-f4b608f11dfc4c8c8eb4c504f867d4aa

https://blog.pingpong.us/xlnet-review/





README.md 정리 190712(복습차원)

python의 flask사용하여 chatbot만듦

api 토큰등은 환경변수를 사용하여 관리함

telegram에 접속해서 tess_bot을 검색하면 사용해볼수있어요~

/한영

/영한

"Chat-bot:  Implement Translation Functionality using Naver Papago"

