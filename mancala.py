#IanNolon
#5/23/18
#mancala.py

from ggame import *

#This makes the buckets the way they are at the beginning of the game, before anybody has taken any moves.
def fillBuckets():
    data['matrix'] = [[4,4,4,4,4,4],[4,4,4,4,4,4]]
    data['stores'] = [0,0]

#This sets up the board with the starting configuration and sprites all the graphics.
def redrawAll():
    for item in App().spritelist[:]: #this deletes all the previous graphics so that numbers are not sprited on top of each other.
        item.destroy()
    
    #fillBuckets()
    data['matrix'] = [[4,4,4,4,4,4],[4,4,4,4,4,4]]
    data['stores'] = [0,0]
    data['turn'] = 1
    
    black = Color(0x000000,1)
    tan = Color(0xE3E385,1)
    yellow = Color(0xF6F605,1)
    blue = Color(0x51BBEC,1)
    
    blackOutline = LineStyle(1,black)
    tanOutline = LineStyle(1,tan)
    
    #sprites board graphics
    board = RectangleAsset(data['XLEN'],data['YLEN'],blackOutline,tan)
    store = RectangleAsset(data['XLEN']/7,data['YLEN']/1.5,blackOutline,yellow)
    house = CircleAsset(data['XLEN']/25,blackOutline,blue) 
    Sprite(board)
    Sprite(store,(data['XLEN']/18,data['YLEN']/6)) #a store is one of the two long yellow things on the sides of the board
    Sprite(store,(data['XLEN']/18+data['XLEN']/1.35,data['YLEN']/6))
    Sprite(house,(2 * data['XLEN']/10 +0.01*data['XLEN'],data['YLEN']/6)) #a house is one of the blue circle things in the middle of the board
    Sprite(house,(3 * data['XLEN']/10 +0.005*data['XLEN'],data['YLEN']/6))
    Sprite(house,(4 * data['XLEN']/10,data['YLEN']/6))
    Sprite(house,(5 * data['XLEN']/10,data['YLEN']/6))
    Sprite(house,(6 * data['XLEN']/10,data['YLEN']/6))
    Sprite(house,(7 * data['XLEN']/10,data['YLEN']/6))
    Sprite(house,(2 * data['XLEN']/10 +0.01*data['XLEN'],data['YLEN']/1.75))
    Sprite(house,(3 * data['XLEN']/10 +0.005*data['XLEN'],data['YLEN']/1.75))
    Sprite(house,(4 * data['XLEN']/10,data['YLEN']/1.75))
    Sprite(house,(5 * data['XLEN']/10,data['YLEN']/1.75))
    Sprite(house,(6 * data['XLEN']/10,data['YLEN']/1.75))
    Sprite(house,(7 * data['XLEN']/10,data['YLEN']/1.75))
    for r in range(0,6): #sprites the numbers that represent how many stones are in each house
        for c in range(0,2):
            houNum = TextAsset(str(data['matrix'][c][r-1]), fill = black, style = 'bold 50pt Times') #the font size does not change when the XLEN constant changes.
            if c == 0: #sprites first collumn
                if r == 0:
                    Sprite(houNum,((2+r)*data['XLEN']/10+data['XLEN']/50+data['XLEN']*0.01,data['YLEN']/6))
                elif r == 1:
                    Sprite(houNum,((2+r)*data['XLEN']/10+data['XLEN']/50+data['XLEN']*0.005,data['YLEN']/6))
                else:
                    Sprite(houNum,((2+r)*data['XLEN']/10+data['XLEN']/50,data['YLEN']/6))
            else: #sprites second collumn
                if r == 0:
                    Sprite(houNum,((2+r)*data['XLEN']/10+data['XLEN']/50+data['XLEN']*0.01,data['YLEN']/1.75))
                elif r == 1:
                    Sprite(houNum,((2+r)*data['XLEN']/10+data['XLEN']/50+data['XLEN']*0.005,data['YLEN']/1.75))
                else:
                    Sprite(houNum,((2+r)*data['XLEN']/10+data['XLEN']/50,data['YLEN']/1.75))
    for w in range(0,2):
        stoNum = TextAsset(str(data['stores'][w]), fill = black, style = 'bold 80pt Times')
        if w == 0:
            if data['stores'][0] < 10:
                Sprite(stoNum,(data['XLEN']/18+data['XLEN']/25,data['YLEN']/3))
            else:
                Sprite(stoNum,(data['XLEN']/18+data['XLEN']/50,data['YLEN']/3))
        else:
            if data['stores'][1] < 10:
                Sprite(stoNum,(data['XLEN']/18+data['XLEN']/25+data['XLEN']/1.35,data['YLEN']/3))
            else:
                Sprite(stoNum,(data['XLEN']/18+data['XLEN']/50+data['XLEN']/1.35,data['YLEN']/3))
    
