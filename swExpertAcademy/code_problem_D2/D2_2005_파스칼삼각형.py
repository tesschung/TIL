'''
>>> a = [1, 2, 3]
>>> a[len(a):] = [10]
>>> a
[1, 2, 3, 10]
'''

temp_list_b = []

for T in range(1):
    pass

    for t in range(1, 4):
        

        if t == 1:
            print(1) # 1이 나옴
        elif t == 2:
            for i in range(2):
                temp_list_b.append(1)
            #print(temp_list_b) # [1, 1]이 나옴
        
        else:
            for t_three in range(1, t-1): # 1부터 3-1 -> 2까지 
                #print(temp_list_b[t-1])    
                a = temp_list_b[t-1] + temp_list_b[t]
                # print(a) #3이 나왔을때 1과 2 index에 넣어줘야 한다.
                temp_list_b.insert(t, a)
                print('sum1', t)


                print(temp_list_b)

    
    # 리스트 중간에 요소 여러 개를 추가
    #temp_list_b[1:1] = a

    #temp_list_b.insert(0, 1)
    #temp_list_b.insert(-1, 1)

#print(temp_list_b)
    #temp_list_b.clear()

'''

'''
>>> a = [1, 2, 3]
>>> a[len(a):] = [10]
>>> a
[1, 2, 3, 10]
'''

temp_list_b = []

for T in range(1):
    pass

    for t in range(1, 5):
        

        if t == 1:
            print(1) # 1이 나옴
        elif t == 2:
            for i in range(2):
                temp_list_b.append(1)
            print(temp_list_b) # [1, 1]이 나옴

        else: 
            temp_list_a = [1]

            for d in range(1, t-1):
                print('--------')
                
                a = temp_list_b[d-1] + temp_list_b[d]
                print('a1', a) #3이 나왔을때 1과 2 index에 넣어줘야 한다.
                
                temp_list_a.append(a)
                print(temp_list_a)
                #temp_list_b.insert(t, a)
                
                print(temp_list_b)

            #temp_list_a    


'''