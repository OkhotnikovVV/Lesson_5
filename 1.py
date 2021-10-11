# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

another_file = open("File_1.txt", "w+")
while True:
    write_to_file = input("Введите текст для записи в файл: ")
    if write_to_file == "":
        break
    another_file.write(write_to_file + "\n")
another_file.close()
print("Файл. Закрыт: ", another_file.closed)
