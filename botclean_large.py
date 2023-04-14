# Excersice HackerRank
# Artificial Intelligence  Bot Building  Bot Clean Large
# https://www.hackerrank.com/challenges/botcleanlarge/problem
# Bot Clean Large

#!/bin/python3

import math
dirty_position = []
# get_dirty_position 
def get_dirty_position(dimr, dimc, board):
  n=len(board)
  for i in range(dimr):
        for j in range(dimc):
            if board[i][j] == "d":
                dirty_position.append([i, j])

# get the dirty 
def get_dirty_nearest(posr, posc, dimr, dimc, dirty_position):
  dirty_nearest = []
  result =  math.sqrt((dimr)**2+(dimc)**2)
  if len(dirty_position)>0:
    for i in range(len(dirty_position)):
      result_0 = math.sqrt(((dirty_position[i][0] - posr) ** 2) + ((dirty_position[i][1] - posc) ** 2))
      if result_0 <= result:
        result = result_0
        dirty_nearest = dirty_position[i]
        #print(f'Bot: {[posr, posc]}, Dirty:{dirty_nearest}, Distance:{result}')
  return(dirty_nearest)


# posr (x), posc (y), board (5*5 grid)
def next_move(posr, posc, dimr, dimc, board):
  get_dirty_position(dimr, dimc, board)
  dirty_nearest=get_dirty_nearest(posr, posc, dimr, dimc, dirty_position)
  # Encuentra la diferencia entre las posiciones del bot y de la princesa
  x_diff = dirty_nearest[0] - posr
  y_diff = dirty_nearest[1] - posc
  
  # Mueve al bot hacia la princesa
  if x_diff > 0:
      print("DOWN\n", end="")
      return
  elif x_diff < 0:
      print("UP\n" , end="")
      return
  if y_diff > 0:
      print("RIGHT\n", end="")
      return
  elif y_diff < 0:
      print("LEFT\n", end="")
      return
  else:
        print('CLEAN')

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)