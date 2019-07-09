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

    