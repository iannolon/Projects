#IanNolon
#4/4/18
#ticTacToeGraphics.py

#import graphics and random integer, needed for the program
from ggame import *
from random import randint

#cell size constant, easily changeable for different sized games
CELL_SIZE = 175 #works best with 200 or 175

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
    if isEmpty(1) == False and isEmpty(2) == False and isEmpty(3) == False:
        if data['sq1'] == data['sq2'] and data['sq2'] == data['sq3']:
            return True
    elif isEmpty(4) == False and isEmpty(5) == False and isEmpty(6) == False:
        if data['sq4'] == data['sq5'] and data['sq5'] == data['sq6']:
            return True
    elif isEmpty(7) == False and isEmpty(8) == False and isEmpty(9) == False:
        if data['sq7'] == data['sq8'] and data['sq8'] == data['sq9']:
            return True
    elif isEmpty(1) == False and isEmpty(4) == False and isEmpty(7) == False:
        if data['sq1'] == data['sq4'] and data['sq4'] == data['sq7']:
            return True
    elif isEmpty(2) == False and isEmpty(5) == False and isEmpty(8) == False:
        if data['sq2'] == data['sq5'] and data['sq5'] == data['sq8']:
            return True
    elif isEmpty(3) == False and isEmpty(6) == False and isEmpty(9) == False:
        if data['sq3'] == data['sq6'] and data['sq6'] == data['sq9']:
            return True
    elif isEmpty(1) == False and isEmpty(5) == False and isEmpty(9) == False:
        if data['sq1'] == data['sq5'] and data['sq5'] == data['sq9']:
            return True
    elif isEmpty(3) == False and isEmpty(5) == False and isEmpty(7) == False:
        if data['sq3'] == data['sq5'] and data['sq5'] == data['sq7']:
            return True
    else:
        return False
    
#checks to see if the board is full and no more moves are possible
def fullBoard():
    if isEmpty(1) == False and isEmpty(2) == False and isEmpty(3) == False and isEmpty(4) == False and isEmpty(5) == False and isEmpty(6) == False and isEmpty(7) == False and isEmpty(8) == False and isEmpty(9) == False:
        return True
    else:
        return False

#code to allow the computer to place O's
def computerTurn():
    r = randint(1,9)
    if r == 1:
        if isEmpty(1) == True:
            Sprite(oGraphic,(20,20))
            data['sq1'] = 2
            return
        else:
            computerTurn()
    elif r == 2:
        if isEmpty(2) == True:
            Sprite(oGraphic,(CELL_SIZE+20,20))
            data['sq2'] = 2
            return
        else:
            computerTurn()
    elif r == 3:
        if isEmpty(3) == True:
            Sprite(oGraphic,(CELL_SIZE*2+20,20))
            data['sq3'] = 2
            return
        else:
            computerTurn()
    elif r == 4:
        if isEmpty(4) == True:
            Sprite(oGraphic,(20,CELL_SIZE+20))
            data['sq4'] = 2
            return
        else:
            computerTurn()
    elif r == 5:
        if isEmpty(5) == True:
            Sprite(oGraphic,(CELL_SIZE+20,CELL_SIZE+20))
            data['sq5'] = 2
            return
        else:
            computerTurn()
    elif r == 6:
        if isEmpty(6) == True:
            Sprite(oGraphic,(CELL_SIZE*2+20,CELL_SIZE+20))
            data['sq6'] = 2
            return
        else:
            computerTurn()
    elif r == 7:
        if isEmpty(7) == True:
            Sprite(oGraphic,(20,CELL_SIZE*2+20))
            data['sq7'] = 2
            return
        else:
            computerTurn()
    elif r == 8:
        if isEmpty(8) == True:
            Sprite(oGraphic,(CELL_SIZE+20,CELL_SIZE*2+20))
            data['sq8'] = 2
            return
        else:
            computerTurn()
    elif r == 9:
        if isEmpty(9) == True:
            Sprite(oGraphic,(CELL_SIZE*2+20,CELL_SIZE*2+20))
            data['sq9'] = 2
            return
        else:
            computerTurn()
    return


