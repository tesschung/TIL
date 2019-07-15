[TOC]

# Git

[Reference](https://backlog.com/git-tutorial/kr/)

## 기본 명령어

1. Git 저장소 설정

   ```bash
   $ git init
   ```

   주의! 반드시 현재 디렉토리에 git을 사용하고 있는지, (master)표기가 없는지 확인할 것!

2. Git add

`git add`는 현재 working directory에서 commit 할 목록에 파일들을 담아 놓는 것이다.

그리고 그 목록은 `index(staging area)`라고 한다.

```bash
$ git add <폴더이름 혹은 파일이름>
```

3. Git commit

현재 소스코드 상태를 저장하는 것, **스냅샷**을 찍는것과 동일하다.

`staging area` (git add로 추가한 파일들이 담기는 곳) 에 있는 내용을 이력으로 기록한다.

```bash
$ git commit -m "커밋 메세지"
```



4. Git status

git의 현재 상태를 확인한다.

커밋할 목록에 담겨있는지 혹은 untracked인지, 커밋할 매녁이 있는지 등등 다양한 정보를 제공한다.

```bash
$ git status
```



5. Git log

   현재까지 커밋된 모든 이력을 확인 할 수 있다.

   ```bash
   $ git log
   ```

   

## 원격 저장소 활용하기

1. 원격 저장소 (remote repository) 등록하기

   ```bash
   $ git remote add origin __경로__
   ```

   원격 저장소(remote)를 등록(add)한다. *origin* 이라는 이름으로!

   origin: name of remote

   최초에 한번만 등록하면 된다.

   아래의 명령어로 현재 등록된 원격 저장소를 확인 할 수 있다.

   ```bash
   $ git remote -v
   origin  https://github.com/tesschung/TIL.git (fetch)
   origin  https://github.com/tesschung/TIL.git (push)
   ```

2. 원격 저장소에 올리기

   ```bash
   $ git push origin master
   ```

   origin이라는 원격저장소의 *master* *브랜치*로 지금까지의 커밋 내역을 올려줘!

   master: name of the main branch

   branch: 하나의 작업에서 branch를 나눠 작업 가능하고, 나중에 master branch에 병합하여 히스토리 관리 가능

3. 원격 저장소에서 가져오기

```bash
$ git pull origin master
```

4. 원격 저장소를 로컬에 복사하기

```bash
$ git clone __경로__
```

다운 받기를 원하는 폴더에서 git bash를 열고 위의 명령어를 입력한다.

경로는 github에서 우측에있는 초록색 버튼을 누르면 나타난다.

![1562649660587](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562649660587.png)

## 재등록

```bash
$ git add .
$ git commit -m "190709"
$ git status
$ git push origin master
```



## 추가 명령어

```bash
$ touch .gitignore

# beam editor
$ vi .gitignore
i : 끼워넣기 실행
파일명/ 입력시 git으로 더이상 관리하지 않음
**.txt 
esc: 일반모드
: :명령어 입력
wq w저장 q나가기 저장하고 나가기
```

[gitignore](https://gitignore.io/) : 환경에 맞춰 필요한 것  .gitignore할 수 있도록 목록 생성



## [github](https://github.com/) 사용법 (Draft)

[tesschung](https://github.com/tesschung)

[TIL](https://github.com/tesschung/TIL.git)

git 이란?

- 코드의 히스토리 관리 도구
- 프로젝트 이전 버전 복원 및 변경 사항 비교 가능
- 협업 가능한 도구



작업 흐름

1. **add**: 커밋할 목록에 추가, 원하는 **특정 코드**만 add가능
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



- 등록방법

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

git init으로 master 설정

잘못 master생성시 **$ rm -rf .git/**



git에 등록하기

```bash
$ git add 01_day/
```

![1562643928270](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562643928270.png)

commit이 되어있지 않은 파일

![1562643993040](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562643993040.png)

commit 준비완료

![1562644051764](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562644051764.png)

commit 완료

![1562644069696](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562644069696.png)

01_day commit완료하여 더이상 나타나지 않음

![1562644146585](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562644146585.png)

git log 사용하여 commit 확인 가능

![1562645388022](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562645388022.png)

원격저장소 관리

![1562645449960](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562645449960.png)

원격저장소 저장 완료

![1562645808511](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562645808511.png)

commit내용을 origin에 push

등록완료



- re등록 (새로운 device에서 작업하고 싶을 경우, local에 commited update내용 적용)

![1562646899204](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562646899204.png)

git pull origin master







##### Clone

* git clone url

  ![1563162214340](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1563162214340.png)