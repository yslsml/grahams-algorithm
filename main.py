from functions import *

def main():
    plt.ion()  # включение интерактивного режима для анимации

    n = 10
    points = initPoints(n)
    hull = makeHull(points)
    drawPolygon(hull)

    plt.ioff()  # выключение интерактивного режима
    plt.show()

main()