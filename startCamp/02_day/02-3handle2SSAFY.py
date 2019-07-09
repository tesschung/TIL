"""
SUMSUNG 자리에 SSAFY 넣기
"""

"""
1. os를 import한다.
"""
import os

"""
2. 해당 폴더로 들어간다.
"""
# 500개의 지원서가 있는 파일로 이동
path = os.chdir(r'C:\Users\student\TIL\startCamp\02_day\file_handling')

# 특정 경로의 모든 파일의 이름을 가지고옴
filenames = os.listdir(path)
print(filenames)

"""
3. for문을 돌면서 변경한다.
"""
#.txt로 끝나는 파일의 이름만 변경
for filename in filenames:
    # 확장자가 .txt인 파일만 이름을 바꾼다.
    splited = os.path.splitext(filename)[1] # 확장자만 따로 분리
    print(splited)

    if splited == '.txt':
        print("SSAFY 로 변경한다.", filename)
        os.rename(filename, filename.replace('SAMSUNG_', 'SSAFY_')) # 첫번째 인자로 넘어간 이름을, 두번째 인자로 넘어간 이름으로 바꾼다.
        