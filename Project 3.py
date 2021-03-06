#https://www.geeksforgeeks.org/tic-tac-toe-gui-in-python-using-pygame/
#https://www.youtube.com/watch?v=pc7XhHxSgrM&ab_channel=CodingSpot
#https://www.youtube.com/watch?v=fT3YWCKvuQE&ab_channel=KylieYing
#https://www.youtube.com/watch?v=trKjYdBASyQ&ab_channel=TheCodingTrain
'''TO DO:
2 player tic tac toe shows a line on 3, currently set to on click which needs to be changed to keys and highlight which cell is being filled.
Display text at the top such as win/loss/draw
add button for refresh at the bottom,
add display for alpha and beta values considered at each step at bottom/top'''
'''imports'''
import pygame,sys
import numpy as np
'''Initializing window'''
pygame.init()
WIDTH = 600
HEIGHT = 600
COLOR=(220,220,220)
BLACK=(0,0,0)
TRANSPARENT=(0,0,0,0)
GREEN=(0,250,0)
CIRCLE=(128,0,128)
CROSS = (0,0,250)
LINE_WIDTH=10
ROWS=3
COLUMNS=3
player=1
max_stats=[0,0,0]
min_stats=[0,0,0]
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("5210 Project 3: Tic Tac Toe")
alpha_beta=[1000,-1000]
util_score={'max':1,'min':-1,'tie':0}
score=0
X,Y=1,1
X1,Y1,X2,Y2,X3,Y3,X4,Y4=258,208,343,208,343,292,258,292
window.fill(COLOR)
game_end=False
game_start=False
#board
'''environment is 2d matrix board'''
board=np.zeros((ROWS,COLUMNS))
#print(board)
def text():
    font = pygame.font.Font('freesansbold.ttf', 20)
    if player==1:
        t = ' Player Max\'s turn '
    elif player==2:
        t = ' Player Min\'s turn '
    text1 = font.render(t, True, BLACK, COLOR)
    text2 = font.render(
        'Player Max Win:{} Loss:{} Draw:{}'.format(max_stats[0], max_stats[1], max_stats[2]), True, BLACK, COLOR)
    text3 = font.render(
        'Player Min Win:{} Loss:{} Draw:{}'.format(min_stats[0], min_stats[1], min_stats[2]), True, BLACK, COLOR)
    text4 = font.render(" Press S to start. Press R to reset. Use arrow keys to move and Enter key to select cell", True, BLACK, COLOR)
    textbox1 = text1.get_rect()
    textbox2 = text2.get_rect()
    textbox3 = text3.get_rect()
    textbox4 = text4.get_rect()
    textbox1.center = (300, 420)
    textbox2.center = (160, 20)
    textbox3.center = (156, 40)
    textbox4.center = (300, 520)
    window.blit(text1, textbox1)
    window.blit(text2, textbox2)
    window.blit(text3, textbox3)
    window.blit(text4, textbox4)
    return
def highlight(x1,y1,x2,y2,x3,y3,x4,y4):
    pygame.draw.line(window, GREEN, (x1, y1), (x2, y2), 5)
    pygame.draw.line(window, GREEN, (x2, y2), (x3, y3), 5)
    pygame.draw.line(window, GREEN, (x3, y3), (x4, y4), 5)
    pygame.draw.line(window, GREEN, (x4, y4), (x1, y1), 5)
    return
def mark(row, col, player):
    board[row][col] = player
#mark(0,0,1)
print(board)

def full():
    for row in range(ROWS):
        for col in range(COLUMNS):
            if board[row][col]==0:
                return False
    return True

def draw():
    for row in range(ROWS):
        for col in range(COLUMNS):
            if board[row][col]==2:
                pygame.draw.circle(window, CIRCLE, (int(col * 100 + 200),(int(row * 100 + 150))), 40, 15)
            if board[row][col]==1:
                pygame.draw.line( window, CROSS, (col * 100 + 240, row * 100 + 120), (col*100+160, row * 100 + 180), 10)
                pygame.draw.line(window, CROSS, (col * 100 + 160, row * 100 + 120), (col*100+240, row * 100 + 180), 10)

#available
def free(row,col):
    return board[row][col]==0

def goal(player):
    #col win
    for col in range(COLUMNS):
        if board[0][col]==player and board[1][col]==player and board[2][col]==player:
            win_line_col(col, player)
            return True
    #row win
    for row in range (ROWS):
        if board[row][0] == player and board[row][1]==player and board[row][2]==player:
            win_line_row(row, player)
            return True
    #diagonal 1
    if board[0][0]==player and board[1][1]==player and board[2][2]==player:
        win_line_d1(player)
        return True
    if board[0][2]==player and board[1][1]==player and board[2][0]==player:
        win_line_d2(player)
        return True
    return False

def win_line_col(col, player) :
    pX = col * 100 + 200
    color=(0,0,0)
    if player==1:
        color = CROSS
    elif player==2:
        color = CIRCLE
    pygame.draw.line(window, color, (pX,110), (pX,390),10)
def win_line_row(row, player) :
    pY = row * 100 + 150
    color = (0, 0, 0)
    if player == 1:
        color = CROSS
    elif player == 2:
        color = CIRCLE
    pygame.draw.line(window, color, (160, pY), (440, pY), 10)
