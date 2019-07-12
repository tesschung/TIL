"""
6329. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 8. 함수의 기초 10
  

인자로 전달된 숫자를 이용해 카운트다운하는 함수 countdown을 정의하고,
  

이 함수를 이용하여 countdown(0), countdown(10)을 순서대로 실행하십시오.

0보다 작거나 같은 인자가 전달되었을 경우 "카운트다운을 하려면 0보다 큰 입력이 필요합니다."를 출력하십시오.
출력
카운트다운을 하려면 0보다 큰 입력이 필요합니다.

10

9

8

7

6

5

4

3

2

1

"""

def countdown(num):
    list_ = []
    if num == 0:
        print('카운트다운을 하려면 0보다 큰 입력이 필요합니다.')
    else:
        for i in range(1, num+1): #1~10까지의 리스트 생성, 리스트 안에서 원소 순환
            list_.append(i) #새로운 리스트 생성
            #print(list_)
        for ai in reversed(list_): #리스트 reversed
            print(ai)

countdown(0)
countdown(10)
        


