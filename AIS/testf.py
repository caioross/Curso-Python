
import turtle
import random
import time

tela = turtle.Screen()
tela.title("Jogo da Cobrinha - Nokia3310")

pontos = 0
tela.bgcolor("black")
tela.setup(width=600, height=600)

tela.tracer(0)

cobra = turtle.Turtle()  # jogador
cobra.speed(0)
cobra.shape("square")
cobra.color("violet")
cobra.penup()
cobra.goto(0, 0)
cobra.direction = 'stop'

fruta = turtle.Turtle()
fruta.speed(0)
fruta.shape("circle")
fruta.color("green")
fruta.penup()
fruta.goto(0, 100)

def cima():
    cobra.direction = 'up'

def baixo():
    cobra.direction = 'down'

def direita():
    cobra.direction = 'right'

def esquerda():
    cobra.direction = 'left'

# fazer a cobra me obedecer
tela.listen()
tela.onkeypress(cima, "Up")
tela.onkeypress(baixo, "Down")
tela.onkeypress(direita, "Right")
tela.onkeypress(esquerda, "Left")

# o coração do app está aqui

while True:
    tela.update()

    if cobra.distance(fruta) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        fruta.goto(x, y)
        pontos += 10
        tela.title(f'Pontos: {str(pontos)}')

    time.sleep(0.1)

    if cobra.direction == "left":
        x = cobra.xcor()
        cobra.setx(x - 20)

    elif cobra.direction == "right":
        x = cobra.xcor()
        cobra.setx(x + 20)

    elif cobra.direction == "down":
        y = cobra.ycor()
        cobra.sety(y - 20)

    elif cobra.direction == "up":
        y = cobra.ycor()
        cobra.sety(y + 20)

    if cobra.xcor() > 290 or cobra.xcor() < -290 or cobra.ycor() > 290 or cobra.ycor() < -290:
        tela.title(f"GAME OVER! Pontuação Final: {str(pontos)}")
        cobra.goto(0, 0)
        cobra.direction = "stop"
        break

# até aqui!!
tela.mainloop()
