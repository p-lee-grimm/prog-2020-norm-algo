def text_find(source_text):
    a = edit_file.find(source_text)
    return a
# проверка содержания в тексте подстроки


initial = open('edit.txt', 'r')
edit_file = initial.read()

substitution_number = 0
key = open('key.txt', 'r')
for line in key.readlines():
    if "/=--" in line:
        substitution_number += 1
key.close()
left_substrings = [''] * substitution_number
right_substrings = [''] * substitution_number
conclusive = [0] * substitution_number
# считывание числа подстановок и создание 3 массивов с найденной длиной:
# первый для левых частей, второй для правых, третий для определения, является ли подстановка заключительной

left_count = 0
right_count = 0
key = open('key.txt', 'r')
for line in key.readlines():
    if "/=--" in line:
        left_substrings[left_count] = line[4:len(line) - 1]
        left_count += 1
    else:
        if "--=>>" in line:
            right_substrings[right_count] = line[5:len(line) - 1]
            conclusive[right_count] = 1
            right_count += 1
        else:
            if "-=>>" in line:
                right_substrings[right_count] = line[4:len(line) - 1]
                conclusive[right_count] = 0
                right_count += 1
key.close()
# внос данных с файла key.txt без последнего символа- переноса строки, в соответствующие ячейки массивов

counter = 0
while counter < substitution_number:
    # пока не пройдены все подстановки, т.е. не пройдены все элементы массивов
    if text_find(left_substrings[counter]) != -1:
        if conclusive[counter] == 0:
            edit_file = edit_file.replace(left_substrings[counter], right_substrings[counter], 1)
            # замена левой части подстановки на правую один раз
            counter = 0
            # если подстановка не заключительная, выполняется одна замена
            # потом выполняется обнуление счетчика, чтобы проверить более приоритетные подстановки
        else:
            edit_file = edit_file.replace(left_substrings[counter], right_substrings[counter], 1)
            break
            # если подстановка заключительная, цикл заканчивается
    else:
        counter += 1
        # если подстроки нет в тексте, смотрится следующая по приоритету подстановка
result_write = open('result.txt', 'w')
result_write.write(edit_file)
