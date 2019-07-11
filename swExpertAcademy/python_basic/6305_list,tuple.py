"""
6305. [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 2. 자료구조 -리스트, 튜플 27 
리스트의 항목 중 중복이 되는 항목을 제거하는 함수를 정의하고 이 함수를 이용해

[12,24,35,24,88,120,155,88,120,155]에서 중복이 제거된 리스트를 출력하십시오.

출력
[12, 24, 35, 88, 120, 155]
"""

""" 결과 값이 상이하다.
list_same = [12,24,35,24,88,120,155,88,120,155]
set_same = set(list_same)
print(set_same)
"""



def same_remove(list_same):
    list_new = [] # 임시리스트를 만들고,

    for a in list_same: # 원본리스트의 각 원소를 순회하여 원소를 추출한다.
        if list_new.count(a) < 1: # .count(a)로 임시리스트에 들어있는 원래 리스트의 개수를 구한다.
            # 만약 임시리스트에 원소가 1미만으로 들어있지 않다면, 하기의 추가 작업을 반복
            list_new.append(a) # 중복을 제거한 리스트를 담는다 
            """
            처음에는 빈리스트 이므로 쭉쭉 들어가다가, 나중에 중복을 발견하면 1이상이 되므로 하기 작업을 반복하지 않는다.
            """ 
    print(list_new)
    
list_same = [12,24,35,24,88,120,155,88,120,155]
same_remove(list_same)


"""
    for i in range(len(list_same)):
        for x in range(1 ,len(list_same)):
            if list_same[i] == list_same[x]:
                list_new.append(a[i])
"""