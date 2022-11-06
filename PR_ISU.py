from random import randrange as rd
import matplotlib.pyplot as plt


#  функция для рандомной генерации уникальных номеров в списке
def number_generate(numberInSet, numberOfAttribute):
    while numberInSet in setOfCoordinates:
        numberInSet = rd(0, 15)
    setOfCoordinates.add(numberInSet)
    listOfCoordinates[numberInSet][2] = numberOfAttribute
    return numberInSet


#  сам алгоритм А*
def algorithm():
    global x_a, y_a
    # т.к. мы выбираем минимальную f, изначально ставим большую, заведомо недостижимую
    f1 = f2 = f3 = f4 = 10
    g = 0

    x_a_l = 4  # координаты прошлой точки. Нужно для того, чтобы агент не возвращался обратно
    y_a_l = 4  #
    #  координаты финиша в удобной форме
    x_f = listOfCoordinates[finishNumber][0]
    y_f = listOfCoordinates[finishNumber][1]
    #  координаты препятсвий в удобной форме
    x_01 = listOfCoordinates[obstacleNumberList[0]][0]
    y_01 = listOfCoordinates[obstacleNumberList[0]][1]
    x_02 = listOfCoordinates[obstacleNumberList[1]][0]
    y_02 = listOfCoordinates[obstacleNumberList[1]][1]
    x_03 = listOfCoordinates[obstacleNumberList[2]][0]
    y_03 = listOfCoordinates[obstacleNumberList[2]][1]

    #  непосредственно алгоритм
    while x_a != x_f or y_a != y_f:
        #  проверяем, что уже не ходили в эту точку, что в точке нет препятсвия и что точка находили в нашем поле
        #  если точка прошла проверку, считаем функцию f равную манхэттенскому расстоянию + кол-ву пройденых шагов
        #  точка слева от А
        if ((x_a - 1 != x_a_l) or (y_a != y_a_l)) and ((x_a - 1 != x_01) or (y_a != y_01)) and (
                (x_a - 1 != x_02) or (y_a != y_02)) and (
                (x_a - 1 != x_03) or (y_a != y_03)) and 3 >= x_a - 1 >= 0:
            f1 = g + abs(x_a - x_f - 1) + abs(y_a - y_f)
        #  точка снизу от А
        if ((x_a != x_a_l) or (y_a - 1 != y_a_l)) and ((x_a != x_01) or (y_a - 1 != y_01)) and (
                (x_a != x_02) or (y_a - 1 != y_02)) and (
                (x_a != x_03) or (y_a - 1 != y_03)) and 3 >= y_a - 1 >= 0:
            f2 = g + abs(x_a - x_f) + abs(y_a - y_f - 1)
        #  точка справа от А
        if ((x_a + 1 != x_a_l) or (y_a != y_a_l)) and ((x_a + 1 != x_01) or (y_a != y_01)) and (
                (x_a + 1 != x_02) or (y_a != y_02)) and (
                (x_a + 1 != x_03) or (y_a != y_03)) and 3 >= x_a + 1 >= 0:
            f3 = g + abs(x_a - x_f + 1) + abs(y_a - y_f)
        #  точка сверху от А
        if ((x_a != x_a_l) or (y_a + 1 != y_a_l)) and ((x_a != x_01) or (y_a + 1 != y_01)) and (
                (x_a != x_02) or (y_a + 1 != y_02)) and (
                (x_a != x_03) or (y_a + 1 != y_03)) and 3 >= y_a + 1 >= 0:
            f4 = g + abs(x_a - x_f) + abs(y_a - y_f + 1)
        f = min(f1, f2, f3, f4)  # выбираем минимальную f
        if f1 == f2 == f3 == f4:  # если все f равны, найти путь невозможно
            print("невозможно найти оптимальный путь")
            break
        if f1 > 50 or f2 > 50 or f3 > 50 or f4 > 10:
            print("невозможно найти оптимальный путь")
            break
        # идем в точку с минимальной f
        if f == f1:
            x_a_l = x_a
            y_a_l = y_a
            x_a = x_a - 1
            y_a = y_a
        elif f == f2:
            x_a_l = x_a
            y_a_l = y_a
            x_a = x_a
            y_a = y_a - 1
        elif f == f3:
            x_a_l = x_a
            y_a_l = y_a
            x_a = x_a + 1
            y_a = y_a
        elif f == f4:
            x_a_l = x_a
            y_a_l = y_a
            x_a = x_a
            y_a = y_a + 1

        print(x_a, y_a)
        plt.text(x_a, y_a, '●', fontstretch='expanded', color='b')
        g += 1
        f1 = f2 = f3 = f4 = 10


def draw(title, suptitle):
    #  задаем границы рисунка
    plt.xlim([-0.5, 3.5])
    plt.ylim([-0.5, 3.5])
    #  делаем сетку
    for x_dot in range(-5, 36, 10):
        plt.vlines(x_dot / 10, -0.5, 3.5, color='k')

    for y_dot in range(-5, 36, 10):
        plt.hlines(y_dot / 10, -0.5, 3.5, color='k')

    plt.axis('off')
    plt.title(title)
    plt.suptitle(suptitle, size = 'small')
    # рисуем точки
    for dot in range(16):
        if listOfCoordinates[dot][2] == 1:
            plt.text(listOfCoordinates[dot][0], listOfCoordinates[dot][1], "A", fontsize='xx-large', color='b')
        if listOfCoordinates[dot][2] == 2:
            plt.text(listOfCoordinates[dot][0], listOfCoordinates[dot][1], "■")
        if listOfCoordinates[dot][2] == 3:
            plt.text(listOfCoordinates[dot][0], listOfCoordinates[dot][1], "F", color='r', fontsize='xx-large',
                     verticalalignment='bottom')
    plt.show()


# генерируем список, множество и переменные
# в listOfCoordinates будут хранится координаты точек и атрибут в формате (x, y, attribute)
# setOfCoordinates нужен, чтобы координаты при рандомном генерировании не повторялись
listOfCoordinates = []
setOfCoordinates = set()
x = 0
y = 0
attribute = 0

# генерируем координаты точек в листе, атрибут всем точкам даем по умолчанию - 0
while len(listOfCoordinates) < 16:
    listOfCoordinates.append([x, y, attribute])
    x += 1
    if x == 4:
        x = 0
        y += 1

# генерируем агента, его атрибут - 1
agentNumber = rd(0, 15)  # генерируем номер агента в сете
agentNumber = number_generate(agentNumber, 1)

# генерируем препятсвия, их атрибут - 2
obstacleNumber = rd(0, 15)
obstacleNumberList = []
i = 0
while i < 3:
    obstacleNumber = number_generate(obstacleNumber, 2)
    i += 1
    obstacleNumberList.append(obstacleNumber)

# генерируем финиш, его атрибут - 3
finishNumber = rd(0, 15)
finishNumber = number_generate(finishNumber, 3)

#  координаты агента в удобной форме
x_a = listOfCoordinates[agentNumber][0]
y_a = listOfCoordinates[agentNumber][1]

print("Координаты точек оптимального пути:")
draw('Сгенерированное поле', 'чтобы продолжить закройте окно')

algorithm()
draw('Оптимальный путь, отмечен синими точками', '')