http://www.pythontutor.com/visualize.html#mode=edit

0716
단어넣기 
백만장자

0717
파리퇴치 
패턴길이
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5P1kNKAl8DFAUq&categoryId=AV5P1kNKAl8DFAUq&categoryType=CODE
a = list(input())
b = list(reversed(a))
if b == a:
    print(True)
else:
    print(False)
아니다...ㅠㅠ

## 이걸 앞으로 계속 전진하면서 검증
## 몫이 점점 커지게...??
def palindrome(word):
    list_word = list(word) # 3 => 1 // 4 => 2
    for i in range(len(list_word) // 2) # 몫을 구한다.
    	if list_word[i] != list_word[-i-1]:
            return False
    return True

def palindrome(word):
    return word == word[::-1]


달팽이숫자

0718
1983. 조교의 성적 매기기 https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PwGK6AcIDFAUq&categoryId=AV5PwGK6AcIDFAUq&categoryType=CODE
1959
2005