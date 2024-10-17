import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats


'''Две категории данных из файла Volgmed_2013.xls
(конкретные категории и данные выбрать в соответствии с вариантом)подвергнуть
А/В тестированию:
сравнить количество пропусков данных на основании точного теста
Фишера;
очистить от выбросов и пропусков и сравнить с помощью t-теста
Уэлча;
сравнить очищенные от выбросов и пропусков категории с помощью U-теста Манна—Уитни.
Для каждого теста сформулировать, в какую сторону отличаются
категории и с каким пи-значением.
Вывести графики гистограмм и эмпирических функций распределения очищенных данных по категориям.

Вариант 10. Становая сила юношей/девушек первого курса.
'''

def lr6():
    #Считываем данные, выбираем 1 курс, удаляем столбец с курсом
    data = pd.read_excel(io = 'Volgmed_2013.xlsx', header=None, skiprows=2, usecols = [1, 4, 17])
    data = data[data[4] == 1]
    data = data.drop(4, axis = 1)

    # print(data[1].unique())

    #Создаем два dataframe один для парней, другой для девушек, удаляем столбец с полом
    data_m = data[(data[1] == 'муж') | (data[1] == 'муж.')]
    data_m = data_m.drop(1, axis=1)
    data_w = data[(data[1] == 'жен') | (data[1] == 'жен.')]
    data_w = data_w.drop(1, axis=1)

    print('Группа 1 — парни, Группа 2 — девушки')

    #Тест фишера
    na_count_m = np.sum(pd.isna(data_m.to_numpy()))
    na_count_w = np.sum(pd.isna(data_w.to_numpy()))

    table = np.array([[len(data_m) - na_count_m, na_count_m],
                     [len(data_w) - na_count_w, na_count_w]])
    print('Тест Фишера по пропускам. Статистика {:}, pi-значение {:}'.format(stats.fisher_exact(table).statistic, stats.fisher_exact(table).pvalue))
    print('В группе 1 пропуска появляются реже чем в группе 2')

    #Очистка от пропусков
    data_m[17] = pd.to_numeric(data[17], errors='coerce')
    data_m.dropna(inplace=True)

    data_w[17] = pd.to_numeric(data[17], errors='coerce')
    data_w.dropna(inplace=True)


    #Очистка от выбросов
    Q1 = data_m[17].quantile(0.25)
    Q3 = data_m[17].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    data_m = data_m[(data_m[17] < upper_bound) & (data_m[17] > lower_bound)]

    Q1 = data_w[17].quantile(0.25)
    Q3 = data_w[17].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    data_w = data_w[(data_w[17] < upper_bound) & (data_w[17] > lower_bound)]

    # print(data_m)
    # print(data_w)

    # Сравнение с помощью t-теста Уэлча
    ttest = stats.ttest_ind(data_m, data_w, equal_var=False)
    print('t-тест Уэлча {:}, p-значение {:}'.format(float(ttest.statistic), float(ttest.pvalue)))
    print('Мат ожидание группы 1 больше чем у группы 2')


    #U-тест Манна—Уитни
    utest = stats.mannwhitneyu(data_m, data_w)
    print('U-тест Манна—Уитни {:}, p-значение {:}'.format(float(utest.statistic), float(utest.pvalue)))
    print('Медиана группы 1 больше чем у группы 2')

    ax = sns.ecdfplot(data_m)
    ax.axes.set_yticks(np.arange(start=0, stop=1.1, step=0.1))
    ax.grid()
    plt.show()
    sns.histplot(data_m, bins=35, kde=False, stat="density")
    plt.show()

    ax = sns.ecdfplot(data_w)
    ax.axes.set_yticks(np.arange(start=0, stop=1.1, step=0.1))
    ax.grid()
    plt.show()
    sns.histplot(data_w, bins=35, kde=False, stat="density")
    plt.show()