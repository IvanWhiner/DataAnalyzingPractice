import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def lr3():
    data = pd.read_excel('Volgmed_2013.xlsx', header=1)
    data = data[['Курс','Становая сила, кг','Вес, кг','Экскурсия грудной клетки, см', 'Пол']]

    for col in ['Курс','Становая сила, кг','Вес, кг','Экскурсия грудной клетки, см']:
        data[col] = pd.to_numeric(data[col], errors='coerce')

    data = data.dropna(subset=['Курс','Становая сила, кг','Вес, кг','Экскурсия грудной клетки, см', 'Пол'])

    data_filt = data[(data['Курс'] == 1) & (data['Пол'] == 'жен') & (data['Становая сила, кг'] > 50)]
    print(data_filt)

    plt.scatter(data['Вес, кг'], data['Экскурсия грудной клетки, см'])
    plt.xlabel('Вес')
    plt.ylabel('Экскурсия грудной клетки')
    plt.show()