

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



## git bash	협업툴

| name                   | meaning                            | description                   |      | method           | example       |
| ---------------------- | ---------------------------------- | ----------------------------- | ---- | ---------------- | ------------- |
| ls                     | list                               | 현재 디렉토리 내용들을 나열   |      |                  |               |
| cd                     | change directory                   | 현재 작업하는 디렉토리로 변경 |      | cd 폴더명        | cd Documents/ |
| code .                 | start vscode                       |                               |      |                  |               |
| mkdir                  | make directory                     | 새로운 디렉토리 생성          |      |                  |               |
| echo                   |                                    | 문자열 출력                   |      | echo 문자열 출력 |               |
| rm                     | remove                             | 파일 지우기                   |      |                  |               |
| exit                   |                                    | 터미널 종료                   |      |                  |               |
| control+l              | reset                              |                               |      |                  |               |
| rm -r 폴더명/          |                                    |                               |      |                  |               |
| touch 원하는 폴더명.py | make a project in python           | 파이썬파일생성                |      |                  |               |
| python -V              | check the version of such language |                               |      |                  |               |

## vscode	project 생성 에디터	

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





## [github](https://github.com/)

[tesschung](https://github.com/tesschung)

git 이란?

* 코드의 히스토리 관리 도구

* 프로젝트 이전 버전 복원 및 변경 사항 비교 가능
* 협업 가능한 도구



작업 흐름

1.  **add**: 커밋할 목록에 추가, 원하는 **특정 코드**만 add가능

2. **commit**: 커밋 목록 만들기(create a snapshot )

3. **push**: 현재까지의 역사(commits)이 기록된 곳에 새로운 커밋 반영



git 기본

| name                                   | meaning | description                    | method | example |
| -------------------------------------- | ------- | ------------------------------ | ------ | ------- |
| $ git add helloworld.py                |         | git의 sub-command중 하나       |        |         |
| $ git commit -m                        |         | -로 시작하면 short name option |        |         |
| $ git config --global user.name "John" |         | --로 시작하면 long name option |        |         |



git 초기화

1. git bash 실행 후, 미리 설정되어있을지 모를 계정 정보 삭제

git config --global --unset credential.helper

git config --system --unset credential.helper

2. windows 자격 증명 관리자에서 git 관련 정보 삭제



등록방법

```bash
$ git config --global user.name "tesschung"
$ git config --global user.name

$ git config --global user.email "geobera0910@naver.com"
$ git config --global user.email

$ git config --global --list
user.name=tesschung
user.email=geobera0910@naver.com
```

![1562639469992](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562639469992.png)





