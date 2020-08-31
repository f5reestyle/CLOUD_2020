import numpy as np
from methods import win, check, isEND, Play, Show

while True :
    shape = input('Please enter the length(n) of one side of the board(n*n). : ')
    shape = int(shape)
    if shape >= 5:
        break
    else:
        print('"n" must be greater than or equal to 5. ')           

grid = np.zeros((shape,shape))          # n*n omok-board. initializing them to 0.

# Game starts.
    
Show(grid) 

while True:
    
    Play(1)                 
    Show(grid)   
    if isEND() == 0:       
        break
    
    Play(2)                                                     
    if isEND() == 0:
        break