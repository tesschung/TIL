'''
2369. [AtCoder Beginner Contest 073] B. Theater 

Joisino is working as a receptionist at a theater.
The theater has 100000 seats, numbered from 1 to 100000.

According to her memo,
N groups of audiences have come so far, N만큼의 그룹 관객들 
and 
the i-th group occupies the consecutive seats 연속적으로 Li부터 Ri까지 앉아있음
from Seat Li to Seat Ri (inclusive).
How many people are sitting at the theater now? 얼마나 많은 관객들이 극장에 앉아있는지

Constraints
1. 1 ≤ N ≤ 1000 
2. 1 ≤ Li ≤ Ri ≤ 100000
3. No seat is occupied by more than one person. 1 seat = 1 person
4. All input values are integers. 정수

Input
The first line of the input contains an integer T,
the number of test sets (1 ≤ T ≤ 10).
For each test set, 
the input is given from Standard Input in the following format:

N
L1   R1
.
.
LN   RN

입력
2 테스트케이스2개가 주어짐 1~10사이로 주어질 것


1          N 1 1배열
24 30      답 7명  1 ≤ Li ≤ Ri ≤ 100000
            24 25 26 27 28 29 30   7명

2          N 2
6 8        2 배열
3 3        답 4명   1 ≤ Li ≤ Ri ≤ 100000
            6 7 8
            3
            4명

출력
#1 7
#2 4
'''

for ai in range(int(input())):
    total = 0
    c = 0
    for bi in range(int(input())):
        d = input().split()
        prin(d) #['24', '30']
        d = list(map(int, d))
        total = d[1]+1-d[0]
        c += total
    print(f'#{ai+1} {c}')


        #d = map(lambda x:x-x, d[0],d[1], d)

'''shorten code'''
for ai in range(int(input())):
    t = 0
    c = 0
    for bi in range(int(input())):
        d = list(map(int, input().split()))
        t = d[1]+1-d[0]
        c += t
    print(f'#{ai+1} {c}')

'''shorten code'''
'''
for ai in range(int(input())):
    t, c = 0, 0
    for bi in range(int(input())):
        d = list(map(int, input().split()))
        t = d[1]+1-d[0]
        c += t
    print(f'#{ai+1} {c}')
'''