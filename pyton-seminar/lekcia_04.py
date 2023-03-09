# Функция это фрагмент программы используемый многократно , любая функция или процедура обозначется в одну функцию и обзначается как def .
# Задача НЕобходимо создать функцию sumnambers , которая будет считать сумму всех элементов от 1 до n
# Решение :

# def sum_nambers(n):
#     summa = 0
#     for i in range(1, n+1):

#         summa += i
#     print(summa)
# sum_nambers(5)
...
# def sum_nambers(n):
#     summa = 0
#     for i in range(1, n+1):

#         summa += i
#     return summa
# print (sum_nambers(5))
...

# def sum_nambers(n,y = 'hello'):
#      print(y)
#      summa = 0
#      for i in range(1, n+1):

#          summa += i
#      return summa

# a =sum_nambers(5, 'qwerty') #Если мы передаем функции аргумент , то значение берётся по умолчанию
# print(a)

...
# Мы хотим передать функции множемство букв и получить единое слово , но мы не знаем сколько имеенно будет букв тоесть аргументов

# def sum_str(*args):
#     res = ''
#     for i in args:
#         res += i
#     return res
# print(sum_str('q', 'w', 'e', 'r','t','y'))
# print(sum_str('p', 'r', 'i', 'v','e','t'))
...

# Модули  что бы вызвать функцию из другого файлика мы должны импортировать этот модуль , затем обратиться к нашему модулю
# import modul1
# Print(modul1.max1(5,9))

# #Метод 2
# from modul1 import max1
# print(max1(10,9))

# Если вы хотите импортировать все функции то нужно сделать так
# from modul1 impor *
# print(max1(10,9))

# Рекурсия
# Пользователи вводят число n и требуется вывести n первых чисел последовательности фебаначи (каждый член происходит путём суммирования двух пред идущих)


# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n-1) + fib(n-2)
# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1)
#[1, 1, 2, 3, 5, 8, 13, 21, 34]
#вывод (0+1=1 1+1=2) 1+2=3 <- это число фибаначи  (3+2=5 , 5+3=8) восьмёрка это число фебаначи  (8+5=13 8+13=21) 13 это число фебанчи 

#Алгоритмы 
#Алгоритм сортировки 
#Быстрая сортировка 
# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]   
#     greater = [i for i in array[1:] if i > pivot] 
#     return quick_sort(less) + [pivot] + quick_sort(greater)
# print(quick_sort([14,5,9,6,3,58,7,5,2,7]))
#Результат [2, 3, 5, 5, 6, 7, 7, 9, 14, 58]
