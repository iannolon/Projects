#IanNolon
#4/4/18
#ticTacToeGraphics.py

#import graphics and random integer, needed for the program
from ggame import *
from random import randint

'''

These are all the possible square numbers needed for a victory. Top 3 are horizontal, next 3 are vertical, and the last 2 are diagonal.

1,2,3
4,5,6
7,8,9
1,4,7
2,5,8
3,6,9
1,5,9
3,5,7
'''

#checks to see if a square is empty and returns True or False
def isEmpty(sqNum):
    if sqNum == 1:
        if data['sq1'] == 0:
            return True
    elif sqNum == 2:
        if data['sq2'] == 0:
            return True
    elif sqNum == 3:
        if data['sq3'] == 0:
            return True
    elif sqNum == 4:
        if data['sq4'] == 0:
            return True
    elif sqNum == 5:
        if data['sq5'] == 0:
            return True
    elif sqNum == 6:
        if data['sq6'] == 0:
            return True
    elif sqNum == 7:
        if data['sq7'] == 0:
            return True
    elif sqNum == 8:
        if data['sq8'] == 0:
            return True
    elif sqNum == 9:
        if data['sq9'] == 0:
            return True
    else:
        return False

#checks all possible winning combinations on the board to see if somebody has won the game and returns if you won or lost
def winner():
    if isEmpty(1) = False and isEmpty(2) = False and isEmpty(3) = False:
        if data['sq1'] = 1 and data['sq2'] = 1 and data['sq3'] = 1:
            return('You won!')
        elif data['sq1'] = 2 and data['sq2'] = 2 and data['sq3'] = 2:
            return('You lost!')
    elif isEmpty(4) = False and isEmpty(5) = False and isEmpty(6) = False:
        if data['sq4'] = 1 and data['sq5'] = 1 and data['sq6'] = 1:
            return('You won!')
        elif data['sq4'] = 2 and data['sq5'] = 2 and data['sq6'] = 2:
            return('You lost!')
    elif isEmpty(7) = False and isEmpty(8) = False and isEmpty(9) = False:
        if data['sq7'] = 1 and data['sq8'] = 1 and data['sq9'] = 1:
            return('You won!')
        elif data['sq7'] = 2 and data['sq8'] = 2 and data['sq9'] = 2:
            return('You lost!')
    elif isEmpty(1) = False and isEmpty(4) = False and isEmpty(7) = False:
        if data['sq1'] = 1 and data['sq4'] = 1 and data['sq7'] = 1:
            return('You won!')
        elif data['sq1'] = 2 and data['sq4'] = 2 and data['sq7'] = 2:
            return('You lost!')
    elif isEmpty(2) = False and isEmpty(5) = False and isEmpty(8) = False:
        if data['sq4'] = 1 and data['sq5'] = 1 and data['sq6'] = 1:
            return('You won!')
        elif data['sq2'] = 2 and data['sq5'] = 2 and data['sq8'] = 2:
            return('You lost!')
    elif isEmpty(3) = False and isEmpty(6) = False and isEmpty(9) = False:
        if data['sq3'] = 1 and data['sq6'] = 1 and data['sq9'] = 1:
            return('You won!')
        elif data['sq3'] = 2 and data['sq6'] = 2 and data['sq9'] = 2:
            return('You lost!')
    elif isEmpty(1) = False and isEmpty(5) = False and isEmpty(9) = False:
        if data['sq1'] = 1 and data['sq5'] = 1 and data['sq9'] = 1:
            return('You won!')
        elif data['sq1'] = 2 and data['sq5'] = 2 and data['sq9'] = 2:
            return('You lost!')
    elif isEmpty(3) = False and isEmpty(5) = False and isEmpty(7) = False:
        if data['sq3'] = 1 and data['sq5'] = 1 and data['sq7'] = 1:
            return('You won!')
        elif data['sq3'] = 2 and data['sq5'] = 2 and data['sq7'] = 2:
            return('You lost!')
    else:
        return False
    
#checks to see if the board is full and no more moves are possible
def fullBoard():
    if isEmpty(1) == False and isEmpty(2) == False and isEmpty(3) == False and isEmpty(4) == False and isEmpty(5) == False and isEmpty(6) == False and isEmpty(7) == False and isEmpty(8) == False and isEmpty(9) == False:
        #return True
    else:
        return False

