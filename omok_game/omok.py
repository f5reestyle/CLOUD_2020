import numpy as np

while True :
    shape = int(input('The length(n) of the grid : '))
    if shape >= 5:
        break
    else :
        print('n >=5, please')

grid = np.zeros((shape,shape))

def check():

    for i in range(shape):
        for j in range(shape-4):
            if np.all(grid[i,j:j+5] == 1):
                print('1플레이어가 승리')
                return 1
            elif np.all(grid[i,j:j+5] == -1):
                print('2플레이어가 승리')
                return 1
    for i in range(shape):
        for j in range(shape-4):
            if np.all(grid[j:j+5,i] == 1):
                print('1플레이어가 승리')
                return 1
            elif np.all(grid[i,j:j+5] == -1):
                print('2플레이어가 승리')
                return 1

    for i in range(shape-4):
        a= [grid[i+j][j] for j in range(shape)]
        if a == [1]*shape:
            print('1플레이어가 승리')
            return 1
        elif a == [-1]*shape:
            print('2플레이어가 승리')
            return 1
    for i in range(shape-4):
        a= [grid[j][i+j] for j in range(shape)]
        if a == [1]*shape:
            print('1플레이어가 승리')
            return 1
        elif a == [-1]*shape:
            print('2플레이어가 승리')
            return 1
            
        
while True:
    
    loc1 =list(map(int, input('1플레이어 바둑돌 위치 : ').split()))
    grid[loc1[0]-1,loc1[1]-1] = 1
    if check() == 1:
        break
    loc2= list(map(int, input('2플레이어 바둑돌 위치 : ').split()))
    grid[loc2[0]-1,loc2[1]-1] = -1
    if check() == 1:
        break
    