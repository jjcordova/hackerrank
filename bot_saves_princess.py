# Excersice HackerRank
# Artificial Intelligence  Bot Building  Bot saves princess
# https://www.hackerrank.com/challenges/saveprincess


#!/usr/bin/python

def displayPathtoPrincess(n,grid):
#print all the moves here
    for i in range(n):
        for j in range(n):
            if grid[i][j] == "m":
                bot_position = (i, j)
            elif grid[i][j] == "p":
                princess_position = (i, j)
    
    # Encuentra la diferencia entre las posiciones del bot y de la princesa
    x_diff = princess_position[0] - bot_position[0]
    y_diff = princess_position[1] - bot_position[1]
    
    # Mueve al bot hacia la princesa
    if x_diff > 0:
        print("DOWN\n" * x_diff, end="")
    elif x_diff < 0:
        print("UP\n" * abs(x_diff), end="")
    if y_diff > 0:
        print("RIGHT\n" * y_diff, end="")
    elif y_diff < 0:
        print("LEFT\n" * abs(y_diff), end="")
        
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)