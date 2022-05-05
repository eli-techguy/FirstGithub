import turtle

#Windows Setup

wn = turtle.Screen()
wn.title("Pong Game by Elias")
wn.bgcolor("white")
wn.setup(width=800, height=600)
wn.tracer(0)

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid = 5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid = 5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Middle Line
line = turtle.Turtle()
line.shape("square")
line.color("black")
line.shapesize(stretch_wid = 1, stretch_len=0.25)
line.penup()
line.goto(0,298)

line = turtle.Turtle()
line.shape("square")
line.color("black")
line.shapesize(stretch_wid = 1, stretch_len=0.25)
line.penup()
line.goto(0,265)

line = turtle.Turtle()
line.shape("square")
line.color("black")
line.shapesize(stretch_wid = 1, stretch_len=0.25)
line.penup()
line.goto(0,230)

line = turtle.Turtle()
line.shape("square")
line.color("black")
line.shapesize(stretch_wid = 1, stretch_len=0.25)
line.penup()
line.goto(0,195)

line = turtle.Turtle()
line.shape("square")
line.color("black")
line.shapesize(stretch_wid = 1, stretch_len=0.25)
line.penup()
line.goto(0,160)

line = turtle.Turtle()
line.shape("square")
line.color("black")
line.shapesize(stretch_wid = 1, stretch_len=0.25)
line.penup()
line.goto(0,125)

line = turtle.Turtle()
line.shape("square")
line.color("black")
line.shapesize(stretch_wid = 1, stretch_len=0.25)
line.penup()
line.goto(0,90)

line = turtle.Turtle()
line.shape("square")
line.color("black")
line.shapesize(stretch_wid = 1, stretch_len=0.25)
line.penup()
line.goto(0,55)

line = turtle.Turtle()
line.shape("square")
line.color("black")
line.shapesize(stretch_wid = 1, stretch_len=0.25)
line.penup()
line.goto(0,20)

line = turtle.Turtle()
line.shape("square")
line.color("black")
line.shapesize(stretch_wid = 1, stretch_len=0.25)
line.penup()
line.goto(0,-15)

line = turtle.Turtle()
line.shape("square")
line.color("black")
line.shapesize(stretch_wid = 1, stretch_len=0.25)
line.penup()
line.goto(0,-50)

line = turtle.Turtle()
line.shape("square")
line.color("black")
line.shapesize(stretch_wid = 1, stretch_len=0.25)
line.penup()
line.goto(0,-85)

line = turtle.Turtle()
line.shape("square")
line.color("black")
line.shapesize(stretch_wid = 1, stretch_len=0.25)
line.penup()
line.goto(0,-120)

line = turtle.Turtle()
line.shape("square")
line.color("black")
line.shapesize(stretch_wid = 1, stretch_len=0.25)
line.penup()
line.goto(0,-155)

line = turtle.Turtle()
line.shape("square")
line.color("black")
line.shapesize(stretch_wid = 1, stretch_len=0.25)
line.penup()
line.goto(0,-190)

line = turtle.Turtle()
line.shape("square")
line.color("black")
line.shapesize(stretch_wid = 1, stretch_len=0.25)
line.penup()
line.goto(0,-225)

line = turtle.Turtle()
line.shape("square")
line.color("black")
line.shapesize(stretch_wid = 1, stretch_len=0.25)
line.penup()
line.goto(0,-260)

line = turtle.Turtle()
line.shape("square")
line.color("black")
line.shapesize(stretch_wid = 1, stretch_len=0.25)
line.penup()
line.goto(0,-295)

#Outer Lines    
line = turtle.Turtle()
line.shape("square")
line.color("black")
line.shapesize(stretch_wid = 1, stretch_len=40)
line.penup()
line.goto(0,300)

line = turtle.Turtle()
line.shape("square")
line.color("black")
line.shapesize(stretch_wid = 30, stretch_len=1)
line.penup()
line.goto(-400,0)

line = turtle.Turtle()
line.shape("square")
line.color("black")
line.shapesize(stretch_wid = 1, stretch_len=40)
line.penup()
line.goto(0,-292)

line = turtle.Turtle()
line.shape("square")
line.color("black")
line.shapesize(stretch_wid = 30, stretch_len=1)
line.penup()
line.goto(392,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy = 0.2

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,245)
pen.write("Player A: 0                           Player B: 0", align="center", font=("Corier", 24, "normal"))

#Score

score_a = 0
score_b = 0

#Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y = y + 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y = y - 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y = y + 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y = y - 20
    paddle_b.sety(y)

#Keyboard Bidiings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


#Main game loop
while True:
    wn.update()
    #Border Checking

    #Top and Buttom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy = ball.dy * -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy = ball.dy* -1

    # Right and Left
    if ball.xcor() > 350:
        score_a = score_a + 1
        #print("Player A: ""+ str(score_a) + "Player B: " + str(score_b))
        pen.clear()
        pen.write("Player A: {}                           Player B: {}".format(score_a, score_b), align="center", font=("Corier", 24, "normal"))
        ball.goto(0,0)
        ball.dx = ball.dx * -1

    if ball.xcor() < -350:
        score_b = score_b + 1
        #print("Player A: ""+ str(score_a) + "Player B: " + str(score_b))
        pen.clear()
        pen.write("Player A: {}                           Player B: {}".format(score_a, score_b), align="center", font=("Corier", 24, "normal"))
        ball.goto(0,0)
        ball.dx = ball.dx* -1


    #Move the Ball
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor()+ ball.dy)

    #Paddle and Ball Collisions
    if (ball.xcor() <-340 and ball.xcor() > -350) and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50:
        ball.setx(-340)
        ball.dx = ball.dx * -1
    elif (ball.xcor() > 340 and ball.xcor() < 350) and ball.ycor() < paddle_b.ycor() +50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.setx(340)
        ball.dx = ball.dx * -1

        # Remove # to make ball bounce of left and right left
        
        #  #Left And Right
    #if ball.xcor() > 390:
     #   ball.setx(390)
      #  ball.dx = ball.dx * -1

    #if ball.xcor() < -390:
        #ball.setx(-390)
        #ball.dx = ball.dx* -1
