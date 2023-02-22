#Задача2
print('введите трёх значное число')
a = int(input())
print(a//100 + a//10%10 + a%10)


#Задача 4
print('введите число')
a = int(input())
b = int((a/3)*2)
c = int((b/2)/2)
s = int(c)
print(c, b, s)



#Задача6
print('Введите номер билета :')
x =list(map(int,list(input())))
tiket1 =sum(x[0: -3])
tiket2 =sum(x[-3:])
if tiket1 == tiket2:
     print('yes')
else:
     print('NO')


#Задача8
n =int(input())
m =int(input())
k =int(input())
area = n * m
last = area - k
full_m = k / n
if full_m == (area - last):
     print('yes')
else:
     print('no')
