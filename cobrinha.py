import turtle
import random
import time

tela = turtle.Screen()
tela.title("Jogo da cobrinha")

pontos = 0

tela.bgcolor("black")
tela.setup(width=600, height=600)
tela.tracer(0)

cobra = turtle.Turtle()
cobra.speed(0)
cobra.shape("square")
cobra.color("white")
cobra.penup()
cobra.goto(0,0)
cobra.direction = 'stop'

comida = turtle.Turtle()
comida.speed(0)
comida.shape('circle')
comida.color('red')
comida.penup()
comida.goto(0,100)

def vai_para_direita():
    cobra.direction = "right"

def vai_para_esquerda():
    cobra.direction = "left"

def vai_para_cima():
    cobra.direction = "up"

def vai_para_baixo():
    cobra.direction = "down"

tela.listen()
tela.onkeypress(vai_para_direita, "Right")
tela.onkeypress(vai_para_esquerda, "Left")
tela.onkeypress(vai_para_cima, "Up")
tela.onkeypress(vai_para_baixo, "Down")

while True:
    tela.update()
    if cobra.distance(comida) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        comida.goto(x,y)
        pontos += 10
        tela.title("Pontos: {}".format(pontos))

    time.sleep(0.1)
    if cobra.direction == "right":
        x = cobra.xcor()
        cobra.setx(x + 20)
    elif cobra.direction == "left":
        x = cobra.xcor()
        cobra.setx(x - 20)
    elif cobra.direction == "up":
        y = cobra.ycor()
        cobra.sety(y + 20)
    elif cobra.direction == "down":
        y = cobra.ycor()
        cobra.sety(y - 20)
    if cobra.xcor()>290 or cobra.xcor()<-290 or cobra.ycor()>290 or cobra.ycor()<-290:
        tela.title("Jogo finalizado! Pontuação final: {}".format(pontos))
        cobra.goto(0,0)
        cobra.direction = "stop"
        break
tela.mainloop()
