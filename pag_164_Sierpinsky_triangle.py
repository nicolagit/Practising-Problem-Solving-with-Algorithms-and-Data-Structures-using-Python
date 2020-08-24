from turtle import *

def drawTriangle(points, color, myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0], points[1][1])
    myTurtle.goto(points[2][0], points[2][1])
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.end_fill()

def get_mid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points, degree, myTurtle):
    colormap = ["blue", "red", "green", "white", "yellow", "violet", "orange"]
    drawTriangle(points, colormap[degree], myTurtle)
    if degree > 0:
        sierpinski(
                [points[0], get_mid(points[0], points[1]), get_mid(points[0], points[2])],
                degree - 1,
                myTurtle)
        sierpinski(
                [points[1], get_mid(points[0], points[1]), get_mid(points[1], points[2])],
                degree - 1,
                myTurtle)
        sierpinski(
            [points[2], get_mid(points[2], points[1]), get_mid(points[0], points[2])],
            degree - 1,
            myTurtle)

myTurtle = Turtle()
myWin = myTurtle.getscreen()
myPoints = [[-180, -150], [0, 150], [180, -150]]
sierpinski(myPoints, 5, myTurtle)
myWin.exitonclick()