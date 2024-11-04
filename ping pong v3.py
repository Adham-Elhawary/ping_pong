from d import ping_pong
import turtle
player1 = input("please enter the name of player 1 : ")
player2 = input("please enter the name of player 2 : ")
key = 0
wind = turtle.Screen()
wind.title("ping pong")
wind.bgcolor("black")
wind.setup(1400,800)
wind.tracer(0)

#txt
txt = turtle.Turtle()
txt.speed(0)
txt.color("white")
txt.penup()
txt.hideturtle()
txt.goto(0,-100)
txt.write("welcome to ping pong v.3 game made by adham\n\n\n         press 1 to play level 1\n         press 2 to play level 2\n         press 3 to play level 3\n         press 4 to play level 4\n         press 5 to play level 5", align = "center", font=("courier",30,"normal"))

#ping_pong
def ping_pong_level_1():
    ping_pong_1 = ping_pong(0.5,txt,player1,player2)
    ping_pong_1.game()
def ping_pong_level_2():
    ping_pong_2 = ping_pong(1,txt,player1,player2)
    ping_pong_2.game()
def ping_pong_level_3():
    ping_pong_3 = ping_pong(1.5,txt,player1,player2)
    ping_pong_3.game()
def ping_pong_level_4():
    ping_pong_4 = ping_pong(2,txt,player1,player2)
    ping_pong_4.game()
def ping_pong_level_5():
    ping_pong_5 = ping_pong(2.5,txt,player1,player2)
    ping_pong_5.game()
#window

wind.listen()
wind.onkeypress(ping_pong_level_1, "1")
wind.onkeypress(ping_pong_level_2, "2")
wind.onkeypress(ping_pong_level_3, "3")
wind.onkeypress(ping_pong_level_4, "4")
wind.onkeypress(ping_pong_level_5, "5")

while True :
    wind.update()