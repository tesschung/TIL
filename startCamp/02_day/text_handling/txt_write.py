"""
1. open a specific file
"""
# 열기모드
# r: 읽기, w: 쓰기(write - overwrite), a: 추가(append)
f = open('ssafy.txt', 'w')

"""
2. write
"""
for i in range(10): # i 0~9
    f.write(f'this is line {i+1} \n')

"""
3. 반드시 close
"""
f.close()


"""
1-3. with문으로 write
"""
# with -> context manager 
# close가 자동적으로 실행됨
with open('with_ssafy.txt','w') as f:
    for i in range(10):
        f.write(f'this is line {i+1} \n')

"""
1-3. with문으로 특정 줄을 리스트로 받아서 write
"""
# utf-8 encoding으로 열겠다는 것
with open('ssafy.txt', 'w', encoding = 'utf-8') as f:
    f.writelines(['0\n', '1\n', '2\n', '3\n'])
