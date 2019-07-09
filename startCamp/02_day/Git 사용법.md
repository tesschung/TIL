# Git

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

```bash
$ git status
```



