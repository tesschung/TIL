"""
https://wikidocs.net/79	python wikidocs site
https://docs.python.org/3.7/	python official site
random	https://docs.python.org/3.7/library/random.html
"""

# random.choice(seq)
# Return a random element from the non-empty sequence seq. If seq is empty, raises IndexError.

# random (외장)모듈/라이브러리 import
import random

# menu 리스트를 만들어주세요.
menu = ["김밥", "비빔밥", "잔치국수", "분식"]

# random 라이브러리의 choice(리스트) 함수 사용하여 
# 리스트에서 랜덤한 결과 1개를 뽑아
# choice 변수에 저장
choice = random.choice(menu)

print(choice)



import random 

menu = ["김밥", "비빔밥", "잔치국수", "분식"]

# menu_phonenumber를 만든다
menu_dict = {"김밥": "010-2343", 
             "비빔밥": "010-4535",
             "잔치국수": "010-5453", 
             "분식": "010-4535"}

choice = random.choice(menu)
print(choice, menu_dict[choice])



#random.sample(seq,숫자)
# 1. random 외장 함수 가져오기
import random

# 2. 1~45까지 숫자 numbers에 저장하기
numbers = []
for i in range(46):
  numbers.append(i)
print(numbers)

# 3. numbers에서 6개 뽑기
num = random.sample(numbers,6)

# 4. 출력하기
print(num)

