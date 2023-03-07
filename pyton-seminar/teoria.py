# import random
# ussername =input('введите имя :')
# if ussername == 'Аня':
#  print('Привет Аня')
# elif ussername == 'Вова':
#  print('Hello Вова')
# elif ussername =='Петя':
#  print('Hello may freind')
# else:
#  print('Привет чел', ussername)

# i =0
# while i<5:
#     if i ==2:
#         break
#     i =i+1
# else:
#     print('Пожалуй')
#     print('Хватит')
# print(i)

# Программа котрая находит минимальный делитель числа
# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0:
#         flag = False
#         print(i)
#     elif i > n // 2:
#         print(n)
#         flag = False
#     i +=1

# a ='qwerty'
# for i in a:
#     print(i)


# Задача2
# print('введите трёх значное число')
# a = int(input())
# print(a//100 + a//10%10 + a%10)


# Задача6
# print('Введите номер билета :')
# x =list(map(int,list(input())))
# tiket1 =sum(x[0: -3])
# tiket2 =sum(x[-3:])
# if tiket1 == tiket2:
#     print('yes')
# else:
#     print('NO')


# Задача 4
# print('введите число')
# a = int(input())
# b = int((a/3)*2)
# c = int((b/2)/2)
# s = int(c)
# print(c, b, s)

# Задача8
# n =int(input())
# m =int(input())
# k =int(input())
# area = n * m
# last = area - k
# full_m = k / n
# if full_m == (area - last):
#     print('yes')
# else:
#     print('no')


# функция append добавления значения в конец списка
# list_1 =[1,2]
# print(list_1)
# list_1.append(3)
# print(list_1)
# list_1.append(85)
# print(list_1)

# тренировочная программа  которая добавляет в список значения от 0 до 4 через цикл for
# list_1 =[]
# print(list_1)
# for i in range(5):  #принимает значение от 0 до 4 , можно ввести любую цифру например 10 и в спиок будед добавляться числа от 0 до 9
#     list_1.append(i)
#     print(list_1)


# основные функции которые могут быть в списках :
# удаление последнего элемента
# еденица ознает порядковый номер элемента списка например 1 это 2 в списке
# print(list_1)
# list_1 =[10,2,3,9,-1,0]
# print(list_1.pop(1))

# #Добавлеие элемента в спиоск на нужную позицию
# list_1 =[10,2,3,9,-1,0]
# print(list_1.insert(2,11)) #Принимает 2 аргумента , первый это позиция , второй это значение которое нужно вставить
# print(list_1)


# Срезы
# list_1 =[1,5,6,8,2,3,9,7]
# print(list_1[0]) #Будет выводится первый элемент
# print(list_1[1]) # Будет выводится второй элемент
# print(list_1[-1]) #Будет выводится последний элемент
# print(list_1[:]) #Выводим весь список
# print(list_1[:2]) #Выводим весь список до элемента с номером 2 тоесть до 6
# print(list_1[len(list_1)-2:]) #Выводим два последние 2 элемента  от 9 до 7

# #Кортежи
# t =()

# print(type(t))

# t =(11, 2, 5,)  #Для создания кортежа мы должны оставить в конце запятую
# print(type(t))

# Преобразование списка вы кортеж
# v =[1,5,7]
# print(v)
# print(type(v))
# v =(tuple(v))
# print(v)
# print(type(v))
# a,b,c =v #Множественное присваивание #Разделим картеж на три переменные (Распаковка картежа )
# print(a,b,c)


# t =(1,5,6,4)
# for i in t: # цикл for
#    print(i)

# Можем вывести по другому
# t = (1, 5, 6, 4)
# for i in range(len(t)):
#     print(t[i])


# # Словарь
# d = {}  # Это означает пустой словарь
# d = dict ()  # Это так же словарь

# #Что бы добавить значение , мы должны в нашем слооваре указать ключь и по ключу мы должны написать значение
# d ['q'] = 'qwerty'
# print(d) #Это обозначет что в словаре есть ключ Q который имеет значение qwerty

# #два значения
# d ['q'] = 'qwerty'
# print(d)
# d['w'] ='qwererty1'
# print(d['w']) #В квадратных скобках пишется ключ

# dictionary = {}
# dictionary = {'up': '↑', 'left': '← ', 'down': '↓', 'right': '→'}
# dictionary[895] = 98998
# print(dictionary)

# del dictionary['left']  # Удаление ключа
# for item in dictionary:
# print('{}: {}'.format(item, dictionary[item]))

# Множество
# colors ={ 'red',  'blue', 'green'}
# print(colors)
# colors.add('red')
# print(colors)
# colors.add('grey') #Добавление элемента
# print(colors)
# colors.remove('red') #удаление элемента из множества
# print(colors)
# colors.clear() #удаление всех элементов множества
# print(colors)

# Операции со множеством
# a ={1,2,3,5,8}
# b ={2,5,8,13,21}
# c =a.copy() #Мы можем скопировать в переменную C  из данные из множества a c={1,2,3,5,8}
# u =a.union(b) #Объединение , множество u  будет содержать уникальное значение из множества a и b  u ={1,2,3,5,8,13,21}
# i =a.intersection(b) #Пересечение , множество i будет содержать значения которые есть в обоих множествах i ={8,2,5}
# d1 =a.difference(b) # Из  значения а вычетаются все значения множества b  d1 ={1,3}
# q =a.union(b).difference(a.intersection(b)) #{1,21,3,13}

# Замороженное множество (не можем изменять )
# a ={1,8,6}
# b =frozenset(a)
# print(b)

# Конструктор списков
# Задача , создать список состоящий из  чётных чисел в диапозоне от 1 до 100
# Решение :
# Создать список  чисел от 1 до 100
# list_1 =[]
# for i in range(1,101):
#     list_1.append(i)
#     print(list_1)

# Эту  функцию можно записать так :
# list_1 = [i for i in range(1,101)]
# print(list_1)

# добавить только чётные числа
# list_1 = [i for i in range(1,101) if i % 2 ==0]
# print(list_1) #[2,4,6....,100]

# Допустим вы решили создать пары каждому из чисел (кортежи)
# list_1 = [(i,i) for i in range(1,101) if i %2 ==0]
# print(list_1) #[(2,2), (4,4), ...... ,(100,100)]

# Также можно умножать , делить , прибавлять , вычетать . Например умножить значение на 2 только четные числа
# list_1=[i*2 for i in range(10) if i % 2 ==0]
# print(list_1) #[0,4,8,12,16]

# Определение времени на выполнения операции
import random
import time
import find_numbers 

some_list = [random.randint(1, 1000) for _ in range(10**6)]
some_set = {random.randint(1, 10**9) for _ in range(10**6)}
find_namber = 6
start = time.perf_counter()
print( find_numbers in some_list)
start = time.perf_counter()
print(end - start)
print(find_numbers in some_set)
start = time.perf_counter()
print(end - start)