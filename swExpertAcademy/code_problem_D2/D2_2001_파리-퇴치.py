'''
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3

5*5 의 배열
2*2 의 파리채

'''

그리면서

def kill_max_flies(n, m):
    board = []
    temp_board = []
    index_num = []
    a = (n-1)*(n-1)
    x = 0

    
    for ni in range(n):
        index_num.append(ni)        
        board.append(input().split())
    # print(board)
    # print(index_num)
    # print(board[0][0:2])
        if x < n:
            for ni_i in range(n-2):
                print('f', board[x][x:x+2])
                temp_max = sum(map(int, board[x][x:x+2])) + sum(map(int, board[x+1][x:x+2]))
                temp_board.append(temp_max)
                x = x + 1        
            print('total_sum', temp_board)
            
        
            
            

kill_max_flies(5, 2)