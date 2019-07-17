'''
숫자 N은 아래와 같다.
N=2a x 3b x 5c x 7d x 11e
N이 주어질 때 a, b, c, d, e 를 출력하라.


[제약 사항]
N은 2 이상 10,000,000 이하이다.


[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 N 이 주어진다.


[출력]
출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
 
입력
10  
6791400
1646400
1425600
8575
185625
6480
1185408
6561
25
330750

출력
#1 3 2 2 3 1
#2 6 1 2 3 0
#3 6 4 2 0 1
#4 0 0 2 3 0
#5 0 3 4 0 1
#6 4 4 1 0 0
#7 7 3 0 3 0
#8 0 8 0 0 0
#9 0 0 2 0 0
#10 1 3 3 2 0
 
 
'''

for T in range(int(input())):
    # 어떤 정수를 소수로만 곱하여 표현하는 것을 소인수분해라고 한다
    c = []
    x = int(input())
    d = 2 ## 가장 작은 소수인 2부터 나눕니다.
    while d <= x:
        if x % d == 0: # x가 d로 나누어지면(나머지가 0이면)
            # print(d)
            c.append(d)
            # d는 x의 약수이므로 출력한다.
            # 약수란 어떤 수를 나누어 떨어지게 하는 0이 아닌 정수를 의미합니다. 예를 들어 1은 모든 수의 약수이죠.
            x = x / d # x를 d로 나눠서 다시 x에 저장합니다.
        else:
            d = d + 1 # 나누어지지 않으면 1을 더해서 반복합니다.
            
    print(f'#{T+1} {c.count(2)} {c.count(3)} {c.count(5)} {c.count(7)} {c.count(11)}')



for T in range(int(input())):
    c = []
    x = int(input())
    d = 2
    while d <= x:
        if x % d == 0:
            c.append(d)
            x = x / d
        else:
            d = d + 1          
    print(f'#{T+1} {c.count(2)} {c.count(3)} {c.count(5)} {c.count(7)} {c.count(11)}')



#박권응님
test_num = int(input())
for i in range(test_num):
    test_case = int(input())
    a, b, c, d, e= (0, 0, 0, 0, 0)

    while test_case > 2 :
        if test_case % 2 == 0 :
            a += 1
            test_case = round(test_case / 2)
        elif test_case % 3 == 0 :
            b += 1
            test_case = round(test_case / 3)
        elif test_case % 5 == 0:
            c += 1
            test_case = round(test_case / 5)
        elif test_case % 7 == 0 :
            d += 1
            test_case = round(test_case / 7)
        elif test_case % 11 == 0 :
            e += 1
            test_case = round(test_case / 11)
        else : 
            print("이상")
            test_case = 0
    print(f'#{i+1} {a} {b} {c} {d} {e}')


#김은성님
T = int(input())

for i in range(T):
    # 기본설정
    num = int(input())
    dem = [2, 3, 5, 7, 11]
    dem_in = [0, 0, 0, 0, 0]
    
    #소인수분해하기
    for de in range(len(dem)): #각각의 소수에 대하여
        while num % (dem[de]**(dem_in[de]+1)) == 0: #승수를 높혀가며 나눠보기
            dem_in[de] += 1


    print(f'#{i+1} ', end = '')
    for k in range(len(dem)):
        print(f'{dem_in[k]}', end=' ')
    print('')