# Programa em python para traçar espirais de Fibonacci
# Espiral fractal usando Turtle
import turtle
import math

def TracFibo(n):
    a = 0
    b = 1
    square_a = a
    square_b = b

    # Definindo coloração da caneta como verde
    x.pencolor("green")

    # Traçando primeiro quadrado
    x.forward(b * fator)
    x.left(90)
    x.forward(b * fator)
    x.left(90)
    x.forward(b * fator)
    x.left(90)
    x.forward(b * fator)

    # Seguindo para o resto da Sequência de Fibonacci
    temp = square_b
    square_b = square_b + square_a
    square_a = temp

    # Traçando o resto dos quadrados
    for i in range(1, n):
        x.backward(square_a * fator)
        x.right(90)
        x.forward(square_b * fator)
        x.left(90)
        x.forward(square_b * fator)
        x.left(90)
        x.forward(square_b * fator)

        # Seguindo a Sequência de Fibonacci
        temp = square_b
        square_b = square_b + square_a
        square_a = temp

    # Trazendo a caneta ao ponto inicial da espiral
    x.penup()
    x.setposition(fator,0)
    x.seth(0)
    x.pendown()

    # Definindo coloração da caneta como azul
    x.pencolor("blue")

    # Traçado da Sequência de Fibonacci
    x.left(90)
    for i in range(n):
        print (b)
        fdwd = (math.pi * b * fator) / 2
        fdwd /=90
        for j in range(90):
            x.forward(fdwd)
            x.left(1)
        temp = a
        a = b
        b = temp + b

# Aqui "fator" é utilizado como o multiplicativo,
# servindo para dimensionar a escala do traçado
# a partir de um certo fator.
fator = 12

# Recebendo o Input para o número de
# Interações que nosso programa rodará
n = int(input("Insira o número de interações Fibonaccis (deve ser maior que 1)"
              ": "))
# Traçando Sequência de Fibonacci Fractal e e printando os
# Números Fibonacci correspondentes
while True:
    if n <= 1:
        n = int(input("O número de interações Fibonaccis deve ser maior que 1,"
                      " por favor, insira novamente: "))
    else:
        print("Sequência de Fibonacci para", n, "elementos: ")
        x = turtle.Turtle()
        x.speed(200)
        TracFibo(n)
        # Manter a janela aberta
        turtle.done()
        break