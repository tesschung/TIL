[TOC]



## site

| #    | links                                                  | description                 |
| ---- | ------------------------------------------------------ | --------------------------- |
|      | typora                                                 |                             |
| 1    | https://typora.io/                                     |                             |
| 2    | https://gist.github.com/ihoneymon/652be052a0727ad59601 |                             |
|      | python                                                 |                             |
| 1    | https://www.python.org/downloads/windows/              | python official site        |
|      | python module                                          |                             |
| 1    | https://wikidocs.net/79                                | python wikidocs site        |
| 2    | https://docs.python.org/3.7/library/random.html        | random                      |
|      | python study reference                                 |                             |
| 1    | https://dojang.io/mod/page/view.php?id=2307            |                             |
| 2    | https://wikidocs.net/16043                             |                             |
|      | API                                                    |                             |
| 1    | https://www.data.go.kr/dataset/15000581/openapi.do     | 대기오염정보 조회 서비스API |
|      |                                                        |                             |



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

|      | 함수/모듈명          | 함수/모듈2명                  | description                                                  | example                                         |
| ---- | -------------------- | ----------------------------- | ------------------------------------------------------------ | ----------------------------------------------- |
|      | 연산자               | +                             |                                                              |                                                 |
|      |                      | -                             |                                                              |                                                 |
|      |                      | *                             |                                                              |                                                 |
|      |                      | /                             |                                                              |                                                 |
|      |                      | **                            | 거듭제곱                                                     |                                                 |
|      |                      | %                             | 모듈러, 나머지를 구한다. a =10 b = 3 인 경우 a%b는 1         |                                                 |
|      | 논리                 | x and y                       | True if both the operands are true                           |                                                 |
|      |                      | x or y                        | True if either of the operands is true                       |                                                 |
|      |                      | not x                         | True if operand is false (complements the operand)           |                                                 |
|      |                      | x > y                         | Greater that - True if left operand is greater than the right |                                                 |
|      |                      | x < y                         | Less that - True if left operand is less than the right      |                                                 |
|      |                      | x == y                        | Equal to - True if both operands are equal                   |                                                 |
|      |                      | x != y                        | **Not equal to** - True if operands are not equal            |                                                 |
|      |                      | x >= y                        | Greater than or equal to - True if left operand is greater than or equal to the right |                                                 |
|      |                      | x <= y                        | Less than or equal to - True if left operand is less than or equal to the right |                                                 |
|      | 자료형               | `int`                         | 정수                                                         |                                                 |
|      |                      | `float`                       | 실수                                                         |                                                 |
|      |                      | `bool`                        | True/False                                                   |                                                 |
|      |                      | `str`                         | string                                                       |                                                 |
|      |                      | `list`                        | list                                                         |                                                 |
|      |                      | `tuple`                       | tuple                                                        |                                                 |
|      |                      | `set`                         | set                                                          |                                                 |
|      |                      | `dict`                        | dictionary                                                   |                                                 |
|      | 문자열 함수          | `len(값)`                     |                                                              | quote = "my best careet partner"<br/>len(quote) |
|      |                      | `index(찾을 문자)`            |                                                              |                                                 |
|      |                      | `upper()/lower()`             |                                                              | quote.upper()                                   |
|      |                      | `replace(바꿀문자, 새문자)`   |                                                              | filename.replace('SAMSUNG_', 'SSAFY_')          |
|      |                      | `count(target문자)`           |                                                              |                                                 |
|      |                      | `strip()`                     |                                                              | .strip()                                        |
|      |                      | `lstrip()`                    |                                                              |                                                 |
|      |                      | `rstrip()`                    |                                                              |                                                 |
|      |                      | `split(기준문자)`             |                                                              |                                                 |
|      |                      | `join`                        |                                                              | ",".join(score_list)                            |
|      | 리스트 함수          | `append(값) `                 | 요소 추가하기                                                | empty_list.append(1)                            |
|      |                      | `extend(리스트)`              |                                                              | empty_list.extend([1,2])                        |
|      |                      | `insert(인덱스, 값)`          | 특정 인덱스에 요소추가                                       | empty_list.insert(0, 100)                       |
|      |                      | `index(값)`                   | 특정값의 인덱스 구하기                                       | a.index(3)                                      |
|      |                      | ` count(값)`                  | 특정값의 개수구하기                                          | a.count(2)                                      |
|      |                      | `reverse()`                   | 순서 뒤집기                                                  | a.reverse()                                     |
|      |                      | ` pop(인덱스)`                | 리스트 요소삭제                                              | num = empty_list.pop(0)                         |
|      |                      | ` remove(값)`                 | 리스트 특정값을 찾아 삭제                                    | empty_list.remove(2)                            |
|      |                      | `sort(), sort(reverse=False)` | 정렬하기(오름차순)                                           | a.sort()                                        |
|      |                      | `sort(reverse=True)`          | 정렬하기(내림차순)                                           | a.sort(reverse=True)                            |
|      | 딕셔너리 기능        | `setdefault(키, 값)`          | 키-값 쌍 추가하기                                            |                                                 |
|      |                      | `update({키:값})`             | 키-값 수정하기                                               |                                                 |
|      |                      | ` clear()`                    | 모든 값 삭제                                                 |                                                 |
|      |                      | ` pop(키,기본값)`             | 키로 딕셔너리 항목삭제                                       |                                                 |
|      | 딕셔너리 할당과 복사 | `copy()`                      | 딕셔너리 복사                                                |                                                 |
|      |                      | `deepcopy()`                  | 중첩 딕셔너리의 경우                                         |                                                 |
|      |                      |                               |                                                              |                                                 |
|      |                      |                               |                                                              |                                                 |
|      |                      |                               |                                                              |                                                 |
|      |                      |                               |                                                              |                                                 |
|      |                      |                               |                                                              |                                                 |
|      |                      |                               |                                                              |                                                 |
|      |                      |                               |                                                              |                                                 |
|      |                      |                               |                                                              |                                                 |
|      |                      |                               |                                                              |                                                 |
|      |                      |                               |                                                              |                                                 |
|      |                      |                               |                                                              |                                                 |
|      |                      |                               |                                                              |                                                 |
|      |                      |                               |                                                              |                                                 |
|      |                      |                               |                                                              |                                                 |
|      |                      |                               |                                                              |                                                 |
|      |                      |                               |                                                              |                                                 |
|      |                      |                               |                                                              |                                                 |
|      |                      |                               |                                                              |                                                 |
|      |                      |                               |                                                              |                                                 |
|      |                      |                               |                                                              |                                                 |
|      |                      |                               |                                                              |                                                 |
|      |                      |                               |                                                              |                                                 |
|      |                      |                               |                                                              |                                                 |
|      |                      |                               |                                                              |                                                 |
|      |                      |                               |                                                              |                                                 |



