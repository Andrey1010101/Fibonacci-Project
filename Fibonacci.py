q = [0, 1, 1]
n = -1
w = []

def spisok(f1 = 1, f2 = 1):
    global q
    
    for i in range(0, n-3):
        f1, f2 = f2, f1 + f2
        q.append(f2)
    return q

def chet(x = 0):
    global q
    global w
    for i in q:
        if i % 2 == 0 and i > 0:
            w.append(i)
    print(w)
    print('\n1- вернуться; \
    \n2- показать только не чётные числа;\
    \n3- записать числовую последовательновст в фаил .txt;\
    \n4- Завершить работу;\n')
    while True:
        try:
            x = int(input('Ввод: '))
            if x == 1:
                print(q)
                work()
                break
            elif x == 2:
                nochet()
                break
            elif x == 3:
                with open("Fibonacci.txt", "w") as file:
                    file.write('\nЧисловая последовательность Фибоначчи (только чётные элементы) ' + str(w))
                    print('\nпоследовательность элементов записана!\
                           \n1- вернуться; \
                           \n2- показать только не чётные числа;\
                           \n3- записать числовую последовательновст в фаил .txt;\
                           \n4- Завершить работу;\n')
            elif x == 4:
                break
            elif x > 4 or x < 1:
                print('Вы ввели несуществующее значение!!!')
        except ValueError:
            print('Вы ввели не число!!!')

def nochet():
    global w
    global q
    for i in q:
        if i % 2 != 0:
            w.append(i)
    print(w)


def work(x = 0):
    global q
    print('\nПриступим к работе с числовой последовательностью Фибоначчи.\
          \nВведите номер действия для выполнения: \
          \n1- показать только чётные числа; \
          \n2- показать только не чётные числа; \
          \n3- записать числовую последовательновст в фаил .txt\
          \n4- Завершить работу;\n')
    while True:
        try:
            x = int(input('Ввод: '))
            if x == 1:
                chet()
                break
            elif x == 2:
                nochet()
                break
            elif x == 3:
                with open("Fibonacci.txt", "w") as file:
                    file.write('\nЧисловая последовательность Фибоначчи ' + str(q))
                    print('\nпоследовательность элементов записана!\
                          \n1- показать только чётные числа; \
                          \n2- показать только не чётные числа;\
                          \n3- записать числовую последовательновст в фаил .txt;\
                          \n4- Завершить работу;\n')
            elif x == 4:
                break
            elif x > 4 or x < 1:
                print('Вы ввели несуществующее значение!!!')
        except ValueError:
            print('Вы ввели не число!!!')

while n < 0:
    try:
        n = int(input('Сколько элементов числовой последовательности Фибоначчи вывести на экран?\n'))    

        if n > 3:
            print(spisok())
        elif n == 1:
            print(q[0])
        elif n == 2:
            print(q[0], q[1])
        elif n == 3:
            print(q[0], q[1], q[2])
        elif n < 0:
            print('Вы ввели отрицательное число!!!')
        

    except ValueError:
        print('Вы ввели не число!!!')
work()
