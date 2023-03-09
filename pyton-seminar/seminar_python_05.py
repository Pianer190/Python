# Задача 1
# expr = input()
# result = eval(expr)
# print(result)

# expr = "8-5+2-1"
# result = eval(expr)
# print(result)

...


# Задача 2
# s = input()
# word = ""
# for c in s:
#     if c != " ":
#         word += c
#     else:
#         if word != "":
#             print(word)
#         word = ""

# if word != "":
#     print(word)

...

#Задача 28
# def sum(a, b):
#     if b == 0:
#         return a
#     else:
#         return sum(a ^ b, (a & b) << 1)
# print(sum(2,2))

...

#Задача26 
# def power(a, b):
#     if b == 0:
#         return 1
#     else:
#         return a * power(a, b-1)

# a = int(input("Введите число A: "))
# b = int(input("Введите число B: "))

# print(power(a, b))