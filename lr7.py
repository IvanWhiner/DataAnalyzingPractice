import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


'''1. Выбрать данные в соответствии с вариантом и построить двумерные диаграммы
рассеяния с раскраской по классам.
2. Построить диаграммы рассеяния в координатах главных компонент с раскраской по
классам.
3. Построить график зависимости доли объясненной дисперсии от номера главной
компоненты.'''

def lr7():
    #1.Построение диаграмм рассеяния с раскраской по классам
    data = pd.read_excel(io = 'Лабораторная работа 7.xlsx', sheet_name= 10, usecols= 'B:F')
    sns.pairplot(data, hue = 'Класс')
    plt.show()

    #2 Построить диаграммы рассеяния в координатах главных компонент с раскраской по классам
    Y = data['Класс']
    X = data.drop('Класс', axis=1)

    sc = StandardScaler()
    sc.fit(X.astype('float64'))
    Xsc = sc.transform(X.astype('float64'))
    Xsc = pd.DataFrame(Xsc, index=X.index, columns=X.columns)

    skpcamod = PCA().fit(X=Xsc)
    scores_skl = pd.DataFrame(skpcamod.transform(Xsc)[:, :2])
    scores_skl.columns = ['PC1', 'PC2']

    sns.scatterplot(x = 'PC1', y = 'PC2', data = scores_skl, hue = Y )
    plt.title('Диаграммы рассеяния в главных компонентах')
    plt.show()

    #3. Построить график зависимости доли объясненной дисперсии от номера главной компоненты
    pca = PCA(n_components=4)
    pca.fit(X)
    exp_variance1 = pca.explained_variance_ratio_
    sns.lineplot(y = exp_variance1, x = range(4))
    plt.ylabel('Доля обьясненной дисперсии')
    plt.legend(['Для нешкалированных данных'])
    plt.xticks(range(4), [f'PC{i+1}' for i in range(4)])
    plt.show()