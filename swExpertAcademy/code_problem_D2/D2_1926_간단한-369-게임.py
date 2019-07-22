b = '-'
for T in range(1, int(input())+1):
    count = 0
    T = str(T)
    for t in T:
        if '3' in t or '6' in t or '9' in t:
            count += 1
            T = count*b
    else:
        T
    print(T, end=' ')