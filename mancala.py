#IanNolon
#5/23/18
#mancala.py

from ggame import *

def fillBuckets():
    matrix = [[4,4,4,4,4,4],[4,4,4,4,4,4]]
    stores = [0,0]
    

def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    
    fillBuckets()
    
    black = Color(0x000000,1)
    tan = Color(0xE3E385,1)
    yellow = Color(0xF6F605,1)
    blue = Color(0x51BBEC,1)
    
    blackOutline = LineStyle(1,black)
    tanOutline = LineStyle(1,tan)
    
    XLEN = 975 #975 looks nice
    YLEN = XLEN * 7/18 #To make the proportions the same
    
    board = RectangleAsset(XLEN,YLEN,blackOutline,tan)
    store = RectangleAsset(XLEN/7,YLEN/1.5,blackOutline,yellow)
    house = CircleAsset(XLEN/25,blackOutline,blue) 
    Sprite(board)
    Sprite(store,(XLEN/18,YLEN/6))
    Sprite(store,(XLEN/18+XLEN/1.35,YLEN/6))
    Sprite(house,(2 * XLEN/10 +0.01*XLEN,YLEN/6))
    Sprite(house,(3 * XLEN/10 +0.005*XLEN,YLEN/6))
    Sprite(house,(4 * XLEN/10,YLEN/6))
    Sprite(house,(5 * XLEN/10,YLEN/6))
    Sprite(house,(6 * XLEN/10,YLEN/6))
    Sprite(house,(7 * XLEN/10,YLEN/6))
    Sprite(house,(2 * XLEN/10 +0.01*XLEN,YLEN/1.75))
    Sprite(house,(3 * XLEN/10 +0.005*XLEN,YLEN/1.75))
    Sprite(house,(4 * XLEN/10,YLEN/1.75))
    Sprite(house,(5 * XLEN/10,YLEN/1.75))
    Sprite(house,(6 * XLEN/10,YLEN/1.75))
    Sprite(house,(7 * XLEN/10,YLEN/1.75))
    for r in range(0,6):
        for c in range(0,2):
            houNum = TextAsset(str(matrix[c][r-1]), fill = black, style = 'bold 50pt Times') #the font size does not change when the XLEN constant changes.
            if c == 0: #sprites first collumn
                if r == 0:
                    Sprite(houNum,((2+r)*XLEN/10+XLEN/50+XLEN*0.01,YLEN/6))
                elif r == 1:
                    Sprite(houNum,((2+r)*XLEN/10+XLEN/50+XLEN*0.005,YLEN/6))
                else:
                    Sprite(houNum,((2+r)*XLEN/10+XLEN/50,YLEN/6))
            else: #sprites second collumn
                if r == 0:
                    Sprite(houNum,((2+r)*XLEN/10+XLEN/50+XLEN*0.01,YLEN/1.75))
                elif r == 1:
                    Sprite(houNum,((2+r)*XLEN/10+XLEN/50+XLEN*0.005,YLEN/1.75))
                else:
                    Sprite(houNum,((2+r)*XLEN/10+XLEN/50,YLEN/1.75))
    for w in range(0,2):
        stoNum = TextAsset(str(stores[w]), fill = black, style = 'bold 80pt Times')
        if w == 0:
            if stores[0] < 10:
                Sprite(stoNum,(XLEN/18+XLEN/25,YLEN/3))
            else:
                Sprite(stoNum,(XLEN/18+XLEN/50,YLEN/3))
        else:
            if stores[1] < 10:
                Sprite(stoNum,(XLEN/18+XLEN/25+XLEN/1.35,YLEN/3))
            else:
                Sprite(stoNum,(XLEN/18+XLEN/50+XLEN/1.35,YLEN/3))
    
'''
def drawPieces():
    for stor in board:
        print(stor)

def movePieces(row,collumn):
    for i in range(board[row][collumn]):
        
    
    
def gameOver():
    
def mouseClick(event):
'''


if __name__ == '__main__':
    redrawAll()
    App().run()

