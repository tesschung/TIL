"""
6288. [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 2. 자료구조 -리스트, 튜플 12 D1

리스트 내포 기능을 이용하여 

requirement)
1부터 20사이의 숫자 중 

condition1)
3의 배수가 아니거나
condition2)
5의 배수가 아닌 


condition3)
숫자들의 제곱 값으로 구성된 

all condition1)
리스트 객체

를 출력하는 프로그램을 작성하십시오.

출력
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 256, 289, 324, 361, 400]
"""

d = []

for i in range(1,21):
    if i%3 != 0 or i%5 != 0:
        # print(i)
        
        d.append(i*i)

print(d)