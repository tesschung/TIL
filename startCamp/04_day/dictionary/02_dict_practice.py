"""
Python dictionary 연습 문제
"""

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')

sum_ = 0 
for value in score.values():
    sum_ += value
    
print(sum_/3)


# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')
sum1 = 0
for value1 in scores['a'].values():
    sum1 += value1

print(sum1/3)

sum2 = 0
for value2 in scores['b'].values():
    sum2 += value2

print(sum2/3)

value3 = sum1+sum2
print(value3/6)

# print(scores['a']['수학'], scores['b']['수학'])


# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""

"""
print(list(city))


for key in city.keys():
    print(key)

for value in city.values():
    print(value)
    
    for one in value:
        one += one
    
    avg_temp = one/3
    print(avg_temp)

new_dict = {}
new_dict[key] = avg_temp
print(new_dict)
"""

new_dict = {}
sum_temp = 0 
for key, value in city.items():
    for one in value:
        sum_temp += one
    
    avg_temp = sum_temp/3
    print(avg_temp)

    
    new_dict[key] = avg_temp
print(new_dict)

"""
print(new_dict)
for key, value in new_dict.items():
    print(value)
"""

# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')

city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

list_ = []
list_2 = []

for value in city.values():
    print(value)
    for value_num in value:
        print(value_num)
        list_.append(value_num)
    print(list_)
    print(min(list_))
    #for i in range(len(list_)):
        #if list_[i] < list_[i+1]:
        #    list_2.append(list_[i])
        #print(list_2)
        # -10까지 찾음, 여기서 range처리필요 그리고 각 dict에 있는지 확인하여 결과 출력


# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')


city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

a = city['서울']
print(a)

for i in a:
    if i != 2:
        print("아니요")
    else:
        print("네")

#for key, value in city.items():
#    print(city['서울'])




sum([1,3,4]) #8
len([1,3,4]) #3
max([1,3,4]) #4
min([1,3,4]) #1