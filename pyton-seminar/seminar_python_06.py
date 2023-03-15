#Задача 30
arr=[]
a1=int(input('введите первый элемент'))
d=int(input('введите разность d'))
n=int(input('введите колличество элементов'))
for i in range(1,n+1):
     arr.append(a1+d*(i-1))
print(arr)



#Задача 32
import random
arr = []
for i in range(20):
	x = int(random.random()*10)  
	arr.append(x)
	print("%3d" % x, end='')
	if (i+1) % 10 == 0:	print()
 
minimum = int(input('min: '))
maximum = int(input('max: '))
 
index = []
i = 0
for i in arr:
	if minimum <= i <= maximum:
		index.append(arr.index(i))
print("Количество: ", len(index))
print("Индексы: ", index)