#This sprites all of the graphics, but with updated numbers. The code for much of it is very similar to redrawAll
def drawPieces():
    for item in App().spritelist[:]:
        item.destroy()
    
    black = Color(0x000000,1)
    tan = Color(0xE3E385,1)
    yellow = Color(0xF6F605,1)
    blue = Color(0x51BBEC,1)
    
    blackOutline = LineStyle(1,black)
    tanOutline = LineStyle(1,tan)
    
    board = RectangleAsset(data['XLEN'],data['YLEN'],blackOutline,tan)
    store = RectangleAsset(data['XLEN']/7,data['YLEN']/1.5,blackOutline,yellow)
    house = CircleAsset(data['XLEN']/25,blackOutline,blue) 
    if data['turn'] == 1:
        turntxt = TextAsset('Top player\'s turn', fill = black, style = 'bold 30pt Times')
    elif data['turn'] == 2:
        turntxt = TextAsset('Bottom player\'s turn', fill = black, style = 'bold 30pt Times')
    Sprite(board)
    Sprite(store,(data['XLEN']/18,data['YLEN']/6))
    Sprite(store,(data['XLEN']/18+data['XLEN']/1.35,data['YLEN']/6))
    Sprite(house,(2 * data['XLEN']/10 +0.01*data['XLEN'],data['YLEN']/6))
    Sprite(house,(3 * data['XLEN']/10 +0.005*data['XLEN'],data['YLEN']/6))
    Sprite(house,(4 * data['XLEN']/10,data['YLEN']/6))
    Sprite(house,(5 * data['XLEN']/10,data['YLEN']/6))
    Sprite(house,(6 * data['XLEN']/10,data['YLEN']/6))
    Sprite(house,(7 * data['XLEN']/10,data['YLEN']/6))
    Sprite(house,(2 * data['XLEN']/10 +0.01*data['XLEN'],data['YLEN']/1.75))
    Sprite(house,(3 * data['XLEN']/10 +0.005*data['XLEN'],data['YLEN']/1.75))
    Sprite(house,(4 * data['XLEN']/10,data['YLEN']/1.75))
    Sprite(house,(5 * data['XLEN']/10,data['YLEN']/1.75))
    Sprite(house,(6 * data['XLEN']/10,data['YLEN']/1.75))
    Sprite(house,(7 * data['XLEN']/10,data['YLEN']/1.75))
    for r in range(0,6):
        for c in range(0,2):
            houNum = TextAsset(str(data['matrix'][c][r]), fill = black, style = 'bold 50pt Times') #the font size does not change when the XLEN constant changes.
            if c == 0: #sprites first collumn
                if r == 0:
                    Sprite(houNum,((2+r)*data['XLEN']/10+data['XLEN']/50+data['XLEN']*0.01,data['YLEN']/6))
                elif r == 1:
                    Sprite(houNum,((2+r)*data['XLEN']/10+data['XLEN']/50+data['XLEN']*0.005,data['YLEN']/6))
                else:
                    Sprite(houNum,((2+r)*data['XLEN']/10+data['XLEN']/50,data['YLEN']/6))
            else: #sprites second collumn
                if r == 0:
                    Sprite(houNum,((2+r)*data['XLEN']/10+data['XLEN']/50+data['XLEN']*0.01,data['YLEN']/1.75))
                elif r == 1:
                    Sprite(houNum,((2+r)*data['XLEN']/10+data['XLEN']/50+data['XLEN']*0.005,data['YLEN']/1.75))
                else:
                    Sprite(houNum,((2+r)*data['XLEN']/10+data['XLEN']/50,data['YLEN']/1.75))
    for w in range(0,2):
        stoNum = TextAsset(str(data['stores'][w]), fill = black, style = 'bold 80pt Times')
        if w == 0:
            if data['stores'][0] < 10:
                Sprite(stoNum,(data['XLEN']/18+data['XLEN']/25,data['YLEN']/3))
            else:
                Sprite(stoNum,(data['XLEN']/18+data['XLEN']/50,data['YLEN']/3))
        else:
            if data['stores'][1] < 10:
                Sprite(stoNum,(data['XLEN']/18+data['XLEN']/25+data['XLEN']/1.35,data['YLEN']/3))
            else:
                Sprite(stoNum,(data['XLEN']/18+data['XLEN']/50+data['XLEN']/1.35,data['YLEN']/3))
    Sprite(turntxt,(data['XLEN']-data['XLEN']/7,data['YLEN']))
    
