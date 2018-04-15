#IanNolon
#4/4/18
#ticTacToeGraphics.py

#import graphics and random integer, needed for the program
from ggame import *
from random import randint

#cell size constant, easily changeable for different sized games
CELL_SIZE = 175 #works best with 200 or 175

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
    return False

#checks all possible winning combinations on the board to see if somebody has won the game and returns if you won or lost
def winner():
    if isEmpty(1) == False and isEmpty(2) == False and isEmpty(3) == False:
        if data['sq1'] == data['sq2'] and data['sq2'] == data['sq3'] and data['sq3'] == 1:
            Sprite(vText,(0,0))
            return True
    elif isEmpty(4) == False and isEmpty(5) == False and isEmpty(6) == False:
        if data['sq4'] == data['sq5'] and data['sq5'] == data['sq6'] and data['sq6'] == 1:
            Sprite(vText,(0,0))
            return True
    elif isEmpty(7) == False and isEmpty(8) == False and isEmpty(9) == False:
        if data['sq7'] == data['sq8'] and data['sq8'] == data['sq9'] and data['sq9'] == 1:
            Sprite(vText,(0,0))
            return True
    elif isEmpty(1) == False and isEmpty(4) == False and isEmpty(7) == False:
        if data['sq1'] == data['sq4'] and data['sq4'] == data['sq7'] and data['sq7'] == 1:
            Sprite(vText,(0,0))
            return True
    elif isEmpty(2) == False and isEmpty(5) == False and isEmpty(8) == False:
        if data['sq2'] == data['sq5'] and data['sq5'] == data['sq8'] and data['sq8'] == 1:
            Sprite(vText,(0,0))
            return True
    elif isEmpty(3) == False and isEmpty(6) == False and isEmpty(9) == False:
        if data['sq3'] == data['sq6'] and data['sq6'] == data['sq9'] and data['sq9'] == 1:
            Sprite(vText,(0,0))
            return True
    elif isEmpty(1) == False and isEmpty(5) == False and isEmpty(9) == False:
        if data['sq1'] == data['sq5'] and data['sq5'] == data['sq9'] and data['sq9'] == 1:
            Sprite(vText,(0,0))
            return True
    elif isEmpty(3) == False and isEmpty(5) == False and isEmpty(7) == False:
        if data['sq3'] == data['sq5'] and data['sq5'] == data['sq7'] and data['sq7'] == 1:
            Sprite(vText,(0,0))
            return True
    else:
        return False
        
