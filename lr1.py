import numpy as np
import matplotlib.pyplot as plt
def lr1():
    #Задание 2. Точки в виде строк
    p1 = [[1,3],[1,1],[3,3],[3,1]]
    p2 = [[4,3],[4,1],[6,3],[6,1]]

    #Функция чтобы постоянно plot(arr[,: 0], ....) не писать
    def plot(arr):
        plt.plot(arr[:, 0], arr[:, 1])

    #Задание 3. Матрицы
    p1 = np.array(p1)
    p2 = np.array(p2)
    #Задание 4. Вывод в виде рисунка
    plot(p1)
    plot(p2)
    plt.show()

    #Задание 5. отражение относительно ОХ
    #Матрица отражения
    r = [[1, 0], [0, -1]]
    r = np.array(r)

    p1_r = np.matmul(p1, r)
    p2_r = np.matmul(p2, r)
    plot(p1)
    plot(p1_r)
    plot(p2)
    plot(p2_r)
    plt.show()

    #Задание 5. Поворот

    #
    def turn(angle):
        angle = np.radians(angle)
        c = np.cos(angle)
        s = np.sin(angle)
        q = [[c, s], [-s, c]]
        return q

    #Поворот на 120 градусов
    p1_t120 = np.matmul(p1, turn(120))
    p2_t120 = np.matmul(p2, turn(120))

    #Поворот на 240 градусов
    p1_t240 = np.matmul(p1, turn(240))
    p2_t240 = np.matmul(p2, turn(240))

    #Увеличение в 5 раз по каждой оси и поворот 5 раз на 60
    in5 = np.array([[5, 0], [0,5]])
    p1_in5 = np.matmul(p1, in5)
    p2_in5 = np.matmul(p2, in5)


    plot(p1_t120)
    plot(p2_t120)
    plot(p1_t240)
    plot(p2_t240)
    for k in range(5):
        pr1 = np.matmul(p1_in5, turn(k * 60))
        pr2 = np.matmul(p2_in5, turn(k * 60))
        plot(pr1)
        plot(pr2)
    plt.show()

    #Задание 7.

    #Матрица на которую умножаем
    a = np.array([[-1, 1], [4, 0]])
    #Обратная ей матрица
    a_1 = np.linalg.inv(a)

    #Умножение на матрицу
    p1 = np.matmul(p1, a)
    p2 = np.matmul(p2, a)
    plot(p1)
    plot(p2)

    #цПроверка
    p1 = np.matmul(p1, a_1)
    p2 = np.matmul(p2, a_1)
    plot(p1)
    plot(p2)
    plt.show()