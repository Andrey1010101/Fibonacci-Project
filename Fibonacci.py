import os

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
    print('Введите номер действия для выполнения: \
          \n1- записать значения в .txt; \
          \n2- вернуться к работе с общим списком значений;')
    r = input()
    if r == 1:
        zapis()
    elif r == 2:
        print(q)
        work()

def nochet():
    global w
    global q
    for i in q:
        if i % 2 != 0:
            w.append(i)
    print(w)
    de()
    
def de():
    print('Введите номер действия для выполнения: \
          \n1- записать значения в .txt; \
          \n2- вернуться к работе с общим списком значений;')
    
    r = input()
    if r == 1:
        zapis()
    elif r == 2:
        print(q)
        work()
   

def zapis():        
    z = open('F.txt', 'w')
    z.write('w')
    z.close()
    print(ok)


def work(x = 0):
    global q
    print('Приступим к работе с числовой последовательностью Фибоначчи.\
          \nВведите номер действия для выполнения: \
          \n1- показать только чётные числа; \
          \n2- показать только не чётные числа; \
          \n3- записать числовую последовательновст в фаил .txt')
    x = int(input())
    if x == 1:
        chet()
    elif x == 2:
        nochet()
    elif x == 3:
        z = open('F.txt', 'w')
        z.write.(q)
        z.close()
        print(ok)
        
    

        


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