def loser():
    if isEmpty(1) == False and isEmpty(2) == False and isEmpty(3) == False:
        if data['sq1'] == data['sq2'] and data['sq2'] == data['sq3'] and data['sq3'] == 2:
            Sprite(lText,(0,0))
            return True
    elif isEmpty(4) == False and isEmpty(5) == False and isEmpty(6) == False:
        if data['sq4'] == data['sq5'] and data['sq5'] == data['sq6'] and data['sq6'] == 2:
            Sprite(lText,(0,0))
            return True
    elif isEmpty(7) == False and isEmpty(8) == False and isEmpty(9) == False:
        if data['sq7'] == data['sq8'] and data['sq8'] == data['sq9'] and data['sq9'] == 2:
            Sprite(lText,(0,0))
            return True
    elif isEmpty(1) == False and isEmpty(4) == False and isEmpty(7) == False:
        if data['sq1'] == data['sq4'] and data['sq4'] == data['sq7'] and data['sq7'] == 2:
            Sprite(lText,(0,0))
            return True
    elif isEmpty(2) == False and isEmpty(5) == False and isEmpty(8) == False:
        if data['sq2'] == data['sq5'] and data['sq5'] == data['sq8'] and data['sq8'] == 2:
            Sprite(lText,(0,0))
            return True
    elif isEmpty(3) == False and isEmpty(6) == False and isEmpty(9) == False:
        if data['sq3'] == data['sq6'] and data['sq6'] == data['sq9'] and data['sq9'] == 2:
            Sprite(lText,(0,0))
            return True
    elif isEmpty(1) == False and isEmpty(5) == False and isEmpty(9) == False:
        if data['sq1'] == data['sq5'] and data['sq5'] == data['sq9'] and data['sq9'] == 2:
            Sprite(lText,(0,0))
            return True
    elif isEmpty(3) == False and isEmpty(5) == False and isEmpty(7) == False:
        if data['sq3'] == data['sq5'] and data['sq5'] == data['sq7'] and data['sq7'] == 2:
            Sprite(lText,(0,0))
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
    ''' #smarter computer
    all win conditions covered here: Top 3 are horizontal, next 3 are vertical, and the last 2 are diagonal.
    1,2,3
    4,5,6
    7,8,9
    1,4,7
    2,5,8
    3,6,9
    1,5,9
    3,5,7
    #win dialogue - if the computer has 2 in a row and a possible winning move, the computer will put its O in the winning spot.
    # put parentheses around the data bc of the ors and ands
    '''
    if (data['sq2'] == 2 and data['sq3'] == 2) or (data['sq4'] == 2 and data['sq7'] == 2) or (data['sq5'] == 2 and data['sq9'] == 2):
        if isEmpty(1) == True:
            Sprite(oGraphic,(20,20))
            data['sq1'] = 2
            return
    elif (data['sq1'] == 2 and data['sq3'] == 2) or (data['sq5'] == 2 and data['sq8'] == 2):
        if isEmpty(2) == True:
            Sprite(oGraphic,(CELL_SIZE+20,20))
            data['sq2'] = 2
            return
    elif (data['sq1'] == 2 and data['sq2'] == 2) or (data['sq6'] == 2 and data['sq9'] == 2) or (data['sq5'] == 2 and data['sq7'] == 2):
        if isEmpty(3) == True:
            Sprite(oGraphic,(CELL_SIZE*2+20,20))
            data['sq3'] = 2
            return
    elif (data['sq5'] == 2 and data['sq6'] == 2) or (data['sq1'] == 2 and data['sq7'] == 2):
        if isEmpty(4) == True:
            Sprite(oGraphic,(20,CELL_SIZE+20))
            data['sq4'] = 2
            return
    elif (data['sq4'] == 2 and data['sq6'] == 2) or (data['sq2'] == 2 and data['sq8'] == 2) or (data['sq1'] == 2 and data['sq9'] == 2) or (data['sq3'] == 2 and data['sq7'] == 2):
        if isEmpty(5) == True:
            Sprite(oGraphic,(CELL_SIZE+20,CELL_SIZE+20))
            data['sq5'] = 2
            return
    elif (data['sq4'] == 2 and data['sq5'] == 2) or (data['sq3'] == 2 and data['sq9'] == 2):
        if isEmpty(6) == True:
            Sprite(oGraphic,(CELL_SIZE*2+20,CELL_SIZE+20))
            data['sq6'] = 2
            return
    elif (data['sq8'] == 2 and data['sq9'] == 2) or (data['sq1'] == 2 and data['sq4'] == 2) or (data['sq3'] == 2 and data['sq5'] == 2):
        if isEmpty(7) == True:
            Sprite(oGraphic,(20,CELL_SIZE*2+20))
            data['sq7'] = 2
            return
    elif (data['sq7'] == 2 and data['sq9'] == 2) or (data['sq2'] == 2 and data['sq5'] == 2):
        if isEmpty(8) == True:
            Sprite(oGraphic,(CELL_SIZE+20,CELL_SIZE*2+20))
            data['sq8'] = 2
            return
    elif (data['sq7'] == 2 and data['sq8'] == 2) or (data['sq3'] == 2 and data['sq6'] == 2) or (data['sq1'] == 2 and data['sq5'] == 2):
        if isEmpty(9) == True:
            Sprite(oGraphic,(CELL_SIZE*2+20,CELL_SIZE*2+20))
            data['sq9'] = 2
            return
    #now it will block you! If you have 2 in a row and are not already blocked, it will place an O there
    elif (data['sq2'] == 1 and data['sq3'] == 1) or (data['sq4'] == 1 and data['sq7'] == 1) or (data['sq5'] == 1 and data['sq9'] == 1):
        if isEmpty(1) == True:
            Sprite(oGraphic,(20,20))
            data['sq1'] = 2
            return
    elif (data['sq1'] == 1 and data['sq3'] == 1) or (data['sq5'] == 1 and data['sq8'] == 1):
        if isEmpty(2) == True:
            Sprite(oGraphic,(CELL_SIZE+20,20))
            data['sq2'] = 2
            return
    elif (data['sq1'] == 1 and data['sq2'] == 1) or (data['sq6'] == 1 and data['sq9'] == 1) or (data['sq5'] == 1 and data['sq7'] == 1):
        if isEmpty(3) == True:
            Sprite(oGraphic,(CELL_SIZE*2+20,20))
            data['sq3'] = 2
            return
    elif (data['sq5'] == 1 and data['sq6'] == 1) or (data['sq1'] == 1 and data['sq7'] == 1):
        if isEmpty(4) == True:
            Sprite(oGraphic,(20,CELL_SIZE+20))
            data['sq4'] = 2
            return
    elif (data['sq4'] == 1 and data['sq6'] == 1) or (data['sq2'] == 1 and data['sq8'] == 1) or (data['sq1'] == 1 and data['sq9'] == 1) or (data['sq3'] == 1 and data['sq7'] == 1):
        if isEmpty(5) == True:
            Sprite(oGraphic,(CELL_SIZE+20,CELL_SIZE+20))
            data['sq5'] = 2
            return
    elif (data['sq4'] == 1 and data['sq5'] == 1) or (data['sq3'] == 1 and data['sq9'] == 1):
        if isEmpty(6) == True:
            Sprite(oGraphic,(CELL_SIZE*2+20,CELL_SIZE+20))
            data['sq6'] = 2
            return
    elif (data['sq8'] == 1 and data['sq9'] == 1) or (data['sq1'] == 1 and data['sq4'] == 1) or (data['sq3'] == 1 and data['sq5'] == 1):
        if isEmpty(7) == True:
            Sprite(oGraphic,(20,CELL_SIZE*2+20))
            data['sq7'] = 2
            return
    elif (data['sq7'] == 1 and data['sq9'] == 1) or (data['sq2'] == 1 and data['sq5'] == 1):
        if isEmpty(8) == True:
            Sprite(oGraphic,(CELL_SIZE+20,CELL_SIZE*2+20))
            data['sq8'] = 2
            return
    elif (data['sq7'] == 1 and data['sq8'] == 1) or (data['sq3'] == 1 and data['sq6'] == 1) or (data['sq1'] == 1 and data['sq5'] == 1):
        if isEmpty(9) == True:
            Sprite(oGraphic,(CELL_SIZE*2+20,CELL_SIZE*2+20))
            data['sq9'] = 2
            return
    '''
    create a fork and block a fork dialogue - forks are where you open up two or more ways to win so the opponent can only block one of them and you win the next turn.
    All possible forks are here:
    1,7,9
    3,7,9
    1,3,7
    1,3,9
    1,3,5
    1,5,7
    5,7,9
    3,5,9
    This fork dialogue will make the computer very smart and hard to beat, so feel free to comment it out if you want an easier game.
    '''
    '''
    elif (data['sq7'] == 2 and data['sq9'] == 2) or (data['sq3'] == 2 and data['sq7'] == 2) or (data['sq3'] == 2 and data['sq9'] == 2) or (data['sq3'] == 2 and data['sq5'] == 2) or (data['sq5'] == 2 and data['sq7'] == 2):
        if isEmpty(1) == True:
            Sprite(oGraphic,(20,20))
            data['sq9'] = 2
            return
    elif (data['sq7'] == 2 and data['sq9'] == 2) or (data['sq1'] == 2 and data['sq7'] == 2) or (data['sq1'] == 2 and data['sq9'] == 2) or (data['sq1'] == 2 and data['sq5'] == 2) or (data['sq5'] == 2 and data['sq9'] == 2):
        if isEmpty(3) == True:
            Sprite(oGraphic,(CELL_SIZE*2+20,20))
            data['sq9'] = 2
            return
    elif (data['sq1'] == 2 and data['sq3'] == 2) or (data['sq1'] == 2 and data['sq7'] == 2) or (data['sq7'] == 2 and data['sq9'] == 2) or (data['sq3'] == 2 and data['sq9'] == 2):
        if isEmpty(5) == True:
            Sprite(oGraphic,(CELL_SIZE+20,CELL_SIZE+20))
            data['sq9'] = 2
            return
    elif (data['sq1'] == 2 and data['sq9'] == 2) or (data['sq3'] == 2 and data['sq9'] == 2) or (data['sq1'] == 2 and data['sq3'] == 2) or (data['sq1'] == 2 and data['sq5'] == 2) or (data['sq5'] == 2 and data['sq9'] == 2):
        if isEmpty(7) == True:
            Sprite(oGraphic,(20,CELL_SIZE*2+20))
            data['sq9'] = 2
            return
    elif (data['sq1'] == 2 and data['sq7'] == 2) or (data['sq3'] == 2 and data['sq7'] == 2) or (data['sq1'] == 2 and data['sq3'] == 2) or (data['sq5'] == 2 and data['sq7'] == 2) or (data['sq3'] == 2 and data['sq5'] == 2):
        if isEmpty(3) == True:
            Sprite(oGraphic,(CELL_SIZE*2+20,20))
            data['sq9'] = 2
            return
    #create fork dialogue to be put here
    '''
    #if none of the above are possible, the computer will play in the middle as it is the most strategically beneficial spot to the computer.
    if isEmpty(5) == True:
        Sprite(oGraphic,(CELL_SIZE+20,CELL_SIZE+20))
        data['sq5'] = 2
        return
    else:
        computerTurn()
    #if the middle is taken, the computer will then play in a random corner.
    r = randint(1,4) 
    if r == 1:
        if isEmpty(1) == True:
            Sprite(oGraphic,(20,20))
            data['sq1'] = 2
            return
        else:
            computerTurn()
    elif r == 2:
        if isEmpty(3) == True:
            Sprite(oGraphic,(CELL_SIZE*2+20,20))
            data['sq3'] = 2
            return
        else:
            computerTurn()
    elif r == 3:
        if isEmpty(7) == True:
            Sprite(oGraphic,(20,CELL_SIZE*2+20))
            data['sq7'] = 2
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
    #lastly, if the computer has no other moves, it will play its piece on a side. 
    #As this is the worst move for the computer to make, it is put last so that it is only achieved if there are no other possible moves that are better.
    r = randint(1,4)
    if r == 1:
        if isEmpty(2) == True:
            Sprite(oGraphic,(CELL_SIZE+20,20))
            data['sq2'] = 2
            return
        else:
            computerTurn()
    elif r == 2:
        if isEmpty(4) == True:
            Sprite(oGraphic,(20,CELL_SIZE+20))
            data['sq4'] = 2
            return
        else:
            computerTurn()
    elif r == 3:
        if isEmpty(6) == True:
            Sprite(oGraphic,(CELL_SIZE*2+20,CELL_SIZE+20))
            data['sq6'] = 2
            return
        else:
            computerTurn()        
    elif r == 4:
        if isEmpty(8) == True:
            Sprite(oGraphic,(CELL_SIZE+20,CELL_SIZE*2+20))
            data['sq8'] = 2
            return
        else:
            computerTurn()
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
    '''
    winner()
    if winner() == True:
        vText = TextAsset('Winner!!!', fill = black, style = 'bold 300pt Times')
        Sprite(vText,(0,0))
    '''
    if xcl > 0 and xcl < CELL_SIZE and ycl > 0 and ycl < CELL_SIZE:
        if isEmpty(1) == True:
            Sprite(xGraphic,(20,20))
            data['sq1'] = 1
            winner()
            computerTurn()
    elif xcl > CELL_SIZE and xcl < CELL_SIZE*2 and ycl > 0 and ycl < CELL_SIZE:
        if isEmpty(2) == True:
            Sprite(xGraphic,(CELL_SIZE+20,20))
            data['sq2'] = 1
            winner()
            computerTurn()
    elif xcl > CELL_SIZE*2 and xcl < CELL_SIZE*3 and ycl > 0 and ycl < CELL_SIZE:
        if isEmpty(3) == True:
            Sprite(xGraphic,(CELL_SIZE*2+20,20))
            data['sq3'] = 1
            winner()
            computerTurn()
    elif xcl > 0 and xcl < CELL_SIZE and ycl > CELL_SIZE and ycl < CELL_SIZE*2:
        if isEmpty(4) == True:
            Sprite(xGraphic,(20,CELL_SIZE+20))
            data['sq4'] = 1
            winner()
            computerTurn()
    elif xcl > CELL_SIZE and xcl < CELL_SIZE*2 and ycl > CELL_SIZE and ycl < CELL_SIZE*2:
        if isEmpty(5) == True:
            Sprite(xGraphic,(CELL_SIZE+20,CELL_SIZE+20))
            data['sq5'] = 1
            winner()
            computerTurn()
    elif xcl > CELL_SIZE*2 and xcl < CELL_SIZE*3 and ycl > CELL_SIZE and ycl < CELL_SIZE*2:
        if isEmpty(6) == True:
            Sprite(xGraphic,(CELL_SIZE*2+20,CELL_SIZE+20))
            data['sq6'] = 1
            winner()
            computerTurn()
    elif xcl > 0 and xcl < CELL_SIZE and ycl > CELL_SIZE*2 and ycl < CELL_SIZE*3:
        if isEmpty(7) == True:
            Sprite(xGraphic,(20,CELL_SIZE*2+20))
            data['sq7'] = 1
            winner()
            computerTurn()
    elif xcl > CELL_SIZE and xcl < CELL_SIZE*2 and ycl > CELL_SIZE*2 and ycl < CELL_SIZE*3:
        if isEmpty(8) == True:
            Sprite(xGraphic,(CELL_SIZE+20,CELL_SIZE*2+20))
            data['sq8'] = 1
            winner()
            computerTurn()
    elif xcl > CELL_SIZE*2 and xcl < CELL_SIZE*3 and ycl > CELL_SIZE*2 and ycl < CELL_SIZE*3:
        if isEmpty(9) == True:
            Sprite(xGraphic,(CELL_SIZE*2+20,CELL_SIZE*2+20))
            data['sq9'] = 1
            winner()
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
    
    #colors and outline
    black = Color(0x000000,1)
    red = Color(0xFF0000,1)
    blackOutline = LineStyle(1,black)
    
    #lines for the graph and the X and O graphics are here, along with winner and loser text
    horzLine = RectangleAsset(CELL_SIZE*3,CELL_SIZE/40,blackOutline,black)
    vertLine = RectangleAsset(CELL_SIZE/40,CELL_SIZE*3,blackOutline,black)
    fontSize = CELL_SIZE/1.6
    xGraphic = TextAsset('X', fill = black, style = 'bold 125pt Times')
    oGraphic = TextAsset('O', fill = black, style = 'bold 125pt Times')
    vText = TextAsset('You win!!!', fill = red, style = 'bold 200pt Times')
    lText = TextAsset('You lose!!!', fill = red, style = 'bold 200pt Times')
    
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
