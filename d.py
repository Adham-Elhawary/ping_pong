import turtle

class ping_pong():
    def __init__(self,speed,txt,player1,player2):
        self.speed = speed
        self.txt = txt
        self.player1 = player1
        self.player2 = player2


    def game(self):


        self.txt.clear()
        wind = turtle.Screen()
        wind.title("ping pong By Adham")
        wind.bgcolor("black")
        wind.setup(1400, 800)  # 700 , 400
        wind.tracer(0)

        # madrab 1
        m1 = turtle.Turtle()
        m1.speed(0)
        m1.shape("square")
        m1.color("blue")
        m1.shapesize(stretch_wid=7, stretch_len=.5)
        m1.penup()
        m1.goto(-650, 0)

        # madrab 2
        m2 = turtle.Turtle()
        m2.speed(0)
        m2.shape("square")
        m2.color("red")
        m2.shapesize(stretch_wid=7, stretch_len=.5)
        m2.penup()
        m2.goto(650, 0)

        # ball
        b = turtle.Turtle()
        b.speed(0)
        b.shape("circle")
        b.color("white")
        b.penup()
        b.goto(0, 0)
        b.dx = self.speed
        b.dy = self.speed

        # score
        score = turtle.Turtle()
        score.speed(0)
        score.color("white")
        score.penup()
        score.hideturtle()
        score.goto(0, 300)
        player1 = self.player1.upper()
        player2 = self.player2.upper()
        score.write(f"{player1} : 0 || {player2} : 0", align="center", font=("courier", 24, "normal"))
        score1 = 0
        score2 = 0

        #player's names


        # functions
        def m1_up():
            y = m1.ycor()
            if y != 350:
                y += 50
                m1.sety(y)

        def m1_down():
            y = m1.ycor()
            if y != -350:
                y -= 50
                m1.sety(y)

        # keyboard bindings
        wind.listen()
        wind.onkeypress(m1_up, "w")

        wind.listen()
        wind.onkeypress(m1_down, "s")

        def m2_up():
            y = m2.ycor()
            if y != 350:
                y += 50
                m2.sety(y)

        def m2_down():
            y = m2.ycor()
            if y != -350:
                y -= 50
                m2.sety(y)

        # keyboard bindings
        wind.listen()
        wind.onkeypress(m2_up, "Up")

        wind.listen()
        wind.onkeypress(m2_down, "Down")

        while True:
            wind.update()

            # move ball
            b.setx(b.xcor() + b.dx)
            b.sety(b.ycor() + b.dy)

            # border check
            if b.ycor() > 390:
                b.sety(390)
                b.dy *= -1

            if b.ycor() < -390:
                b.sety(-390)
                b.dy *= -1

            if b.xcor() > 690:
                b.goto(0, 0)
                b.dx = self.speed
                b.dx *= -1
                score1 += 1
                score.clear()
                score.write("{} : {} || {} : {}".format(player1,score1,player2 ,score2), align="center",
                            font=("courier", 24, "normal"))

            if b.xcor() < -690:
                b.goto(0, 0)
                b.dx = self.speed
                b.dx *= -1
                score2 += 1
                score.clear()
                score.write("{} : {} || {} : {}".format(player1 ,score1,player2 ,score2), align="center",
                            font=("courier", 24, "normal"))

            # tasadom madrab with ball

            if (b.xcor() > 640 and b.xcor() < 650) and (b.ycor() < m2.ycor() + 90 and b.ycor() > m2.ycor() - 90):
                b.setx(640)
                b.dx *= -1.1

            if (b.xcor() < -640 and b.xcor() > -650) and (b.ycor() < m1.ycor() + 90 and b.ycor() > m1.ycor() - 90):
                b.setx(-640)
                b.dx *= -1.1




