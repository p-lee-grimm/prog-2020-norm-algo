def text_find(source_text):
    result_text = open('result.txt', 'r')
    result_read = result_text.read()
    a = result_read.find(source_text)
    result_text.close()
    return a
# проверка содержания в тексте подстроки


def markov_replace(source_text, replace_text):
    result_file = open('result.txt', 'r')
    result_text = result_file.read()
    open_file_write = open('result.txt', 'w')
    open_file_write.write(result_text.replace(source_text, replace_text, 1))
    result_file.close()
    open_file_write.close()
# замена левой части подстановки на правую один раз


result_write = open('result.txt', 'w')
initial_read = open('edit.txt', 'r')
read_for_copy = initial_read.read()
result_write.write(read_for_copy)
result_write.close()
initial_read.close()

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
file = open('key.txt', 'r')
for line in file.readlines():
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
file.close()
# внос данных с файла key.txt без последнего символа- переноса строки, в соответствующие ячейки массивов

counter = 0
while counter < substitution_number:
    # пока не пройдены все подстановки, т.е. не пройдены все элементы массивов
    if text_find(left_substrings[counter]) != -1:
        if conclusive[counter] == 0:
            markov_replace(left_substrings[counter], right_substrings[counter])
            counter = 0
            # если подстановка не заключительная, выполняется одна замена
            # потом выполняется обнуление счетчика, чтобы проверить более приоритетные подстановки
        else:
            markov_replace(left_substrings[counter], right_substrings[counter])
            break
            # если подстановка заключительная, цикл заканчивается
    else:
        counter += 1
        # если подстроки нет в тексте, смотрится следующая по приоритету подстановка