## 함수/모듈 정리

|      | 모듈명   | 함수/모듈2명                                 | description                                                  | example                                                      |
| ---- | -------- | -------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
|      | `random` | `random`                                     |                                                              |                                                              |
|      |          | `random.choice(seq)`                         | Return a random element from the non-empty sequence seq. If seq is empty, raises IndexError. |                                                              |
|      | `os`     | `os`                                         | os가 할 수 있는 기능을 가져와서 python에서 실행              |                                                              |
|      |          | `os.system(str)`                             |                                                              | cmd = 'echo "Hello World"'                                   |
|      |          | `os.chdir(r'path')`                          | change file directory                                        | os.chdir(r'C:\Users\student\TIL\startCamp\02_day\file_handling') |
|      |          |                                              |                                                              |                                                              |
|      |          | `os.listdir(path)`                           | 특정 경로의 모든 파일의 이름을 가지고옴                      |                                                              |
|      |          | `os.path.splitext(filename)`                 | 확장자만 따로 분리                                           |                                                              |
|      |          | `os.rename(filename, f'SAMSUNG_{filename}')` | rename a file or a directory                                 | # 첫번째 인자로 넘어간 이름을, 두번째 인자로 넘어간 이름으로 바꾼다. |
|      | `csv`    |                                              |                                                              |                                                              |
|      |          | `csv.writerow(string)`                       |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |
|      |          |                                              |                                                              |                                                              |

