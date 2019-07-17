'''
※ SW Expert 아카데미의 문제를 무단 복제하는 것을 금지합니다.

삼성전자에 입사한 종민이는 회사 근처로 이사를 하게 되었다.
그런데 집의 위치가 두 수도 회사 A, B 중간에 위치하기에 원하는 수도 회사를 선택할 수 있게 되었는데, 
두 회사 중 더 적게 수도 요금을 부담해도 되는 회사를 고르려고 한다.
종민이가 알아본 결과 두 회사의 수도 요금은 한 달 동안 사용한 수도의 양에 따라 다음과 같이 정해진다.

A사 : 1리터당 P원의 돈을 내야 한다.
B사 : 기본 요금이 Q원이고, 월간 사용량이 R리터 이하인 경우 요금은 기본 요금만 청구된다. 
하지만 R 리터보다 많은 양을 사용한 경우 초과량에 대해 1리터당 S원의 요금을 더 내야 한다.

종민이의 집에서 한 달간 사용하는 수도의 양이 W리터라고 할 때, 
요금이 더 저렴한 회사를 골라 그 요금을 출력하는 프로그램을 작성하라.

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스마다 첫 번째 줄에 위 본문에서 설명한 대로 P, Q, R, S, W(1 ≤ P, Q, R, S, W ≤ 10000, 자연수)가 순서대로 공백 하나로 구분되어 주어진다.

[출력]
각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 종민이가 내야 하는 수도 요금을 출력한다.

입력
2

8 300 100 10 250
 
출력
#1 90
#2 1800
'''

'''
T -> 2
input().split()
LIST -> INDEX 계산

9 
P : A사의 1리터당 가격

100 
Q : B사의 기본요금, 월간 사용량이 R리터 이하인 경우 요금은 Q만 청구됨 
20
R : B사는 R리터보다 많은양을 초과시 
3
S : 1리터당 S원의 요금을 추가로낸다

10
W : 종민이 사용하는 수도의 양은 W리터다
'''

'''
a = input()
print(a)


b = list(input().split())
print(b)
print(b[1])


    A = W*P

    if W < R:
        B = Q
    elif W > R:
        B = Q + ((w-R)*S)

if A >= B:
    print(B)
else:
    print(A)
'''

for T in range(int(input())):
    ABW = list(input().split())
    ABW = list(map(int, ABW))
    result = 0
    P = ABW[0]
    Q = ABW[1]
    R = ABW[2]
    S = ABW[3]
    W = ABW[4]
    
    A = W*P

    if W < R:
        B = Q
    elif W > R:
        B = Q + ((W-R)*S)

    if A >= B:
        result = B
    elif A <= B:
        result = A
    print(f'#{T+1} {result}')


for T in range(int(input())):
    ABW = input().split()
    P, Q, R, S, W = map(int, ABW)
    result = 0
    A = W*P
    if W < R:
        B = Q
    elif W > R:
        B = Q + ((W-R)*S)
    if A >= B:
        result = B
    elif A <= B:
        result = A
    print(f'#{T+1} {result}')


for T in range(int(input())):
    P, Q, R, S, W = map(int, input().split())
    r = 0
    A = W*P
    if W < R:
        B = Q
    elif W > R:
        B = Q + ((W-R)*S)
    if A >= B:
        r = B
    elif A <= B:
        r = A
    print(f'#{T+1} {r}')

#박권응님
test_num = int(input())
C_A, C_B = 0, 0
for i in range(test_num):
    Q = list(map(int, input().split()))
    W = Q[4]
    A_r = Q[0]
    B_b = Q[1]
    B_c = Q[2]
    B_r = Q[3]
    result_A = 0
    result_B = 0
    result_A = W*A_r
    if W < B_c :
        result_B = B_b
    else :
        result_B = B_b + (W-B_c)*B_r
    if result_A > result_B:
        print(f'#{i+1} {result_B}')
    else :
        print(f'#{i+1} {result_A}')


#김은성님
T = int(input())

for i in range(T):
    p, q, r, s, w = list(map(int,input().split())) #각각의 변수에 값을 입력
    a = w * p 										#A사 요금
    b = q if w <= r else q + (w - r) * s	  #B사 요금
    price = min(a, b) 								#둘중 낮은가격
    print(f'#{i+1} {price}')


# 수정필(하기 문제, 문제 읽기 필)
# 6번째줄 if랑 8번째줄 elif에서 W = R 이 없어서, 
# W이랑 R에 같은 값 들어가면 B가 안나올수도 있을거같아요
for T in range(int(input())):
    P, Q, R, S, W = map(int, input().split())
    A = W*P
    if W <= R:
        B = Q
    elif W > R:
        B = Q + ((W-R)*S)
    r = min(A, B)
    print(f'#{T+1} {r}')