#code to allow the computer to place O's
def computerTurn():
    r = randint(1,10)
    if r = 1:
        #if isEmpty(1) = True:
            Sprite(oGraphic,(20,20))
            data['sq1'] = 2
            return
    elif r = 2:
        #if isEmpty(2) = True:
            Sprite(oGraphic,(220,20))
            data['sq2'] = 2
            return
    elif r = 3:
        #if isEmpty(3) = True:
            Sprite(oGraphic,(420,20))
            data['sq3'] = 2
            return
    elif r = 4:
        #if isEmpty(4) = True:
            Sprite(oGraphic,(20,220))
            data['sq4'] = 2
            return
    elif r = 5:
        #if isEmpty(5) = True:
            Sprite(oGraphic,(220,220))
            data['sq5'] = 2
            return
    elif r = 6:
        #if isEmpty(6) = True:
            Sprite(oGraphic,(420,220))
            data['sq6'] = 2
            return
    elif r = 7:
        #if isEmpty(7) = True:
            Sprite(oGraphic,(20,420))
            data['sq7'] = 2
            return
    elif r = 8:
        #if isEmpty(8) = True:
            Sprite(oGraphic,(220,420))
            data['sq8'] = 2
            return
    elif r = 9:
        #if isEmpty(9) = True:
            Sprite(oGraphic,(420,420))
            data['sq9'] = 2
            return
    else:
        computerTurn()
    return
  

def mouseClick(event):
    #determine what square was clicked
    #place an X there if possible
    xcl=event.x
    ycl=event.y
    if xcl > 0 and xcl < 200 and ycl > 0 and ycl < 200:
        #if isEmpty(1) = True:
            Sprite(xGraphic,(20,20))
            data['sq1'] = 1
    if xcl > 200 and xcl < 400 and ycl > 0 and ycl < 200:
        #if isEmpty(2) = True:
            Sprite(xGraphic,(220,20))
            data['sq2'] = 1
    if xcl > 400 and xcl < 600 and ycl > 0 and ycl < 200:
        #if isEmpty(3) = True:
            Sprite(xGraphic,(420,20))
            data['sq3'] = 1
    if xcl > 0 and xcl < 200 and ycl > 200 and ycl < 400:
        #if isEmpty(4) = True:
            Sprite(xGraphic,(20,220))
            data['sq4'] = 1
    if xcl > 200 and xcl < 400 and ycl > 200 and ycl < 400:
        #if isEmpty(5) = True:
            Sprite(xGraphic,(220,220))
            data['sq5'] = 1
    if xcl > 400 and xcl < 600 and ycl > 200 and ycl < 400:
        #if isEmpty(6) = True:
            Sprite(xGraphic,(420,220))
            data['sq6'] = 1
    if xcl > 0 and xcl < 200 and ycl > 400 and ycl < 600:
        #if isEmpty(7) = True:
            Sprite(xGraphic,(20,420))
            data['sq7'] = 1
    if xcl > 200 and xcl < 400 and ycl > 400 and ycl < 600:
        #if isEmpty(8) = True:
            Sprite(xGraphic,(220,420))
            data['sq8'] = 1
    if xcl > 400 and xcl < 600 and ycl > 400 and ycl < 600:
        #if isEmpty(9) = True:
            Sprite(xGraphic,(420,420))
            data['sq9'] = 1
    return


if __name__=='__main__':
    
    #puts variables in a dictionary. If the square is equal to 0, it is empty, if it is 1, then it has an X, and if it is 2, then it has an O. It sets them all to 0 initially because they're all empty.
    data = {}
    data['sq1'] = 0
    data['sq2'] = 0
    data['sq3'] = 0
    data['sq4'] = 0
    data['sq5'] = 0
    data['sq6'] = 0
    data['sq7'] = 0
    data['sq8'] = 0
    data['sq9'] = 0
    
    #color and outline
    black = Color(0x000000,1)
    blackOutline = LineStyle(1,black)
    
    #lines for the graph and the X and O graphics are here
    horzLine = RectangleAsset(600,5,blackOutline,black)
    vertLine = RectangleAsset(5,600,blackOutline,black)
    xGraphic = TextAsset('X', fill = black, style = 'bold 125pt Times')
    oGraphic = TextAsset('O', fill = black, style = 'bold 125pt Times')
    
    #sprites the 3 by 3 graph 
    Sprite(horzLine,(0,0))
    Sprite(horzLine,(0,200))
    Sprite(horzLine,(0,400))
    Sprite(horzLine,(0,600))
    Sprite(vertLine,(0,0))
    Sprite(vertLine,(200,0))
    Sprite(vertLine,(400,0))
    Sprite(vertLine,(600,0))
    
    #runs the code
    App().listenMouseEvent('click',mouseClick)
    App().run()
    
    
    
