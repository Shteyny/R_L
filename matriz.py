from random import randint, choice
import time
import polya


cletchatka = {0: [polya.Clet],
              1: [polya.Evac, polya.Block, polya.Clet, polya.Clet, polya.Clet, polya.Block, polya.Clet, polya.Clet, polya.Clet, polya.Block, polya.Clet, polya.Clet, polya.Clet, polya.Block, polya.Clet, polya.Clet, polya.Clet, polya.Block, polya.Clet, polya.Clet, polya.Clet, polya.Block, polya.Clet, polya.Clet, polya.Clet, polya.Block, polya.Clet, polya.Clet, polya.Clet,],
              2: [polya.Evac]}



def level_create(nach, end, matriz2, her, screen):
    levelspis = []
    for i in range(len(matriz2)):
        line = []
        for j in range(len(matriz2[i])):
            try:
                line.append(choice(cletchatka[matriz2[i][j]])(her, (j, i), screen))
            except KeyError:
                return sozd(nach, end, her, screen)
        levelspis.append(line)
    return levelspis




def pris(end, matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j].append(max([abs(j - end[0]), abs(i - end[1])]))
    return matriz


def poisk_crat(nach, end, matriz, her, screen):
    matriz = pris(end, matriz)
    phantom = []
    for i in range(len(matriz)):
        phantom.append([])
        for z in range(len(matriz[0])):
            phantom[i].append(1)
    phantom[nach[1] - 1][nach[0] - 1] = 0
    phantom[end[1] - 1][end[0] - 1] = 2
    finding = True
    pos = [nach[0] - 1, nach[1] - 1]
    timer = time.time()
    while finding:
        min = [1000, pos]
        if pos[1] - 1 >= 0 and phantom[pos[1] - 1][pos[0]] != 0:
            summ = matriz[pos[1] - 1][pos[0]][1] + matriz[pos[1] - 1][pos[0]][0]
            if pos[1] - 1 >= end[1] - 1:
                summ -= 30
            if min[0] >= summ:
                min[0] = summ
                min[1] = [pos[0], pos[1] - 1]
        if pos[1] + 1 <= 7 and phantom[pos[1] + 1][pos[0]] != 0:
            summ = matriz[pos[1] + 1][pos[0]][1] + matriz[pos[1] + 1][pos[0]][0]
            if pos[1] + 1 <= end[1] - 1:
                summ -= 30
            if min[0] >= summ:
                min[0] = summ
                min[1] = [pos[0], pos[1] + 1]
        if pos[0] - 1 >= 0 and phantom[pos[1]][pos[0] - 1] != 0:
            summ = matriz[pos[1]][pos[0] - 1][1] + matriz[pos[1]][pos[0] ][0]
            if pos[0] - 1 >= end[0] - 1:
                summ -= 30
            if min[0] >= summ:
                min[0] = summ
                min[1] = [pos[0] - 1, pos[1]]
        if pos[0] + 1 <= 9 and phantom[pos[1]][pos[0] + 1] != 0:
            summ = matriz[pos[1]][pos[0] + 1][1] + matriz[pos[1]][pos[0] + 1][0]
            if pos[0] + 1 <= end[0] - 1:
                summ -= 30
            if min[0] >= summ:
                min[0] = summ
                min[1] = [pos[0] + 1, pos[1]]
        if pos == [end[0]-1, end[1]-1]:
            finding = False
        phantom[pos[1]][pos[0]] = 0
        pos = min[1]
        if time.time() - timer > 0.25:
            return sozd(nach, end, her, screen)
    phantom[end[1] - 1][end[0] - 1] = 2
    return phantom

def sozd(nach, end, her, screen):
    matriz1 = []
    for i in range(8):
        line = []
        for j in range(10):
            line.append([randint(1, 100)])
        matriz1.append(line)
    way = (poisk_crat(nach, end, matriz1, her, screen))
    return level_create(nach, end, way, her, screen)

#Формировать от первой свободной клетки. 1. Столбцы и Строчки не могут быть полностью заполненны единицами. 2. "0" имеет по соседству как минимум ещё 2 нуля
