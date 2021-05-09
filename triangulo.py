# Programa em python para traçar Triangulos em regiões
# clicadas com o mouse usando Turtle
import turtle

# Método Screen() para gera tela
tela = turtle.Screen()

# Criando o objeto Caneta
caneta = turtle.Turtle()

def triangulo(abs, ord):
    # Movendo a caneta para a região clicada
    caneta.penup()
    caneta.goto(abs, ord)
    caneta.pendown()

    # Realizando 3 movimentos com a caneta: Mover 100 unidades para frente,
    # redirecionar o ângulo para 120 graus à esquerda e mover mais
    # 100 unidades para frente. Resultando em um triângulo
    for i in range(3):
        caneta.forward(100)
        caneta.left(120)
        caneta.forward(100)


# Identificação do clique
turtle.onscreenclick(triangulo, 1)
turtle.listen()

# Manter a janela aberta
turtle.done()