
'''
http://www.pythontutor.com/visualize.html#mode=edit

0716
단어넣기 
백만장자

0717
파리퇴치 
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PzOCKAigDFAUq&categoryId=AV5PzOCKAigDFAUq&categoryType=CODE&&&

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

'''

'''
def bisectionmethod(x2):
    stable_number = 2 ** 0.5 #1.4142135623730951
    compare_number = 0.00001
    x = 1.25

    m = 1.5
    d = m ** 2

    # 두 구간의 차이가 0.00001 보다 작으면 근을 찾은 것으로 간주
    if (d - (x2 ** 2)) < compare_number: #0.6875
        if (x2 ** 2) < stable_number < d:
            return f'{x2 ** 2} < {stable_number} < {d}'
    
    else:  
        x2 = (x + m)/2
        return bisectionmethod(x2)
     
        #print(f'{x2 ** 2} < {stable_number} < {d}')

bisectionmethod(1.25)
'''


'''
print((1.5 ** 2) - (1.25**2))
print(2**0.5)
'''

def bisectionmethod_second(left, right): # 1.25 1.5
    if right - left < 0.0001:
        return f'끝났습니다.'

    else:    
        stable_number = 2 ** 0.5 #1.4142135623730951
        middle = (left + right) / 2

        if middle < stable_number:
            left = middle
            print(f'{middle} < {stable_number} < {right}')
            return bisectionmethod_second(left, right)

        elif middle > stable_number:
            right = middle
            print(f'{left} < {stable_number} < {middle}')
            return bisectionmethod_second(left, right)
        
print(bisectionmethod_second(1.25, 1.5))



a = [1, 2]
print(sum(a))