def win_line_d1(player) :
    if player == 1:
        color = CROSS
    elif player == 2:
        color = CIRCLE
    pygame.draw.line(window, color, (170,120), (440,390), 15)


def win_line_d2(player) :
    if player == 1:
        color = CROSS
    elif player == 2:
        color = CIRCLE
    pygame.draw.line(window, color, (420,120), (165,390), 15)
def grid():
    #horizontal
    pygame.draw.line(window, BLACK, (150, 200), (450, 200), LINE_WIDTH)
    pygame.draw.line(window, BLACK, (150, 300), (450, 300), LINE_WIDTH)
    pygame.draw.line(window, BLACK, (146, 100), (455, 100), LINE_WIDTH)
    pygame.draw.line(window, BLACK, (146, 400), (455, 400), LINE_WIDTH)
    #vertical
    pygame.draw.line(window, BLACK, (250, 100), (250, 400), LINE_WIDTH)
    pygame.draw.line(window, BLACK, (350, 100), (350, 400), LINE_WIDTH)
    pygame.draw.line(window, BLACK, (150, 100), (150, 400), LINE_WIDTH)
    pygame.draw.line(window, BLACK, (450, 100), (450, 400), LINE_WIDTH)


def restart(board):
    window.fill(COLOR)
    grid()
    #x1,y1,x2,y2,x3,y3,x4,y4=X1,Y1,X2,Y2,X3,Y3,X4,Y4
    #highlight(x1,y1,x2,y2,x3,y3,x4,y4)
    for i in range(ROWS):
        for j in range(COLUMNS):
            board[i][j]=0
    player=1
    game_end=False
    game_start=False
    draw()
    return game_end,game_start,board,player
#display loop
while True:
    grid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    #link board
        '''key movement'''
        #highlight('center')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s and not game_start:
                game_start=True
                x1,y1,x2,y2,x3,y3,x4,y4=X1,Y1,X2,Y2,X3,Y3,X4,Y4
                x,y=X,Y
                highlight(x1, y1, x2, y2, x3, y3, x4, y4)
            '''navigation working enter player change bugged'''
            if event.key == pygame.K_RETURN and not game_end and game_start:
                print(x,y)
                if free(x,y):
                    if player==1:
                        mark(x,y,1)
                        print(board)
                        if goal(player):
                            game_end = True
                            game_start=False
                            max_stats[0] += 1
                            min_stats[1] += 1
                        elif full():
                            max_stats[2]+=1
                            min_stats[2]+=1
                        player = 2
                    elif player==2:
                        mark(x, y, 2)
                        if goal(player):
                            game_end = True
                            game_start=False
                            max_stats[0] += 1
                            min_stats[1] += 1
                        elif full():
                            max_stats[2] += 1
                            min_stats[2] += 1
                        player = 1
                    draw()
            elif event.key == pygame.K_LEFT and game_start:
                if y>0:
                    y -= 1
                    window.fill(COLOR)
                    grid()
                    draw()
                    x1-=100
                    x2-=100
                    x3-=100
                    x4-=100
                    highlight(x1, y1, x2, y2, x3, y3, x4, y4)
                    print(x,y)
            elif event.key == pygame.K_RIGHT and game_start:
                if y<2:
                    y +=1
                    window.fill(COLOR)
                    grid()
                    draw()
                    x1+=100
                    x2+=100
                    x3+=100
                    x4+=100
                    highlight(x1, y1, x2, y2, x3, y3, x4, y4)
                    print(x,y)
            elif event.key == pygame.K_UP and game_start:
                if x>0:
                    x -=1
                    window.fill(COLOR)
                    grid()
                    draw()
                    y1-=100
                    y2-=100
                    y3-=100
                    y4-=100
                    highlight(x1, y1, x2, y2, x3, y3, x4, y4)
                    print(x,y)
            elif event.key == pygame.K_DOWN and game_start:
                if x<2:
                    x +=1
                    window.fill(COLOR)
                    grid()
                    draw()
                    y1+=100
                    y2+=100
                    y3+=100
                    y4+=100
                    highlight(x1, y1, x2, y2, x3, y3, x4, y4)
                    #print(x,y)
            if event.key == pygame.K_r:
                game_end, game_start, board, player = restart(board)

        '''currently with mouse click, convert this to navigation for player 2 with arrow keys and enter key like refresh'''
        '''if event.type == pygame.MOUSEBUTTONDOWN and not game_end:
            mouseX=event.pos[0]#x
            mouseY=event.pos[1]#y
            click_row= int((mouseY-100)//100)
            click_col= int((mouseX-150)//100)

            if (click_row < 0 or click_row > 2 ) or (click_col < 0 or click_col > 2):
                continue
            elif free(click_row, click_col):
                if player==1:
                    mark(click_row,click_col,1)
                    if goal(player):
                        game_end=True
                        max_stats[0]+=1
                        min_stats[1]+=1
                    player=2
                elif player==2:
                    mark(click_row,click_col,2)
                    if goal(player):
                        game_end=True
                        max_stats[0]+=1
                        min_stats[1]+=1
                    player=1
        if full():
            max_stats[2]+=1
            min_stats[2]+=1
            draw()'''
        text()
        #highlight(0)
        #if event.type == pygame.KEYDOWN:
#    elif event.key == pygame.K_r:
#        restart()
    pygame.display.update()