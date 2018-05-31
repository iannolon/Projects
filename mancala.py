#IanNolon
#5/23/18
#mancala.py
#add comments

from ggame import *

def fillBuckets():
    data['matrix'] = [[4,4,4,4,4,4],[4,4,4,4,4,4]]
    data['stores'] = [0,0]

def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    
    #fillBuckets()
    data['matrix'] = [[4,4,4,4,4,4],[4,4,4,4,4,4]]
    data['stores'] = [0,0]
    
    black = Color(0x000000,1)
    tan = Color(0xE3E385,1)
    yellow = Color(0xF6F605,1)
    blue = Color(0x51BBEC,1)
    
    blackOutline = LineStyle(1,black)
    tanOutline = LineStyle(1,tan)
    
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
    for r in range(0,6):
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
    

def movePieces(row,collumn):
    print(row,'row',collumn,'collumn')
    quan = data['matrix'][row-1][collumn-1]
    if quan > 0:
        data['matrix'][row-1][collumn-1] = 0
        for i in range(quan-1,0,-1):
            if data['matrix'][collumn-i] == 6:
                data['stores'][row-1] += 1
                drawPieces()
            else:
                data['matrix'][row-i][collumn-i] += 1
                drawPieces()
    

def gameOver():
    if data['matrix'][0] == [0,0,0,0,0,0]:
        print('Top player won!')
        return True
    elif data['matrix'][1] == [0,0,0,0,0,0]:
        print('Bottom player won!')
        return True
    else:
        return False
    

def mouseClick(event):
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


if __name__ == '__main__':
    data = {}
    data['XLEN'] = 975 #975 looks nice
    data['YLEN'] = data['XLEN'] * 7/18 #To make the proportions the same
    fillBuckets()
    redrawAll()
    #matrix = [[4,4,2,4,7,4],[4,4,0,4,2,4]]
    #stores = [0,6]
    drawPieces()
    App().listenMouseEvent('click',mouseClick)
    App().run()

