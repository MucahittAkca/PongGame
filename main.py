# scoreboard, tahta, top sınıfları olusturulacak.
# scoreboard skoru tutacak ve ekrana yazacak.
# top kenarlara ve tahtalara carptıgında 90 derece acı artırıp yoluna devam edecek.
# belki belli carpma sayısından sonra hız artırılabilir.
import turtle
from turtle import Screen
from tahta import Tahta, Turtle
from top import Top
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

kurek = Tahta(350)
kurek1 = Tahta(-350)
top = Top()
scoreboard = Scoreboard()

new_ycor = -300
for i in range(21):
    çizgi = Turtle("square")
    çizgi.penup()
    çizgi.color("white")
    çizgi.shapesize(stretch_wid=0.75, stretch_len=0.25)
    çizgi.goto(0, new_ycor)
    new_ycor += 30

screen.listen()
screen.onkey(key="Up", fun=kurek.yukari_cik)
screen.onkey(key="Down", fun=kurek.asagi_in)
screen.onkey(key="w", fun=kurek1.yukari_cik)
screen.onkey(key="s", fun=kurek1.asagi_in)

game_is_on = True

while game_is_on:
    time.sleep(top.move_speed)
    screen.update()
    top.hareket_et()
    scoreboard.update_score()


    if top.xcor() > 380:
        top.restart()
        scoreboard.l_point()
        hız = 0

    elif top.xcor() < -380:
        top.restart()
        scoreboard.r_point()
        hız = 0

    if top.ycor() == 280 or top.ycor() == -280:
        top.çarpma_y()

    if top.distance(kurek) < 60 and top.xcor() > 320 or top.distance(kurek1) < 60 and top.xcor() < -320:
        top.carpma_x()



screen.exitonclick()
