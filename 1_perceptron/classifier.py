import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl



if __name__=='__main__':
    #У нас будет по 5 событий, т.е. 5 для типа С1, и 5 для типа С2.
    N = 5

    #используя библиотеку random делаем список из 5ти элементов
    x1= np.random.random(N)
    # x2=x1 + случайное отклонение
    #Благодаря такому ходу и x1 и x2 будут лежать выше нашей прямой.
    x2= x1+ [np.random.randint(10)/10 for i in range(N)]
    #на данный момент у нас x1 это массив из 5 элементов
    #и x2 массив из 5 элементов, теперь мы сделаем двумерный массив
    #В пайтоне это просто:
    C1=[x1,x2]

    #Теперь генерируем точки C2 похожим образом
    x1 = np.random.random(N)
    #Тут дополнительный -0.1 потому что при x<0 у нас должен получаться
    #наш случай C2:
    x2 = x1- [np.random.randint(10)/10 for i in range(N)] - 0.1
    C2 = [x1, x2]

    #Далее формируем прямую под 45 градусов, чтобы ее видеть
    f = [0, 1]

    #Далее задаем веса для нашей нейронной сети
    w = np.array([-0.5, 0.5])

    #Теперь проводим наши точки по нашей классифицирующей нейронной сети.

    for i in range(N):
        x = np.array([C2[0][i], C2[1][i]])
        y = np.dot(w, x)
        if y>= 0:
            print("С1")
        else:
            print("C2")
    # также мы хотим, чтобы эти точки подсвечивались на нашей
    #плоскости, желательно разными цветами
    plt.scatter(C1[0][:], C1[1][:], s=10, c='red')
    plt.scatter(C2[0][:], C2[1][:], s=10, c='blue')
    plt.plot(f)
    plt.grid(True)
    plt.show()

