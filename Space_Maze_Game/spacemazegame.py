import turtle

rocket = turtle.Turtle()
spaceman = turtle.Turtle()
space = turtle.Screen()

space.setup(width=800, height=600)  # Optional: set window size
space.title("Space Maze Game")

space.addshape("Spaceman.gif")
spaceman.shape("Spaceman.gif")
spaceman.penup()
spaceman.goto(-103, 255)

space.bgpic("Maze_background.gif")
space.addshape("Rocket.gif")
rocket.shape("Rocket.gif")
rocket.penup()
rocket.goto(180, -250)
rocket.speed(0)

def up():
    rocket.setheading(90)
    rocket.forward(10)
    rocket.setheading(0)

def down():
    rocket.setheading(270)
    rocket.forward(10)
    rocket.setheading(0)

def left():
    rocket.setheading(180)
    rocket.forward(10)
    rocket.setheading(0)

def right():  
    rocket.forward(10)

# Keyboard bindings
space.listen()
space.onkeypress(up, "Up")
space.onkeypress(down, "Down")
space.onkeypress(right, "Right")
space.onkeypress(left, "Left")

# Game loop using ontimer
def check_collision():
    if rocket.distance(spaceman) < 10:
        space.bgpic("winning_game.gif")
    else:
        space.ontimer(check_collision, 100)  # check again after 100ms

check_collision()  # start checking

turtle.done()
