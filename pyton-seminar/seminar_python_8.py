#Задача1
def read_last(lines, file):
     if lines > 0:
         with open('article.txt', encoding='utf-8') as text:
             file_lines = text.readlines()[-lines:]
         for line in file_lines:
             print(line.strip())
         else:
             print('Количество строк может быть только целым положительным')

 # Тесты
# read_last(3, 'article.txt')
# read_last(-5, 'article.txt')


# article.txt
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела


# Задача 2
with open('article.txt') as file:
    for line in file.readlines():
        if len(line) > max_len:
            max_len = len(line)
            max_str = [line]
        elif len(line) == max_len:
            max_str.append(line)

        for elem in max_str:
            print(elem, end='article.txt')