def mouseClick(event):
    #determine what square was clicked and place an X there if possible
    xcl=event.x
    ycl=event.y
    winner()
    if winner() == True:
        vText = TextAsset('Winner!!!', fill = black, style = 'bold 300pt Times')
        Sprite(vText,(0,0))
    elif xcl > 0 and xcl < CELL_SIZE and ycl > 0 and ycl < CELL_SIZE:
        if isEmpty(1) == True:
            Sprite(xGraphic,(20,20))
            data['sq1'] = 1
            computerTurn()
    elif xcl > CELL_SIZE and xcl < CELL_SIZE*2 and ycl > 0 and ycl < CELL_SIZE:
        if isEmpty(2) == True:
            Sprite(xGraphic,(CELL_SIZE+20,20))
            data['sq2'] = 1
            computerTurn()
    elif xcl > CELL_SIZE*2 and xcl < CELL_SIZE*3 and ycl > 0 and ycl < CELL_SIZE:
        if isEmpty(3) == True:
            Sprite(xGraphic,(CELL_SIZE*2+20,20))
            data['sq3'] = 1
            computerTurn()
    elif xcl > 0 and xcl < CELL_SIZE and ycl > CELL_SIZE and ycl < CELL_SIZE*2:
        if isEmpty(4) == True:
            Sprite(xGraphic,(20,CELL_SIZE+20))
            data['sq4'] = 1
            computerTurn()
    elif xcl > CELL_SIZE and xcl < CELL_SIZE*2 and ycl > CELL_SIZE and ycl < CELL_SIZE*2:
        if isEmpty(5) == True:
            Sprite(xGraphic,(CELL_SIZE+20,CELL_SIZE+20))
            data['sq5'] = 1
            computerTurn()
    elif xcl > CELL_SIZE*2 and xcl < CELL_SIZE*3 and ycl > CELL_SIZE and ycl < CELL_SIZE*2:
        if isEmpty(6) == True:
            Sprite(xGraphic,(CELL_SIZE*2+20,CELL_SIZE*+20)) #this square doesn't work, it sprites the X inside of square 3 not square 6.
            data['sq6'] = 1
            computerTurn()
    elif xcl > 0 and xcl < CELL_SIZE and ycl > CELL_SIZE*2 and ycl < CELL_SIZE*3:
        if isEmpty(7) == True:
            Sprite(xGraphic,(20,CELL_SIZE*2+20))
            data['sq7'] = 1
            computerTurn()
    elif xcl > CELL_SIZE and xcl < CELL_SIZE*2 and ycl > CELL_SIZE*2 and ycl < CELL_SIZE*3:
        if isEmpty(8) == True:
            Sprite(xGraphic,(CELL_SIZE+20,CELL_SIZE*2+20))
            data['sq8'] = 1
            computerTurn()
    elif xcl > CELL_SIZE*2 and xcl < CELL_SIZE*3 and ycl > CELL_SIZE*2 and ycl < CELL_SIZE*3:
        if isEmpty(9) == True:
            Sprite(xGraphic,(CELL_SIZE*2+20,CELL_SIZE*2+20))
            data['sq9'] = 1
            computerTurn()
    return


#main code
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
    data['winner'] = 0 #when this variable is 0, there is no winner. When it is equal to 1, the player has won. When it is equal to 2, the computer has won.
    
    #color and outline
    black = Color(0x000000,1)
    blackOutline = LineStyle(1,black)
    
    #lines for the graph and the X and O graphics are here
    horzLine = RectangleAsset(CELL_SIZE*3,CELL_SIZE/40,blackOutline,black)
    vertLine = RectangleAsset(CELL_SIZE/40,CELL_SIZE*3,blackOutline,black)
    fontSize = CELL_SIZE/1.6
    xGraphic = TextAsset('X', fill = black, style = 'bold 125pt Times')
    oGraphic = TextAsset('O', fill = black, style = 'bold 125pt Times')
    
    #sprites the 3 by 3 graph 
    Sprite(horzLine,(0,0))
    Sprite(horzLine,(0,CELL_SIZE))
    Sprite(horzLine,(0,CELL_SIZE*2))
    Sprite(horzLine,(0,CELL_SIZE*3))
    Sprite(vertLine,(0,0))
    Sprite(vertLine,(CELL_SIZE,0))
    Sprite(vertLine,(CELL_SIZE*2,0))
    Sprite(vertLine,(CELL_SIZE*3,0))
    
    #runs the code
    App().listenMouseEvent('click',mouseClick)
    App().run()
    
