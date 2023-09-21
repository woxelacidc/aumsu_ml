import numpy as np


#Функция гиперболического тангенса
def f(x):
    return 2/(1 + np.exp(-x)) - 1

#производная от функции гиперболического тангенса
def df(x):
    return 0.5*(1 + x)*(1 - x)

#Случайный вектор весов скрытого слоя, начальные случайные значения
W1 = np.array([[-0.2, 0.3, -0.4], [0.1, -0.3, -0.4]])

#Случайный вектор весов второго(для выходного слоя) слоя
W2 = np.array([0.2, 0.3])


#Функция, которая пропускает вектор наблюдений через нейронную сеть
def go_forward(inp):
    #для каждого нейрона мы должны запомнить выходные значения.
    sum = np.dot(W1, inp) #Тут мы перемножаем наши входные значения на веса.
    out = np.array([f(x) for x in sum]) #Тут мы пропускаем значения через функцию активации.
    #тут то же, просто для второго слоя, который как бы выходной, для последнего нейрона.
    sum = np.dot(W2, out)
    y = f(sum)
    #Возвращаем сохраненные значения y и out. т.е. выходные значения с нейронов скрытого слоя y и выходного out.
    #
    return (y, out)

def train(epoch):
    global W2, W1
    lmd = 0.01          # шаг обучения
    N = 10000           # число итераций при обучении
    count = len(epoch)  # функция len - вычисляет количество элементов в массиве

    #Прогоняемся по итерациям по обучению, 10 000 раз.
    for k in range(N):
        x = epoch[np.random.randint(0, count)]  # случайных выбор входного сигнала из обучающей выборки
        y, out = go_forward(x[0:3])             # прямой проход по НС и вычисление выходных значений нейронов
        e = y - x[-1]                           # ошибка на последнем нейроне
        delta = e*df(y)                         # локальный градиент
        W2[0] = W2[0] - lmd * delta * out[0]    # корректировка веса первой связи
        W2[1] = W2[1] - lmd * delta * out[1]    # корректировка веса второй связи

        #Локальный градиент для скрытого слоя
        delta2 = W2*delta*df(out)               # вектор из 2-х величин локальных градиентов
        # корректировка связей первого слоя
        W1[0, :] = W1[0, :] - np.array(x[0:3]) * delta2[0] * lmd #для первого нейрона
        W1[1, :] = W1[1, :] - np.array(x[0:3]) * delta2[1] * lmd #для второго нейрона

#Обучающая выборка
epoch = [
    (-1, -1, -1, -1),
    (-1, -1, 1, -1),
    (-1, 1, -1, -1),
    (-1, 1, 1, 1),
    (1, -1, -1, -1),
    (1, -1, 1, 1),
    (1, 1, -1, 1),
    (1, 1, 1, 1),
]


#Запускаем обучение
train(epoch)

#Проверяем результаты
for x in epoch:
    y, out = go_forward(x[0:3]) #[0:3] значит первые 3 элемента мы отправляем в сеть
    print(f"Выходное значение нейронной сети: {y}=>{x[-1]}")
    #x[-1] это последний элемент нашей входной выборке, т.е. то что => это как бы реальный ожидаемый результат
    #а y - это выход нейронной сети и вот мы производим такую проверку.

