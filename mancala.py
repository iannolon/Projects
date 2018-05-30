#IanNolon
#5/23/18
#mancala.py

from ggame import *
#ADD THE DICTIONARY TO STORES AND MATRIX

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
    

def drawPieces():
    #define the matrix as it is now
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
    
'''
def movePieces(row,collumn):
    #do i need to add the stores into the main matrix
    
'''
def gameOver():
    if data['matrix'][0] == [0,0,0,0,0,0]:
        print('Top player won!')
        return True
    elif data['matrix'][1] == [0,0,0,0,0,0]:
        print('Bottom player won!')
        return True
    else:
        return False
    

#def mouseClick(event):
    #event.x and event.y
    '''
    2 * XLEN/10 +0.01*XLEN,YLEN/6
    3 * XLEN/10 +0.005*XLEN,YLEN/6
    Sprite(house,(4 * XLEN/10,YLEN/6
    Sprite(house,(5 * XLEN/10,YLEN/6
    Sprite(house,(6 * XLEN/10,YLEN/6
    Sprite(house,(7 * XLEN/10,YLEN/6
    Sprite(house,(2 * XLEN/10 +0.01*XLEN,YLEN/1.75
    3 * XLEN/10 +0.005*XLEN,YLEN/1.75
    4 * XLEN/10,YLEN/1.75
    5 * XLEN/10,YLEN/1.75
    6 * XLEN/10,YLEN/1.75
    7 * XLEN/10,YLEN/1.75
    '''


if __name__ == '__main__':
    data = {}
    data['XLEN'] = 975 #975 looks nice
    data['YLEN'] = data['XLEN'] * 7/18 #To make the proportions the same
    fillBuckets()
    redrawAll()
    #matrix = [[4,4,2,4,7,4],[4,4,0,4,2,4]]
    #stores = [0,6]
    drawPieces()
    App().run()

