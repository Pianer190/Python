 #  Задача 16.  Вычслить сколько раз встречается некоторое число X в массиве .
 # Пример
 # 5
 # 1 2 3 4 5
 # 3
 # Вывод
 # 1
input()
lst = map(int, (input().split()))
n = int(input())
inc = 0
for i in lst:
        if i == n:
            inc += 1
print(inc)


# Задача 18 Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
N = int(input())
a = [int(input()) for i in range(N)]
x = int(input())
b = [abs(a[i]-x) for i in range(len(a))]
print(a[b.index(min(b))])


# Задача 20: Напишите программу, которая вычисляет стоимость введенного пользователем слова.
import re
s = input()
d = {'[AEIOULNSTR]': '1', '[DG]': '2', '[BCMP]': '3',
     '[FHVWY]': '4', 'K': '5', '[JX]': '8', '[QZ]': '19'}
for k in d:
    s = re.sub(k, d[k], s)
print(sum(map(int, s)))
