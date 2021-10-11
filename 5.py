# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open("Count.txt", "w+") as another_file:
    another_file.write("-1 0 1 2 3 4 5.6")
    another_file.seek(0)
    content = another_file.read().split()
    for i, item in enumerate(content):
        content[i] = float(item)
    print(sum(content))
