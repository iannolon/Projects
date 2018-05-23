#IanNolon
#5/23/18
#mancala.py

from ggame import *

black = Color(0x000000,1)
tan = Color(0xE3E385,1)
yellow = Color(0xF6F605,1)

blackOutline = LineStyle(1,black)
tanOutline = LineStyle(1,tan)

XLEN = 900 #900 looks nice
YLEN = XLEN * 4/9 #To make the proportions the same

board = RectangleAsset(XLEN,YLEN,blackOutline,tan)
goal = RectangleAsset(XLEN/7,YLEN/1.5,blackOutline,yellow)

Sprite(board)
Sprite(goal,(XLEN/18,YLEN/6))
Sprite(goal,(XLEN/18+XLEN/1.35,YLEN/6))
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