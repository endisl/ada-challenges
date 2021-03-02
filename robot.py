'''
Problema
Um robô é posicionado na posição (0,0) de um espaço onde ele pode se movimentar livremente, inicialmente apontando para a direita.
Em seguida ele recebe um programa que pode ser formado por quatro instruções: "E" que vira o robô no sentido anti-horário em 90 graus, “F” que faz o robô se deslocar uma posição para trás.
O objetivo é, dado um arquivo com uma série de comandos em uma string, calcular a posição final do robô após a execução desta.

Obs: O sistema de coordenadas cresce para a direita e para cima.

Formato de entrada
Uma string s formada por uma sequência de n comandos entre os 4 existentes (“F”, “T”, “E” e “D”).

Obs: Eventualmente a string s de entrada pode conter erros.

Formato de saída
Escrever a posição de saída no formato “(x, y)”. Caso ocorra um erro a saída deve ser apenas um “0”. A saída não deve conter espaços antes ou depois do valor da resposta!

Restrições
O tamanho da string s de entrada é, no máximo, 1000 caracteres.

Exemplo de Entrada 1
FFFF
Exemplo de Saída 1
(4,0)

Exemplo de Entrada 2
DFF
Exemplo de Saída 2
(0,-2)

Explanação dos exemplos
No primeiro caso, o robô se deslocou para frente 4 vezes, e como inicialmente apontava para a direita, sua posição final é (4,0). No segundo caso, ele foi virado 90 graus para direita e deslocado de duas posições, por isso chegou a posição (0,-2) - lembrando que o sistema de coordenadas cresce para cima por isso do valor negativo em y.
'''

# creating an empty list to store the comands
cmds = []

# initializing the variables
x = 0
y = 0

# input the comands
value = input("Commands:")

# checking the restrictions
if len(value) > 1000:
    print(0)
    quit()

for v in value:
    # checking if the comands are valid and appending them into a list
    if v in ['F', 'T', 'D', 'E']:
        cmds.append(v)
    else:
        print(0)
        quit()

# initializing the angle of rotation
angle = 0

# the robot is initiallly at the origin (0,0) and facing x-axis positive
for cmd in cmds:

    # the robot is rotating 90 degrees anticlockwise
    if cmd == 'E':
        if angle == 360:
            angle = 0
        angle = angle + 90

    # the robot is rotating 90 degrees clockwise
    if cmd == 'D':
        if angle == -360:
            angle = 0
        angle = angle - 90

    # the robot is moving forward
    if cmd == 'F':
        if angle == 0:  # on x-axis positive
            x = x+1
        elif angle == 90 or angle == -270:  # on y-axis positive
            y = y+1
        elif angle == 180 or angle == -180:  # on x-axis negative
            x = x-1
        elif angle == 270 or angle == -90:  # on y-axis negative
            y = y-1

    # the robot is moving backward
    if cmd == 'T':
        if angle == 0:  # on x-axis negative
            x = x-1
        elif angle == 90 or angle == -270:  # on y-axis negative
            y = y-1
        elif angle == 180 or angle == -180:  # on x-axis positive
            x = x+1
        elif angle == 270 or angle == -90:  # on y-axis positive
            y = y+1

# printing the final position of the robot
print(f"({x},{y})")
