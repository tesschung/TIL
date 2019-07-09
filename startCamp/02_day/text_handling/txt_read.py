"""
1.
"""
f = open('ssafy.txt', 'r')
"""
2.
"""
all_text = f.read() # all text read(\n문자 포함)
print(all_text)
"""
3.

"""
f.close()


"""
1-3.
"""
with open('with_ssafy.txt', 'r') as f:
    with_all_text = f.read()
    print(with_all_text)


# 전체를 읽고, list로 불러온다.
with open('with_ssafy.txt', 'r') as f:
    with_text_lines = f.readlines()
    print(with_text_lines)

    # print by lines
    # .strip()으로 \n 제거
    # print() 자체에 \n 존재
    for line in with_text_lines:
        print(line.strip())
