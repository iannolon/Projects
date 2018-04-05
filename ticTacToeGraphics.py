#IanNolon
#4/4/18
#ticTacToeGraphics.py

from ggame import *
from random import randint

def isEmpty(sqNum):
    #if square is empty:
        #return True
    #else:
        #return False
        return

def winner():
    #if someone has won:
        #return True
    #else:
        #return False
        return
        
def fullBoard():
    #if isEmpty(1) == False and isEmpty(2) == False and isEmpty(3) == False and isEmpty(4) == False and isEmpty(5) == False and isEmpty(6) == False and isEmpty(7) == False and isEmpty(8) == False and isEmpty(9) == False:
        #return True
    #else:
        #return False
        return

def computerTurn():
    r = randint(1,10)
    #if isEmpty(r) = True:
        #computer places his piece in square r
    return

def mouseClick(event):
    #determine what square was clicked
    #place an X there if possible
    xcl=event.x
    ycl=event.y
    if xcl > 0 and xcl < 200 and ycl > 0 and ycl < 200:
        #if isEmpty(1) = True:
            Sprite(ldiagLine,(20,20))
    if xcl > 200 and xcl < 400 and ycl > 0 and ycl < 200:
        #if isEmpty(2) = True:
            Sprite(ldiagLine,(220,20))
    if xcl > 400 and xcl < 600 and ycl > 0 and ycl < 200:
        #if isEmpty(3) = True:
            Sprite(ldiagLine,(420,20))
    if xcl > 0 and xcl < 200 and ycl > 200 and ycl < 400:
        #if isEmpty(4) = True:
            Sprite(ldiagLine,(20,220))
    if xcl > 200 and xcl < 400 and ycl > 200 and ycl < 400:
        #if isEmpty(5) = True:
            Sprite(ldiagLine,(220,220))
    if xcl > 400 and xcl < 600 and ycl > 200 and ycl < 400:
        #if isEmpty(6) = True:
            Sprite(ldiagLine,(420,220))
    if xcl > 0 and xcl < 200 and ycl > 400 and ycl < 600:
        #if isEmpty(7) = True:
            Sprite(ldiagLine,(20,420))
    if xcl > 200 and xcl < 400 and ycl > 400 and ycl < 600:
        #if isEmpty(8) = True:
            Sprite(ldiagLine,(220,420))
    if xcl > 400 and xcl < 600 and ycl > 400 and ycl < 600:
        #if isEmpty(9) = True:
            Sprite(ldiagLine,(420,420))
    return

if __name__=='__main__':
    
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
    
    black = Color(0x000000,1)
    blackOutline = LineStyle(1,black)
    
    horzLine = RectangleAsset(200,5,blackOutline,black)
    vertLine = RectangleAsset(5,200,blackOutline,black)
    ldiagLine = LineAsset(160,160,blackOutline)
    # = LineAsset(0,180,blackOutline)
    
    Sprite(horzLine,(0,0))
    Sprite(vertLine,(0,0))
    Sprite(horzLine,(200,0))
    Sprite(vertLine,(200,0))
    Sprite(horzLine,(400,0))
    Sprite(vertLine,(400,0))
    Sprite(vertLine,(600,0))
    Sprite(horzLine,(0,200))
    Sprite(vertLine,(0,200))
    Sprite(horzLine,(200,200))
    Sprite(vertLine,(200,200))
    Sprite(horzLine,(400,200))
    Sprite(vertLine,(400,200))
    Sprite(vertLine,(600,200))
    Sprite(horzLine,(0,400))
    Sprite(vertLine,(0,400))
    Sprite(horzLine,(200,400))
    Sprite(vertLine,(200,400))
    Sprite(horzLine,(400,400))
    Sprite(vertLine,(400,400))
    Sprite(vertLine,(600,400))
    
    
    App().listenMouseEvent('click',mouseClick)
    App().run()
