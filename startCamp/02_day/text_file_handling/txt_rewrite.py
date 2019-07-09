# ssafy.txt 파일 읽고
# 역순으로 reversed_ssafy.txt 파일로 저장
with open('ssafy.txt', 'w', encoding = 'utf-8') as f:
    f.writelines(['0\n', '1\n', '2\n', '3\n'])

with open('ssafy.txt', 'r') as f:
    lines = f.readlines() # List 형식으로 각 라인을 item 삼아서 반환한다.
    # print(lines)


#reverse()함수로 list내의 원소를 역순으로 만든다.
lines.reverse()
print(lines)

with open('reversed_ssafy.txt', 'w') as f:
    for line in lines:
        f.write(line)
    