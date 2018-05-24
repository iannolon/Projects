#IanNolon
#5/23/18
#mancala.py

from ggame import *
'''
def fillBuckets():
    board = [[4,4,4,4,4,4],[4,4,4,4,4,4]]
    
def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    fillBuckets()
    
def drawPieces():
    for stor in board:
        print(stor)

def movePieces(row,collumn):
    for i in range(board[row][collumn]):
        
    
    
def gameOver():
    
def mouseClick(event):
'''


if __name__ == '__main__':
    
    matrix = [[4,4,4,4,4,4],[4,4,4,4,4,4]]

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
    for i in matrix:
        if int(i) < 5:
            i = TextAsset(str(matrix[0][i-1]), fill = black, style = 'bold 40pt Times')
        else:
            i = TextAsset(str(matrix[1][i-5]), fill = black, style = 'bold 40pt Times')
    b1 = TextAsset(board[0], fill = black, style = 'bold 40pt Times')
    c1 = TextAsset(board[0], fill = black, style = 'bold 40pt Times')
    d1 = TextAsset(board[0], fill = black, style = 'bold 40pt Times')
    e1 = TextAsset(board[0], fill = black, style = 'bold 40pt Times')
    f1 = TextAsset(board[0], fill = black, style = 'bold 40pt Times')
    a2 = TextAsset(board[0], fill = black, style = 'bold 40pt Times')
    b2 = TextAsset(board[0], fill = black, style = 'bold 40pt Times')
    c2 = TextAsset(board[0], fill = black, style = 'bold 40pt Times')
    d2 = TextAsset(board[0], fill = black, style = 'bold 40pt Times')
    e2 = TextAsset(board[0], fill = black, style = 'bold 40pt Times')
    f2 = TextAsset(board[0], fill = black, style = 'bold 40pt Times')
    
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
    #Sprite(1,(2 * XLEN/10 +0.01*XLEN,YLEN/6))
    App().run()


'''
blueCircle = CircleAsset(50,blackOutline,blue) #radius, outline, fill
greenEllipse = EllipseAsset(100,50,blackOutline,green) #width, height, outline, fill
blackLine = LineAsset(50,160,blackOutline) #x_endpoint, y_endpoint, lineStyle
redTriangle = PolygonAsset([(0,0),(120,180),(60,300)], blackOutline, red) #endpoints, outline, fill
text = TextAsset('Swollen Nolon', fill = black, style = 'bold 40pt Times') #text


Sprite(redRectangle)
Sprite(blueCircle,(50,50))
Sprite(greenEllipse,(200,200))
Sprite(blackLine)
Sprite(redTriangle)
Sprite(text,(300,200))
App().run()
'''