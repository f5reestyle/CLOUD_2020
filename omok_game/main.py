import numpy as np
from methods import isEND, Play, Show

while True :
    shape = input('Please enter the length(n) of one side of the board(n*n). : ')
    shape = int(shape)
    if shape >= 5:
        break
    else:
        print('"n" must be greater than or equal to 5. ')   

# n*n omok-board. initializing them to 0.
grid = np.zeros((shape,shape))         

# Game starts.
    
Show(grid) 

while True:    # play the game until someone wins.
    
    Play(1)        # player 1 plays      
    Show(grid)     
    if isEND() == 0:      
        break
    
    Play(2)        # player 2 plays                                                
    if isEND() == 0:
        break