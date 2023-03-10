###################Задача 22###################
n = int(input("Введите количество элементов первого множества: "))
set_a = set()
for i in range(n):
    set_a.add(int(input(f"Введите {i+1}-й элемент первого множества: ")))

m = int(input("Введите количество элементов второго множества: "))
set_b = set()
for i in range(m):
    set_b.add(int(input(f"Введите {i+1}-й элемент второго множества: ")))
    

intersection = sorted(list(set_a.intersection(set_b)))
print(f"Числа, которые встречаются в обоих наборах в порядке возрастания без повторений: {intersection}")


############Задача 24###########
n = int(input()) # количество кустов
a = list(map(int, input().split())) # массив урожайности

ans = 0 # инициализируем максимальное число ягод

for i in range(n):
    # перебираем все возможные варианты выбора кустов для сбора ягод
    # начиная с i-го куста и двух его соседей
    j = (i - 1 + n) % n
    k = (i + 1) % n
    berries = a[i] + a[j] + a[k]
    if berries > ans:
        ans = berries

print(ans) # выводим максимальное число ягод