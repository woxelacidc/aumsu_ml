import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl


def linear(x):
    w1= 0.5
    w2= -0.5
    y=x*(-(w1/w2))
    return y

if __name__=='__main__':
    #Генерируем множество x-ов
    x_arr = np.arange(-5, 5, 0.1)
    y_arr = []
    #Перебираем все x в нашем массиве иксов, это цикл.
    for x in x_arr:
        #Получаем наш y из x, за счет написанной нами функции
        y = linear(x)
        #добавляем полученный y в массив y-ов
        y_arr.append(y)
    # Строим график
    plt.plot(x_arr, y_arr)
    # Выводим его на экран
    plt.show()
