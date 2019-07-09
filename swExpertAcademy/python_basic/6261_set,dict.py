"""
다음과 같은 기존의 맥주 가격을 5% 인상하려고 할 경우,
딕셔너리 내포 기능을 이용한 코드를 작성하십시오.
## 딕셔너리 내포: dictionary comprehension
for i, v in enumerate(list):
    print(i,v)

## zip 


percent 증가율
 # 인상 전
beer = {'하이트': 2000, 
'카스': 2100, 
'칭따오': 2500, 
'하이네켄': 4000, 
'버드와이저': 500}

"""

"""
# output
{'하이트': 2000, 
'카스': 2100, 
'칭따오': 2500, 
'하이네켄': 4000, 
'버드와이저': 500}            # 인상 전

{'하이트': 2100.0, 
'카스': 2205.0, 
'칭따오': 2625.0, 
'하이네켄': 4200.0,
 '버드와이저': 525.0}  # 인상 후

 """

beer_before = {'하이트': 2000, '카스': 2100, '칭따오': 2500, '하이네켄': 4000, '버드와이저': 500}   
# print(list(beer_before))

new_price_list = []
new_beer_list =[]

for i in beer_before.values():
    new_price = i+i*0.05
    new_price_list.append(new_price)
# print(new_price_list)

for n in beer_before.keys():
    new_beer_list.append(n)
# print(new_beer_list)

new_dict = {}

for new_beer_list, new_price_list in zip(new_beer_list, new_price_list):
    # print(new_beer_list, new_price_list)
    # new_dict = {new_beer_list : new_price_list}
    # print(new_dict)
    new_dict.update({new_beer_list:new_price_list})

print(beer_before)
print(new_dict)
 
