"""
1. dictionary 생성
"""
dinner = {
    '양자강':'02-57-4211',
    '김밥카페':'02-553-3181',
    '순남시래기':'02-508-0887'
}

print('key:value', dinner.items())
print('key', dinner.keys())
print('value', dinner.values())


"""
2. open
3. for문 돌리기, .items() 사용
"""
# 1. string formatting
with open('dinner.csv', 'w', encoding='utf-8') as f:
    for item in dinner.items(): # dict -> list [['양자강', '02-557-4221'], ['김밥카페', ''02-553-3181'], ['순남시래기','02-508-0887']]
        f.write(f'{item[0]},{item[1]} \n')


# 2. csv writer
import csv
with open('dinner.csv', 'w', encoding='utf-8', newline='') as f: #\n방지를 위한 newline='', **option으로 작성시 띄어쓰기 없음**
    csv_writer = csv.writer(f) #f라는 파일에 csv를 작성하는 객체를 생성
    for item in dinner.items(): # dict -> list [['양자강', '02-557-4221'], ['김밥카페', ''02-553-3181'], ['순남시래기','02-508-0887']]
        csv_writer.writerow(item)
