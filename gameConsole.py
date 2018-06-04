#IanJamesDanielandStephen
#idk
#gameConsole.py

from ggame import *
from random import randint

def runSnake():
    #James Roth
    #5/23/18
    #snakeActual.py - snake game for final project
    
    #constants
    CELLSIZE = 20
    ROWS = 10
    COLUMNS = 14
    
    #colors
    black=Color(0x000000,1)
    red=Color(0xff0000,1)
    tan=Color(0xd2b48c,1)
    white=Color(0xffffff,0)
    black=Color(0x000000,1)
    blackOutline=LineStyle(1,black)
    
    #functions
    def reset(event):
        if data["gameOver"] == 1:
            if data["lenSnake"] > data["bestScore"]:
                data["bestScore"] = data["lenSnake"]
            data["gameOver"] = 0
            data["headX"] = COLUMNS/2
            data["headY"] = ROWS/2
            data["lenSnake"] = 1
            data["board"] = []
            data["frames"] = 0
            data["movement"] = [1,0]
            loadSnakeBoard()
            redrawAll()
    
    def redrawAll(): #clears board
        for item in App().spritelist[:]:
            item.destroy()
        drawSnakeBoard()
    
    def gameOver(): #collided with edge/self - ends game
        data["gameOver"] = 1 #doesn't allow snake to move
    
    def drawSnakeBoard(): #draws background, calls snake creation
        drawSnakeCell()
        Sprite(RectangleAsset(CELLSIZE*COLUMNS,CELLSIZE*ROWS,LineStyle(1,black),white)) #border
        Sprite(TextAsset("Length: " + str(data["lenSnake"]), fill = black, style = "15pt Arial"),(CELLSIZE*COLUMNS+10, 10))
        Sprite(TextAsset("High Score:" + str(data["bestScore"]), fill = black, style = "15pt Arial"),(CELLSIZE*COLUMNS+10, 40))
    
    def step(): #runs game
        data["frames"] += 1
        if data["frames"] == data["eyes"]:
            data["frames"] = 0
            if data["gameOver"] == 0:
                moveSnake(data["movement"][0], data["movement"][1])
            else:
                Sprite(TextAsset("Game Over", fill = red, style = "20pt Arial"),(CELLSIZE*(COLUMNS-4)/2,CELLSIZE*(ROWS-4)/2))
    
    def loadSnakeBoard(): #initial matrix of board
        for i in range(0, ROWS+1):
            list1 = []
            for j in range(0, COLUMNS+1):
                list1.append(0)
            data["board"].append(list1)
        data["board"][data["headY"]][data["headX"]] = 1 #initial snake position
        placeFood()
    
    def drawSnakeCell(): #draws snake and food
        #slow version with eyes
        if data["eyes"] == 1:
            largest = data["lenSnake"]
            for i in range(0, len(data["board"])):
                for j in range(0, len(data["board"][i])):
                    if data["board"][i][j] >= 1 and data["board"][i][j] != largest:
                        Sprite(RectangleAsset(CELLSIZE,CELLSIZE,blackOutline,tan),(CELLSIZE*j+1,CELLSIZE*i+1))
                    elif data["board"][i][j] == largest:
                        Sprite(RectangleAsset(CELLSIZE,CELLSIZE,blackOutline,tan),(CELLSIZE*j+1,CELLSIZE*i+1))
                        if data["movement"] == [-1,0]:
                            Sprite(CircleAsset(1,blackOutline,black),((CELLSIZE*j+1)+CELLSIZE*0.33,(CELLSIZE*i+1)+CELLSIZE*0.33))
                            Sprite(CircleAsset(1,blackOutline,black),((CELLSIZE*j+1)+CELLSIZE*0.33,(CELLSIZE*i+1)+CELLSIZE*0.67))
                        elif data["movement"] == [1,0]:
                            Sprite(CircleAsset(1,blackOutline,black),((CELLSIZE*j+1)+CELLSIZE*0.67,(CELLSIZE*i+1)+CELLSIZE*0.33))
                            Sprite(CircleAsset(1,blackOutline,black),((CELLSIZE*j+1)+CELLSIZE*0.67,(CELLSIZE*i+1)+CELLSIZE*0.67))
                        elif data["movement"] == [0,1]:
                            Sprite(CircleAsset(1,blackOutline,black),((CELLSIZE*j+1)+CELLSIZE*0.33,(CELLSIZE*i+1)+CELLSIZE*0.67))
                            Sprite(CircleAsset(1,blackOutline,black),((CELLSIZE*j+1)+CELLSIZE*0.67,(CELLSIZE*i+1)+CELLSIZE*0.67))
                        else:
                            Sprite(CircleAsset(1,blackOutline,black),((CELLSIZE*j+1)+CELLSIZE*0.33,(CELLSIZE*i+1)+CELLSIZE*0.33))
                            Sprite(CircleAsset(1,blackOutline,black),((CELLSIZE*j+1)+CELLSIZE*0.67,(CELLSIZE*i+1)+CELLSIZE*0.33))
                    elif data["board"][i][j] == -1:
                        Sprite(RectangleAsset(CELLSIZE,CELLSIZE,LineStyle(1,black),red),(CELLSIZE*j+1,CELLSIZE*i+1))
        #fastest, no eyes
        if data["eyes"] == 3:
            for i in range(0, len(data["board"])):
                for j in range(0, len(data["board"][i])):
                    if data["board"][i][j] >= 1:
                        Sprite(RectangleAsset(CELLSIZE,CELLSIZE,blackOutline,tan),(CELLSIZE*j+1,CELLSIZE*i+1))
                    elif data["board"][i][j] == -1:
                        Sprite(RectangleAsset(CELLSIZE,CELLSIZE,LineStyle(1,black),red),(CELLSIZE*j+1,CELLSIZE*i+1))
    
    def moveUp(event):
        ignoreTimerEvent = True
        if data["movement"] != [0,1]:
            data["movement"] = [0,-1]
    
    def moveDown(event):
        ignoreTimerEvent = True
        if data["movement"] != [0,-1]:
            data["movement"] = [0,1]
    
    def moveLeft(event):
        ignoreTimerEvent = True
        if data["movement"] != [1,0]:
            data["movement"] = [-1,0]
    
    def moveRight(event):
        ignoreTimerEvent = True
        if data["movement"] != [-1,0]:
            data["movement"] = [1,0]
    
    def moveSnake(col, row): #updates the matrix with the snake's position
        data["headY"] += row
        data["headX"] += col
        if data["board"][data["headY"]][data["headX"]] == -1: #found food?
            data["lenSnake"] += 1
            data["board"][data["headY"]][data["headX"]] = data["lenSnake"]
            placeFood()
        elif data["board"][data["headY"]][data["headX"]] >= 1: #hit yourself?
            gameOver()
        elif data["headY"] >= ROWS or data["headY"] < 0 or data["headX"] >= COLUMNS or data["headX"] < 0: #hit edge?
            gameOver() 
        elif data["board"][data["headY"]][data["headX"]] == 0: #cell empty?
            removeTail()
            data["board"][data["headY"]][data["headX"]] = data["lenSnake"]
        redrawAll()
        
    def placeFood(): #places food in the matrix
        Col = randint(0,COLUMNS-1)
        Row = randint(0, ROWS-1)
        if data["board"][Row][Col] == 0:
            data["board"][Row][Col] = -1
        else:
            placeFood()
    
    def removeTail(): #subtracts 1 from every snake cell, removing the end of the snake
        for i in range(0, len(data["board"])):
            for j in range(0, len(data["board"][i])):
                if data["board"][i][j] >= 1:
                    data["board"][i][j] -= 1
    
    if __name__ == "__main__":
        #dictionary
        data = {}
        data["board"] = []
        data["eyes"] = 0
        data["gameOver"] = 0
        data["headX"] = COLUMNS/2
        data["headY"] = ROWS/2
        data["lenSnake"] = 1
        data["frames"] = 0
        data["bestScore"] = 0
        data["movement"] = [1,0]
        loadSnakeBoard()
        redrawAll()
        
        #do you want eyes?
        data["eyes"] = int(input("Eyes? Y(1)/N(0). Eyes make the game run slower. "))
        if data["eyes"] == 0:
            data["eyes"] = 3
        
        #key controls
        App().listenKeyEvent("keydown","right arrow", moveRight)
        App().listenKeyEvent("keydown","left arrow", moveLeft)
        App().listenKeyEvent("keydown","up arrow", moveUp)
        App().listenKeyEvent("keydown","down arrow", moveDown)
        App().listenKeyEvent("keydown","space", reset)
        
        App().run(step)
        
        
def mouseClick(event):
    if event.x < 400 and event.y < 270:
        runSnake()
    elif event.x > 400 and event.y < 270:
        print('mancala')
    elif event.x < 400 and event.y > 270:
        print('battleship')
    elif event.x > 400 and event.y > 270:
        print('dots and boxes')

if __name__ == '__main__':
    
    black = Color(0x000000,1)
    blackOutline = LineStyle(1,black)
    
    board = RectangleAsset(400,270,blackOutline,white)
    snText = TextAsset(('SNAKE'), fill = black, style = 'bold 50pt Times')
    manText = TextAsset(('MANCALA'), fill = black, style = 'bold 50pt Times')
    btshText = TextAsset(('BATTLESHIP'), fill = black, style = 'bold 50pt Times')
    dtbxText = TextAsset(('DOTS AND BOXES'), fill = black, style = 'bold 50pt Times')
    
    Sprite(board)
    Sprite(board,(400,0))
    Sprite(board,(0,270))
    Sprite(board,(400,270))
    Sprite(snText,(50,50))
    Sprite(manText,(450,50))
    Sprite(btshText,(0, 300))
    Sprite(dtbxText,(450,300))
    App().listenMouseEvent('click',mouseClick)
    App().run()
    
    
    