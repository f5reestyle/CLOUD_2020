import numpy as np
import matplotlib.pyplot as plt
from main import shape, grid

# Print that player n wins
def win(n):
    print('{}player wins'.format(n))         
    return 0

# Check who wins
def check(a):
    if np.all(a == 1):
        return win(1)
    elif np.all(a==2):
        return win(2)
    

# check whether the game ends
def isEND():
    
    # Check horizontal lines.
    for i in range(shape):
        for j in range(shape-4):
            if check(grid[i,j:j+5]) == 0:
                return 0          
                
    # Check vertical lines.
    for i in range(shape):
        for j in range(shape-4):
            if check(grid[j:j+5,i]) == 0:
                return 0
            
        
    # Check diagonal lines.

    #  ↘ directions
    for i in range(shape-4):
        for j in range(shape-4):
            a= np.array([grid[i+k][j+k] for k in range(5)])     
            if check(a) == 0:
                return 0
    # ↗ directions
    for i in range(shape-4):
        for j in range(shape-4):
            a= np.array([grid[shape-1-j-k][i+k] for k in range(5)])
            if check(a) == 0:
                return 0

# Check whether there already exists a stone
def Play(player):
    while True:
        _input= input(f'Please enter the {player}player\'s stone position(x y). Numbers from 1 to {shape} are allowed  : ')
        try:
            n,m =list(map(int,_input.split()))
            if grid[n-1,m-1] == 0:
                grid[n-1,m-1] = player
                break
            print('There already exists a stone.')
        except:
            print('Please enter something like 1 5 or 2 2')
            
# Show the process of a game graphically 
def Show(grid):
    plt.title('omok-pan')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(0, shape+1,1)
    plt.ylim(0, shape+1,1)
    plt.xticks(np.arange(1, shape+1, step=1))
    plt.yticks(np.arange(1, shape+1, step=1))
    
    # player 1 plays with black stones. player 2 with white ones.
    b_x = [i+1 for i in np.where(grid==1)[0]]
    b_y = [i+1 for i in np.where(grid==1)[1]]
    w_x = [i+1 for i in np.where(grid==2)[0]]
    w_y = [i+1 for i in np.where(grid==2)[1]]
          
    plt.plot(b_x,b_y, linestyle='None', markersize= 20, markerfacecolor= 'black', marker = 'o')
    plt.plot(w_x,w_y, linestyle='None', markersize= 20, markerfacecolor= 'white', marker = 'o')
    
    
    plt.grid(color='grey',linewidth=0.7)
    plt.show()
