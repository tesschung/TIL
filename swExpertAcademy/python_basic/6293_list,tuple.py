"""
6293. [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 2. 자료구조 -리스트, 튜플 17
다음의 결과와 같이 사용자로부터 콤마(,)로 구분해 여러 원의 반지름을 입력 받아
이들에 대한 원의 둘레를 계산해 출력하는 프로그램을 작성하십시오

입력
2, 3, 4, 5

출력
12.57, 18.85, 25.13, 31.42

원둘레구하는공식
원의반지름x2x3.14(원주율)
지름 x 파이 = 원둘레
"""

a = 2, 3, 4, 5

d = []
for i in a:
    circle = i*2*3.141592653589793238462643383279502884197169399375
    d.append(circle)
    # ",".join(d)
    print(f'{circle:.2f}', end=', ')