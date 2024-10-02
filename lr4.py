import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler
def lr4():
    data = pd.read_excel(io = 'Lr4.xlsx', sheet_name = '10', usecols = [1, 2, 3, 4, 5], names = ['class', 'x1', 'x2', 'x3', 'x4'])
    describe_data = data.describe()
    # print(describe_data)

    #Эмпирические функции распределения
    X = data.drop('class', axis = 1, inplace= False)
    ecdf = sns.ecdfplot(X)
    plt.title('Эмпирические функции распределения')
    plt.show()

    #Ящики с усами и скрипичные диаграммы
    fig, axes = plt.subplots(nrows= 2, ncols= 4, figsize = (17, 8))
    b_plt1 = sns.boxplot(y = data['x1'], data = data, ax = axes[0, 0]).set_title('Ящик с усами для х1')
    b_plt2 = sns.boxplot(y=data['x2'], data=data, ax=axes[0, 1]).set_title('Ящик с усами для х2')
    b_plt3 = sns.boxplot(y=data['x3'], data=data, ax=axes[0, 2]).set_title('Ящик с усами для х3')
    b_plt4 = sns.boxplot(y=data['x4'], data=data, ax=axes[0, 3]).set_title('Ящик с усами для х4')

    violin_plt1 = sns.violinplot(y=data['x1'], data=data, ax=axes[1, 0]).set_title('Скрипичная диаграмма для х1')
    violin_plt2 = sns.violinplot(y=data['x2'], data=data, ax=axes[1, 1]).set_title('Скрипичная диаграмма для х2')
    violin_plt3 = sns.violinplot(y=data['x3'], data=data, ax=axes[1, 2]).set_title('Скрипичная диаграмма для х3')
    violin_plt4 = sns.violinplot(y=data['x4'], data=data, ax=axes[1, 3]).set_title('Скрипичная диаграмма для х4')
    plt.show()

    #Гистограммы
    fig, axes = plt.subplots(ncols = 4, figsize = (17, 4))
    hist1 = sns.histplot(x = data['x1'], ax = axes[0]).set_title('Гистограмма для х1')
    hist2 = sns.histplot(x=data['x2'], ax=axes[1]).set_title('Гистограмма для х2')
    hist3 = sns.histplot(x=data['x3'], ax=axes[2]).set_title('Гистограмма для х3')
    hist4 = sns.histplot(x=data['x4'], ax=axes[3]).set_title('Гистограмма для х4')
    plt.show()


    # Диаграммы рассеяния с указанием класса
    data['class'] = data['class'].astype(str)
    sns.pairplot(data = data, hue = 'class', diag_kind= 'kde', kind= 'scatter', height= 2, plot_kws= {'s': 10})
    plt.show()


    # График двумерной плотности распределения. Пустые графики указывают на то, что два набора данных идентичны
    cols = ['x1', 'x2', 'x3', 'x4']
    fig, axes = plt.subplots(nrows = 4, ncols = 4, figsize = (14, 7))
    for i in range(4):
        for j in range(4):
            if i == j:
                continue
            kde = sns.kdeplot(y = data[cols[i]],
                              x = data[cols[j]],
                              cmap = 'coolwarm',
                              warn_singular= False,
                              ax = axes[i, j]).set_title(f'График двумерной плотности распределения {cols[i]}  от {cols[j]}')
    plt.show()

    #Комбинированные диаграммы

    #Шкалирование данных
    sc = StandardScaler()
    X = X.astype('float64')
    sc.fit(X)
    Xsc = sc.transform(X.astype('float64'))
    Xsc = pd.DataFrame(Xsc, index = X.index, columns = X.columns)
    Xsc['class'] = data['class']
    print(Xsc)

    fig, axes = plt.subplots(1, 4, figsize = (17, 5))
    for i in range(4):
        p = sns.swarmplot(y = f'x{i+1}',
                          hue = 'class',
                          data = Xsc,
                          dodge = True,
                          ax = axes[i])
        pp = sns.boxplot(y = f'x{i+1}',
                         hue = 'class',
                         data = Xsc,
                         showcaps = False,
                         boxprops = {'facecolor': 'None', 'linewidth': 1.5, 'zorder': 10},
                         ax = axes[i],
                         zorder = 10
        )
    plt.show()


