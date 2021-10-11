# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open("File_1.txt") as another_file:
    stroka = 0
    for line in another_file:
        stroka += 1
        content = line.split()
        print(f"Количество слов в строке № {stroka}: {len(content)}")
print("Файл. Закрыт: ", another_file.closed)
