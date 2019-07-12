"""
2072. 홀수만 더하기
10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.

[제약 사항]
각 수는 0 이상 10000 이하의 정수이다.

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.

[출력]
출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.) 

입력
3
3 17 1 39 8 41 2 32 99 2
22 8 5 123 7 2 63 7 3 46
6 63 2 3 58 76 21 33 8 1   

출력
#1 200
#2 208
#3 121
"""
"""
a = int(input())

for i in range(1, a+1): #1, 2, 3  3번
    sum_ = 0
    num_list = str(input()).split()
    for d in num_list:
        d = int(d) # 여기까지 홀수 출력됨
        #print(d)
        if d%2 == 1:
            sum_ += d
    print(f'#{i} {sum_}') 
"""


"""제출"""

"""

a = int(input())
for i in range(1, a+1): 
    s = 0
    l = str(input()).split()
    for d in l:
        d = int(d)
        if d%2 == 1:
            s += d
    print(f'#{i} {s}')

"""

a = int(input())
for i in range(1, a+1): 
    s = 0
    l = str(input()).split()
    l = map(int, l)
    for d in l:
        if d%2 == 1:
            s += d
    print(f'#{i} {s}')
