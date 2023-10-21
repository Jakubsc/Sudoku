import pygame
import time
from math import floor

def solve(board):
    position=find_empty(board)
    if position:
        y, x=position
    else:
        return True
    
    for i in range(9):
        if valid(board,i+1,x,y):
            board[y][x]=i+1
            if(solve(board)):
                return True
            board[y][x]=0
    return False
def solve_and_show(screen,board):
  
  position=find_empty(board)
  if position:
      y, x=position
  else:
      return True
  
  for i in range(9):#trying all numbers in one spot
      if valid(board,i+1,x,y):
          board[y][x]=i+1
          display=myFont.render(str(board[y][x]),1,white)
          draw(screen,x,y,green)
          if x%3:
            screen.blit(display,(x*52+(x//3-1)*2+17,y*52+(y//3-1)*2+8))#displaying number
          else:
            screen.blit(display,(x*52+(x//3)*2+17,y*52+(y//3)*2+8))
          pygame.time.delay(100)
          pygame.display.flip()
          if(solve_and_show(screen,board)):
              return True
          board[y][x]=0
          pygame.draw.rect(screen, (0,0,0), (x*52+(x//3)*2+2,y*52+(y//3)*2+2, 49, 49)) 
          draw(screen,x,y,red)
  return False
    
def valid(board, num, x,y):

    for i in range(9):
        if((board[y][i]==num) or (board[i][x]==num)): #checks if there is a same value in same row or column
            return False
    x=floor(x/3)
    y=floor(y/3)
    for i in range(y*3,y*3+3): #checks if in 3x3 square is already that number
        for j in range(x*3,x*3+3):
            if(board[i][j]==num):
                return False
    return True   
def find_empty(bo):
    for i in range(9):
        for j in range(9):
            if bo[i][j]==0:
                return(i,j)
    return None
  
def draw(screen,x,y,colour): #drawing square
  pygame.draw.line(screen, colour, (x*52+(x//3)*2,y*52+(y//3)*2), ((x+1)*52+(x//3)*2, y*52+(y//3)*2),2) #upper line
  pygame.draw.line(screen, colour, (x*52+(x//3)*2,y*52+(y//3)*2), (x*52+(x//3)*2, (y+1)*52+(y//3)*2),2) #left line
  pygame.draw.line(screen, colour, ((x+1)*52+(x//3)*2, (y+1)*52+(y//3)*2), ((x+1)*52+(x//3)*2, y*52+(y//3)*2),2)#right line
  pygame.draw.line(screen, colour, ((x+1)*52+(x//3)*2, (y+1)*52+(y//3)*2), (x*52+(x//3)*2, (y+1)*52+(y//3)*2),2)#lower line
  pygame.display.flip()



board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
users_board=[
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
solve(board)#this we will use as tool to compare when user put number in a marked square
pygame.init()
background_colour = (0,0,0)#black
white=(255,255,255)
green=(0,255,0)
red=(255,0,0)
(width, height) = (476, 500)

myFont = pygame.font.SysFont("Times New Roman", 40)
screen = pygame.display.set_mode((width, height))
screen.fill(background_colour)

for i in range(0,10): #drawing lines
    if i%3==0 and i!=0:
      pygame.draw.line(screen, white, (i*52+(i//3)*2-1,0), (i*52+(i//3)*2-1, 474),4)
      pygame.draw.line(screen, white, (0, i*52+(i//3)*2-1), (474, i*52+(i//3)*2-1),4)
      print(i*52+(i//3)*2-2)
    else:
       pygame.draw.line(screen, white, (i*52+(i//3)*2,0), (i*52+(i//3)*2, 474),2)
       pygame.draw.line(screen, white, (0, i*52+(i//3)*2), (474, i*52+(i//3)*2),2)

       
      
for y in range(0,9): #drawing numbers
   for x in range(0,9):
        if(users_board[y][x]!=0):
            display=myFont.render(str(users_board[y][x]),1,white)
            if y%3 and y !=0:
              screen.blit(display,(x*52+(x//3-1)*2+17,y*52+(y//3-1)*2+8))
            else:
              screen.blit(display,(x*52+(x//3)*2+17,y*52+(y//3)*2+8))
pygame.display.set_caption('Sudoku')
pygame.display.flip()
running = True
marked=False
x_prev=-1
y_prev=-1
key=None
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_KP1 or event.key == pygame.K_1:
          key = 1
      if event.key == pygame.K_KP2 or event.key == pygame.K_2:
          key = 2
      if event.key == pygame.K_KP3 or event.key == pygame.K_3:
          key = 3
      if event.key == pygame.K_KP4 or event.key == pygame.K_4:
          key = 4
      if event.key == pygame.K_KP5 or event.key == pygame.K_5:
          key = 5
      if event.key == pygame.K_KP6 or event.key == pygame.K_6:
          key = 6
      if event.key == pygame.K_KP7 or event.key == pygame.K_7:
          key = 7
      if event.key == pygame.K_KP8 or event.key == pygame.K_8:
          key = 8
      if event.key == pygame.K_KP9 or event.key == pygame.K_9:
          key = 9
      if event.key == pygame.K_SPACE:
        if marked:
          draw(screen,x,y,white)
        solve_and_show(screen,users_board)
      if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN or key!=None:
        if marked:
          display=myFont.render(str(key),1,white)
          if(users_board[y][x]==0):
            if(key==board[y][x]):
              users_board[y][x]=key
              print("*******")
              print("Succes!")
              print("*******")
              if x_prev%3 and x_prev !=0: #drawing succesful number
                screen.blit(display,(x_prev*52+(x_prev//3-1)*2+17,y_prev*52+(y_prev//3-1)*2+8))
              else:
                screen.blit(display,(x_prev*52+(x_prev//3)*2+17,y_prev*52+(y_prev//3)*2+8))
              pygame.display.flip()
            else:
               print("------")
               print("Wrong!")
               print("------")
          else:
             print("mark empty square")  

    elif event.type == pygame.MOUSEBUTTONUP:
      pos = pygame.mouse.get_pos()
      print("-----------")
      print(pos[0],pos[1])

      x_rem=0
      y_rem=0
      if(pos[0]>156):
        if(pos[0]>316):
          x_rem+=2
        x_rem+=2
      x=(pos[0]-x_rem)//52
      if(pos[1]>156):
        if(pos[1]>316):
          y_rem+=2
        y_rem+=2
      y=(pos[1]-y_rem)//52
      
      print("x=",x, "y=",y)
      print("-----------")
      if marked:
        draw(screen,x_prev,y_prev,white)
      draw(screen,x,y,green)
      marked=True
      x_prev=x
      y_prev=y
      

