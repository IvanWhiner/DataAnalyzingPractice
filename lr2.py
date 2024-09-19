import numpy as np
import matplotlib.pyplot as plt


points = [[13.44, 0.75],
          [13.56, 1.78],
          [12.22, 2.65],
          [10.87, 3.23],
          [8.98, 3.13],
          [7.66, 2.39]]

points = np.array(points)
def lr2():
    t = np.linspace(0, 2 * np.pi, num = 5000)
    x = 9 + np.sqrt(2)*np.cos(t)
    y = 1 + np.sqrt(2)*np.sin(t)
    plt.scatter(points[:, 0], points[:,1])
    plt.plot(x, y)
    plt.show()

    R = np.zeros((len(x), 6))
    r = np.zeros(len(x))
    sum_kv = np.zeros(len(x))
    for j in range(len(x)):
        sum_kv[j] = 0
        for i in range(6):
            R[j, i] = ((x[j] - points[i, 0]) ** 2 + (y[j] - points[i, 1]) ** 2) ** 0.5
        r[j] = np.mean(R[j, :])
        for i in range(6):
            sum_kv[j] += (R[j, i] - r[j]) ** 2

    plt.plot(x, sum_kv)
    plt.grid()
    plt.show()

    def goldenRatio(a, b, eps=1e-8):
        phi = (1 + np.sqrt(5)) / 2
        resphi = 2 - phi

        x1 = a + resphi * (b - a)
        x2 = b - resphi * (b - a)
        f1 = sum_kv[int(x1)]
        f2 = sum_kv[int(x2)]

        while abs(a - b) > eps:
            if f1 < f2:
                b = x2
                x2 = x1
                f2 = f1
                x1 = a + resphi * (b - a)
                f1 = sum_kv[int(x1)]
            else:
                a = x1
                x1 = x2
                f1 = f2
                x2 = b - resphi * (b - a)
                f2 = sum_kv[int(x2)]

        return (a + b) / 2

    result = int(goldenRatio(0, x.size - 1))
    X_center = round(x[result], 3)
    Y_center = round(y[result], 3)
    radius = round(r[result], 3)

    plt.axis('equal')
    plt.grid()
    plt.plot(x, y)
    plt.scatter(points[:, 0], points[:, 1])
    plt.scatter(X_center, Y_center)
    plt.gca().add_patch(plt.Circle((X_center, Y_center), radius, fill=False))

    plt.show()
