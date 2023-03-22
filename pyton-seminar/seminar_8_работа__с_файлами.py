# Функция которая открывает файлы
# with open('example.txt','r',encoding='utf-8') as file:
#     #считать информацию с файла
#     text = file.read()
#     for letter in text: #выводит буквы в виде списка
#       print(text)


# чтение файла построчно
# with open('example.txt', 'r', encoding='utf-8') as file:
#  len = file.readline()
# while line :
#    print(line)
#    line = file.readline()


#запись файла 
with open('res.txt','a',encoding='utf-8') as file: #если я заменю 'w' на 'a' то данные дозапишутся в  файли res
  res = [1,2,3]
  for el in res:
   file.write(str(el))


