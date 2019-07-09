# 다음과 같이 사용자가 입력한 문장에서 대소문를 구별해 각각의 갯수를 출력하는 프로그램을 작성하십시오.


"""
input
Hello World! 123

output
UPPER CASE 2
LOWER CASE 8
"""
a = 'Hello World! 123'

"""
print(a.isupper())
print(a.islower())
"""

upper = 0
lower = 0 

d = list(a)

for i in d:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1


print('UPPER CASE {}\nLOWER CASE {}'.format(upper, lower))