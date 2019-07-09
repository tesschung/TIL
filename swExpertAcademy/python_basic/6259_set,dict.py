# 다음과 같이 사용자가 입력한 문장에서 숫자와 문자를 구별해 
# 각각의 개수를 출력하는 프로그램을 작성하십시오.

"""
input
hello world! 123


output
LETTERS 10
DIGITS 3
"""
a = 'hello world!'
b = '123'
c = 'hello world! 123'

# print(b.isdigit())
# print(a.isalpha())

letter = 0
digit = 0
d = list(c)
# print(type(d))

for i in d:
    print(i)
    if i.isdigit():
        digit += 1
        
    elif i.isalpha():
        letter += 1

# print(digit)
# print(letter)


print("LETTERS {} \nDIGITS {}".format(letter,digit))