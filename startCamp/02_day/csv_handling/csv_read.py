# 1. .split(기준문자) 
with open('dinner.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines() #list의 형태로 저장되므로 가장 적합
    # print(lines)
    for line in lines:
        print(line.strip().split(',')) # , 기준으로 문자열을 split 한다. -> list 형식


# 2. csv reader
import csv

with open('dinner.csv', 'r', encoding='utf-8') as f:
    csv_reader = csv.reader(f)
    items = csv_reader
    print(items)
    for item in items:  # for문을 돌려서 확인 가능
        print(item)