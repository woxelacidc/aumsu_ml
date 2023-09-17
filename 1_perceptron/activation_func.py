import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

def stepFunc(x):
    if x >= 0:
        return 1
    if x < 0:
        return -1



if __name__=='__main__':
    #Генерируем множество x-ов
    x_arr = np.arange(-5, 5, 0.1)
    y_arr = []
    #Перебираем все x в нашем массиве иксов, это цикл.
    for x in x_arr:
        #Получаем наш y из x, за счет написанной нами функции
        y = stepFunc(x)
        #добавляем полученный y в массив y-ов
        y_arr.append(y)
    # Строим график
    plt.plot(x_arr, y_arr)
    # Выводим его на экран
    plt.show()






