'''
1288. 새로운 불면증 치료법
※ SW Expert 아카데미의 문제를 무단 복제하는 것을 금지합니다.

민석이는 1번 양부터 순서대로 세는 것이 재미없을 것 같아서 
N의 배수 번호인 양을 세기로 하였다.
즉, 
첫 번째에는 N번 양을 세고, 두 번째에는 2N번 양, … , k번째에는 kN번 양을 센다.

이렇게 숫자를 세던 민석이에게 잠은 더 오지 않고 다음과 같은 궁금증이 생겼다.
이전에 셌던 번호들의 각 자리수에서 
0에서 9까지의 모든 숫자를 보는 것은 최소 몇 번 양을 센 시점일까?

예를 들어 N = 1295이라고 하자.

첫 번째로 N = 1295번 양을 센다. 현재 본 숫자는 1, 2, 5, 9이다.

두 번째로 2N = 2590번 양을 센다. 현재 본 숫자는 0, 2, 5, 9이다.
현재까지 본 숫자는 0, 1, 2, 5, 9이다.

세 번째로 3N = 3885번 양을 센다. 현재 본 숫자는 3, 5, 8이다.
현재까지 본 숫자는 0, 1, 2, 3, 5, 8, 9이다.

네 번째로 4N = 5180번 양을 센다. 현재 본 숫자는 0, 1, 5, 8이다.
현재까지 본 숫자는 0, 1, 2, 3, 5, 8, 9이다.

다섯 번째로 5N = 6475번 양을 센다. 현재 본 숫자는 4, 5, 6, 7이다.
현재까지 본 숫자는 0, 1, 2, 3, 4, 5, 6, 7, 8, 9이다.

5N번 양을 세면 0에서 9까지 모든 숫자를 보게 되므로 
민석이는 양 세기를 멈춘다.

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 N (1 ≤ N ≤ 106)이 주어진다.

[출력]
각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
최소 몇 번 양을 세었을 때 
이전에 봤던 숫자들의 자릿수에서 0에서 9까지의 모든 숫자를 보게 되는지 출력한다.
( 민석이는 xN번 양을 세고 있다. )

입력
5
1           1  2 3 4 5 6 7 8 9 0       10     0-9
2           2 4 6 8 1 0  20 22 24      90     0-9
11          1, 1                       110    0-9
1295        1, 2, 9, 5                 6475   0-9
1692        1, 6, 9, 2                 5076   0-9

list
set 
list

출력
#1 10
#2 90
#3 110
#4 6475
#5 5076
'''

# ( 민석이는 xN번 양을 세고 있다. )


for for_num in range(int(input())):

    N = int(input())
    num_list = []
    set_list = []
    k = 0

    while len(set_list) < 10:
        k += 1
        number = k * N
        str_number = str(number)
        for i in range(len(str_number)):
            num_list.append(str_number[i])
            set_list = set(num_list)

    print(f'#{for_num+1} {k * N}')


for T in range(int(input())):
    N = int(input())
    num_list = []
    set_list = []
    k = 0
    while len(set_list) < 10:
        k += 1
        number = k * N
        str_number = str(number)
        for i in range(len(str_number)):
            num_list.append(str_number[i])
            set_list = set(num_list)
    print(f'#{T+1} {k * N}')  # k이 돈 횟수 만큼 N을 곱하기


for T in range(int(input())):  # test case는 5번이다.
    N=int(input())
    k=1
    x=set(str(N))
    while(len(x)<10):
        k+=1
        x.update(str(k*N))
    print(f'#{T+1} {k*N}')


## x의 len이 10을 초과하기전까지 계속 반복하여 돌고, 반복하면서 축적된 k에 N을 곱한다.
## x는 set이므로, 중복이 없고+원소가 다 나눠진다.
for T in range(int(input())):
    N, k = int(input()), 1
    x = set(str(N))
    while len(x) < 10:
        k += 1
        x.update(str(k*N))
    print(f'#{T+1} {k*N}')

    

for T in range(int(input())):
    N = int(input()) # 2
    k = 1
    x = set(str(N)) # {'2', '4', '6'}
    while len(x) < 10: # 3
        k = K + 1 # 4
        x.update(str(k*N)) # 8
    print(f'#{T+1} {k*N}')