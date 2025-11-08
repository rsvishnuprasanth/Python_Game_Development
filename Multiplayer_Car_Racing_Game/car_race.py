import turtle

track = turtle.Screen()

track.bgpic("race_track.gif")

redcar = turtle.Turtle()
track.addshape("red_car.gif")
redcar.shape("red_car.gif")
redcar.setheading(90)
redcar.penup()
redcar.goto(-100,-240)

bluecar = turtle.Turtle()
track.addshape("blue_car.gif")
bluecar.shape("blue_car.gif")
bluecar.setheading(90)
bluecar.penup()
bluecar.goto(100,-240)

def red():
    redcar.forward(5)

def blue():
    bluecar.forward(5)

turtle.onkeypress(red,"Up")
turtle.onkeypress(blue,"w")

turtle.listen()
while True:
    track.update()
    if redcar.pos() > (-100,200):
        track.bgpic("redwins.gif")
    elif bluecar.pos() > (100,200):
        track.bgpic("bluewins.gif")

turtle.done()