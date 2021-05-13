# Programa em python para traçar uma árvore fractal
# de 15 ramificações usando Turtle
import turtle
from turtle import *

# Definindo a velocidade de traçado como a mais rápida possível
speed('fastest')

# Redirecionando a caneta para cima
rt(-90)

# O ângulo definido para cada ramificação
angulo = 30

# Função para traçar as ramificações
def config(tamanho, nivel):
    if nivel > 0:
        colormode(255)

        # Definindo a cor magenta (255, 0, 255) como a
        # do último ramo da árvore (as folhas)
        pencolor(255//nivel, 0, 255//nivel)

        # Traçando o tronco da árvore
        fd(tamanho)
        rt(angulo)

        # Função de repetição do caminho da caneta para os proximos ramos
        config(0.8 * tamanho, nivel - 1)
        pencolor(255//nivel, 0, 255//nivel)
        lt(2 * angulo)

        # recursive call for
        # the left subtree
        config(0.8 * tamanho, nivel - 1)

        pencolor(255//nivel, 0, 255//nivel)

        rt(angulo)
        fd(-tamanho)


# Configurando o tamanho do tronco da árvore (80) e a
# quantidade de ramificações por seguimento (15)
config(80, 15)

# Manter a janela aberta após o processo
turtle.done()