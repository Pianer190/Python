# Задача №10
# print('введите числа ')
# n = int(input())
# k = 0
# for i in range(n):
#     v = int(input())
#     if v == 1:
#         k += 1
# print(k if k<n/2 else n-k)





s, p = (int(input()) for _ in '12')
for x in range(1, 1001):
    y = s -x
    if x <= y and x * y == p:
        print(x, y)
        break

n = int(input())
p = 1
while p * 2 <= n:
     p *= 2
print(p)