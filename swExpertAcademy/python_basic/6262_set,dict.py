"""
다음의 결과와 같이 입력된 문자열의 문자 빈도수를 구하는 프로그램을 작성하십시오.

입력
abcdefgabc

출력
a,2

b,2

c,2

d,1

e,1

f,1

g,1
"""

## dict 외우기


a = 'abcdefgabc'
a = list(a)
print(a)

alphabet_count={}
for alphabet in a:
    if alphabet in alphabet_count:
        alphabet_count[alphabet] += 1
    else:
        alphabet_count[alphabet] = 1

print(alphabet_count)

print(alphabet_count['a'])

print(alphabet_count.keys())
print(alphabet_count.values())

# key와 value를 한꺼번에 for문을 반복하려면 items() 를 사용합니다.
for key, val in alphabet_count.items():
    print('{},{}'.format(key,val))

""" 실수
for alphabet_one in alphabet_count.keys():
    print(alphabet_one)
    for alphabet_num in alphabet_count.values():
        if alphabet_one == alphabet_one:
            print(alphabet_num)
            print(alphabet_one,",",alphabet_num)
"""