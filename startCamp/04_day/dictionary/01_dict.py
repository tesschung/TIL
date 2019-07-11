"""
Dictionary 만들기
"""
#1. 
lunch1 = {
    '중국집' : '02',
}
print(lunch1)

#2.
lunch2 = dict(중국집='02')
print(lunch2)

"""
dict 내용 추가
"""
# 키값으로 접근
lunch1['중국집'] # 02
lunch1['분식집'] = '031' # 새로운 키를 생성하고, 그 키값 또한 생성
print(lunch1['분식집'])

"""
dict 내용 가져오기
"""
idol = {
    'bts' : { 
        '지민' : 24,
        'RM' : 25
    }
}
# 랩몬스터의 나이는?
print(idol['bts']['RM'])

print('-'*10)

"""
dict 반복문 활용하기
기본 활용
"""
for key in lunch1:
    print('key:', key, 
    'value:', lunch1[key])

"""
value만 가져오기
"""
for value in lunch1.values():
    print(value)

"""
key만 가져오기
"""
for key in lunch1.keys():
    print(key)


"""
.items()로 key, value 가져오기
"""
for key, value in lunch1.items():
    print(lunch1.items())
    print(key, value)

# 활용: tuple형태로 key와 value가 쌍으로 순회함
for key in lunch1.items():
    print(key, type(key))