#This moves the pieces how they should be moved. When a house is clicked, its number becomes zero and all of the houses to the left of it go up by one for how many pieces were in the clicked house
def movePieces(row,collumn):
    goAgain = False
    #print(row-1,'row',collumn-1,'collumn')
    quan = data['matrix'][row-1][collumn-1]
    if data['turn'] == 1:
        if row != 2:
            data['matrix'][row-1][collumn-1] = 0
            if row == 1:
                i = collumn-2
                while quan > 0:
                    if i < 0:
                        data['stores'][row-1] += 1
                        i = 0
                        quan -= 1
                        if quan == 0:
                            goAgain = True
                        while quan > 0:
                            data['matrix'][row][i] += 1
                            i += 1
                            quan -= 1
                    else:
                        data['matrix'][row-1][i] += 1
                        i -= 1
                        quan -= 1
            if goAgain == False:
                data['turn'] = 2
            else:
                data['turn'] = 1
    elif data['turn'] == 2:
        if row != 1:
            data['matrix'][row-1][collumn-1] = 0
            if row == 2:
                i = collumn
                while quan > 0:
                    if i == 6:
                        data['stores'][row-1] += 1
                        i = 5
                        quan -= 1
                        if quan == 0:
                            goAgain = True
                        while quan > -1:
                            data['matrix'][row-2][i] += 1
                            i -= 1
                            quan -= 1
                    else:
                        data['matrix'][row-1][i] += 1
                        i += 1
                        quan -= 1
            if goAgain == False:
                data['turn'] = 1
            else:
                data['turn'] = 2
    drawPieces()
    #print(data['matrix'])

            
#This determines if the game is over or not by seeing if one of the rows is empty or not and it returns who won along with a Boolean
def gameOver():
    if data['matrix'][0] == [0,0,0,0,0,0]:
        topVText = TextAsset('Top player wins!', fill = black, style = 'bold 50pt Times')
        Sprite(topVtext,(data['XLEN']-data['XLEN']/3,data['YLEN'])
        return True
    elif data['matrix'][1] == [0,0,0,0,0,0]:
        botVText = TextAsset('Bottom player wins!', fill = black, style = 'bold 50pt Times')
        Sprite(botVtext,(data['XLEN']-data['XLEN']/3,data['YLEN'])
        return True
    else:
        return False

#This determines which house you clicked and sends that information by calling the movePieces function with the correct row and collumn
def mouseClick(event):
    if gameOver() == False:
        if event.x > 2 * data['XLEN']/10 +0.01*data['XLEN'] and event.y > data['YLEN']/6 and event.x < 3 * data['XLEN']/10 +0.005*data['XLEN'] and event.y < data['YLEN']/2.5:
            movePieces(1,1)
        elif event.x > 3 * data['XLEN']/10 +0.005*data['XLEN'] and event.y > data['YLEN']/6 and event.x < 4 * data['XLEN']/10 and event.y < data['YLEN']/2.5:
            movePieces(1,2)
        elif event.x > 4 * data['XLEN']/10 and event.y > data['YLEN']/6 and event.x < 5 * data['XLEN']/10 and event.y < data['YLEN']/2.5:
            movePieces(1,3)
        elif event.x > 5 * data['XLEN']/10 and event.y > data['YLEN']/6 and event.x < 6 * data['XLEN']/10 and event.y < data['YLEN']/2.5:
            movePieces(1,4)
        elif event.x > 6 * data['XLEN']/10 and event.y > data['YLEN']/6 and event.x < 7 * data['XLEN']/10 and event.y < data['YLEN']/2.5:
            movePieces(1,5)
        elif event.x > 7 * data['XLEN']/10 and event.y > data['YLEN']/6 and event.x < 8 * data['XLEN']/10 and event.y < data['YLEN']/2.5:
            movePieces(1,6)
        elif event.x > 2 * data['XLEN']/10 +0.01*data['XLEN'] and event.y > data['YLEN']/1.75 and event.x < 3 * data['XLEN']/10 +0.005*data['XLEN'] and event.y < data['YLEN']/1.25:
            movePieces(2,1)
        elif event.x > 3 * data['XLEN']/10 +0.005*data['XLEN'] and event.y > data['YLEN']/1.75 and event.x < 4 * data['XLEN']/10 and event.y < data['YLEN']/1.25:
            movePieces(2,2)
        elif event.x > 4 * data['XLEN']/10 and event.y > data['YLEN']/1.75 and event.x < 5 * data['XLEN']/10 and event.y < data['YLEN']/1.25:
            movePieces(2,3)
        elif event.x > 5 * data['XLEN']/10 and event.y > data['YLEN']/1.75 and event.x < 6 * data['XLEN']/10 and event.y < data['YLEN']/1.25:
            movePieces(2,4)
        elif event.x > 6 * data['XLEN']/10 and event.y > data['YLEN']/1.75 and event.x < 7 * data['XLEN']/10 and event.y < data['YLEN']/1.25:
            movePieces(2,5)
        elif event.x > 7 * data['XLEN']/10 and event.y > data['YLEN']/1.75 and event.x < 8 * data['XLEN']/10 and event.y < data['YLEN']/1.25:
            movePieces(2,6)
    else:
        gameOver()

#The rest of the code is stored here
if __name__ == '__main__':
    data = {} #set up dictionary
    data['XLEN'] = 975 #975 looks nice
    data['YLEN'] = data['XLEN'] * 7/18 #To make the proportions the same
    data['turn'] = 1 #turn 1 is person on top, turn 2 is person on bottom
    fillBuckets()
    redrawAll()
    drawPieces()
    App().listenMouseEvent('click',mouseClick)
    App().run()
