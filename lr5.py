import PyPDF2
import re

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import randint, geom, logser

'''
Вариант 10. Найти все интервалы (по количеству знаков) между буквами «ж» в повести А. И. Солженицына «Матренин двор».
Аппроксимировать
равномерным на целых числах (randint),
геометрическим (geom),
логарифмическим (logser) распределением.
Вывести вероятности для полученных аппроксимаций вместе с гистограммой,
посчитать среднее значение логарифмической функции правдоподобия.
'''
def lr5():
    #Считываем файл
    pdf_path = 'Matr_Dvor.pdf'
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text() + '\n'  # Добавляем текст с каждой страницы

    #Ищем индексы буквы, затем считаем интервалы
    positions = [m.start() for m in re.finditer('ж', text)]
    intervals = [positions[i + 1] - positions[i] for i in range(len(positions) - 1)]


    #Строим гистограмму и целочисленное распределение
    sns.histplot(intervals, stat='density')
    C = range(max(intervals) + 1)
    plt.plot(C, randint.pmf(C, min(intervals), max(intervals)), color='red')
    plt.show()

    #Значение логарифма правдоподобия
    u = sum(randint.logpmf(intervals, min(intervals), max(intervals) + 1)) / len(intervals)
    print('Среднее значение логарифма правдоподобия {:.3}'.format(u))

    #Геометрическое распределение и логарифм правдоподобия
    sns.histplot(intervals, stat='density')
    p = 1 / np.mean(intervals)
    C = range(max(intervals)+1)
    plt.plot(C, geom.pmf(C, p), color='red')
    plt.show()

    u = sum(geom.logpmf(intervals, p)) / len(intervals)
    print('Среднее значение логарифма правдоподобия {:.3}'.format(u))

    # Логарифмическое распределение и логарифм правдоподобия
    sns.histplot(intervals, stat='density')
    p = 1 - (np.mean(intervals)-1)/np.mean(intervals)
    C = range(1, max(intervals) + 1)
    plt.plot(C, logser.pmf(C, p), color='red')
    plt.show()

    u = sum(logser.logpmf(intervals, p)) / len(intervals)
    print('Среднее значение логарифма правдоподобия {:.3}'.format(u))
