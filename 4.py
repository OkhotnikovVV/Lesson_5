# 4. Создать (не программно) текстовый файл.
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

rename = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
ru = open("Number_ru.txt", "w+")
with open("Number.txt") as another_file:
    for line in another_file:
        content = line.split()
        content[0] = rename.get(content[0])
        content_ru = " ".join(content)
        ru.write(content_ru + "\n")
ru.close()




