def text_find(source_text):
    result_text = open('result.txt', 'r')
    result_read = result_text.read()
    a = result_read.find(source_text)
    result_text.close()
    return a


def markov_replace(source_text, replace_text):
    result_file = open('result.txt', 'r')
    result_text = result_file.read()
    open_file_write = open('result.txt', 'w')
    open_file_write.write(result_text.replace(source_text, replace_text, 1))
    result_file.close()
    open_file_write.close()


result_write = open('result.txt', 'w')
initial_read = open('edit.txt', 'r')
read_for_copy = initial_read.read()
result_write.write(read_for_copy)
result_write.close()
initial_read.close()

permutation_number = 0
key = open('key.txt', 'r')
for line in key.readlines():
    if "/=--" in line:
        permutation_number += 1
key.close()

have_substrings = ['']*permutation_number
need_substrings = ['']*permutation_number
conclusive = [0]*permutation_number
left_count = 0
right_count = 0

file = open('key.txt', 'r')
for line in file.readlines():
    if "/=--" in line:
        have_substrings[left_count] = line[4:len(line) - 1]
        left_count += 1
    else:
        if "--=>>" in line:
            need_substrings[right_count] = line[5:len(line) - 1]
            conclusive[right_count] = 1
            right_count += 1
        else:
            if "-=>>" in line:
                need_substrings[right_count] = line[4:len(line) - 1]
                conclusive[right_count] = 0
                right_count += 1
file.close()

counter = 0
while counter < permutation_number:
    if text_find(have_substrings[counter]) != -1:
        if conclusive[counter] == 0:
            markov_replace(have_substrings[counter], need_substrings[counter])
            counter = 0
        else:
            markov_replace(have_substrings[counter], need_substrings[counter])
            break
    else:
        counter += 1
