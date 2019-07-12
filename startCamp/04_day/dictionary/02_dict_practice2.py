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

"""
값이 필요해서 접근 해야함
"""

total_score = 0
# print(score.values())

for value in score.values():
    total_score += value

print(total_score/len(score.keys()))

total_score_sum = sum(score.values())
print(total_score/len(score))

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

total_score_ = 0
count = 0

for person_score in scores.values():
    print(person_score.values()) 
    # dict_values([80, 90, 100])
    # dict_values([80, 90, 100])
    total_score_ += sum(person_score.values())
    count += len(person_score) # 6

#print(count)
avg_score_ = 0
avg_score_ = total_score_/count
print(avg_score_)

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
for key, value in city.items():
    average_temp = sum(value) / len(value)
    #print(average_temp)
    #print(key, value) 
    print(f'{key} : {average_temp:.2f}') #.2f로 round


# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
count = 0
for name, temp in city.items():
    #print(name, temp)
    # 첫 번째 시행 때
    # 단 한번만 실행되는 조건이 필요해서 count 변수 사용
    if count == 0:
        hot_temp = max(temp) # count가 0일때/첫번째 키인 서울 5
        cold_temp = min(temp) # count가 0일때/첫번째 키인 서울 -10
        hot_city = name
        cold_city = name
        # 서울을 한 번 돌고, 그 다음 키로 돈다 -> count는 더이상 0이 아니므로
    else:
        # 최저 온도가 cold_temp 보다 낮으면, cold_temp 에 값을 새로 넣고,
        if min(temp) < cold_temp:
            cold_temp = min(temp)
            cold_city = name
        # 최고 온도가 hot_temp 보다 높으면, hot_temp 에 값을 새로 넣는다.
        if max(temp) > hot_temp:
            hot_temp = max(temp)
            hot_city = name
    count += 1

print(f'최고로 더웠던 지역은 {hot_city} {hot_temp} 였고, 최고로 추웠던 지역은 {cold_city} {cold_temp} 였다.')


# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?
if 2 in city['서울']:
    print('네 있어요')
else:
    print('아니요 없어요')