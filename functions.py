from Point import Point
import random
import matplotlib.pyplot as plt
import numpy as np


def initPoints(n) -> list:
    X = [random.randint(0, 10) for _ in range(n)]
    Y = [random.randint(0, 10) for _ in range(n)]
    points = []
    for i in range(len(X)):
        el = Point(X[i], Y[i])
        for j in range(len(points)):
            if el.equals(points[j]):
                el.x = random.randint(0, 10)
                el.y = random.randint(0, 10)
        points.append(el)
    return points


def determinant(p, p1, p2):  # p относительно p1p2
    return (p2.x - p1.x) * (p.y - p1.y) - (p.x - p1.x) * (p2.y - p1.y)


def xPoints(stack):
    n = len(stack)
    X = []
    for i in range(n):
        X.append(stack[i].x)
    return X


def yPoints(stack):
    n = len(stack)
    Y = []
    for i in range(n):
        Y.append(stack[i].y)
    return Y


def sort(points, S):  # сортировка вставкой
    n = len(points)
    for i in range(2, n):
        j = i
        while j > 1 and (determinant(points[S[j]], points[S[0]], points[S[j - 1]]) < 0):  # P[j] правее P[0]P[j-1]
            S[j], S[j - 1] = S[j - 1], S[j]  # меняем местами номера этих точек
            j -= 1


def findMinPoint(points, S):
    n = len(points)
    for i in range(1, n):
        if points[S[i]].y < points[S[0]].y:
            S[i], S[0] = S[0], S[i]  # меняем местами номера этих точек
    for i in range(1, n):
        if points[S[i]].y == points[S[0]].y:
            if points[S[i]].x < points[S[0]].x:
                S[i], S[0] = S[0], S[i]


def drawPoints(points):
    n = len(points)
    for i in range(n):
        plt.scatter(points[i].x, points[i].y)  # рисует точку
        plt.text(points[i].x + 0.1, points[i].y + 0.1, 'P{}'.format(i))  # имя точки


def drawLines(stack):
    xpoints = np.array(xPoints(stack))
    ypoints = np.array(yPoints(stack))
    plt.plot(xpoints, ypoints, color="orange")


def makeHull(points):
    n = len(points)  # число точек
    S = list(range(0, n))  # список номеров точек

    findMinPoint(points, S)
    sort(points, S)

    stack = [points[S[0]], points[S[1]]]  # создаем стек

    plt.clf()  # очистить текущую фигуру
    drawPoints(points)
    drawLines(stack)
    updateGraphics()  # обновление графика

    for i in range(2, n):
        while determinant(points[S[i]], stack[-2], stack[-1]) < 0:  # правее предыдущей стороны
            del stack[-1]  # pop
            plt.clf()
            drawPoints(points)
            drawLines(stack)
            updateGraphics()
        stack.append(points[S[i]])  # push
        plt.clf()
        drawPoints(points)
        drawLines(stack)
        updateGraphics()
    return stack


def updateGraphics():  # обновление графика
    plt.draw()
    plt.gcf().canvas.flush_events()
    plt.pause(0.4)


def drawPolygon(points: list):
    for i in range(0, len(points)):
        if i + 1 == len(points):
            k = 0  # k - индекс последней точки
        else:
            k = i + 1
        plt.plot([points[i].x, points[k].x], [points[i].y, points[k].y], color="orange")
