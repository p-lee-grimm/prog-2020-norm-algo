b = 'C:\\Users\\User\\Desktop\\folder1\\t1\\newfile.txt'
c = 'C:\\Users\\User\\Desktop\\folder1\\t1\\key.txt'
count = 0                                   #счетчик строк в схеме

file = open(c, 'r')
for line in file.readlines():               #считаем, сколько строк в схеме подстановок
    if "/=--" in line:                      #если в строке есть ))--, то прибавляем 1.
        count += 1
file.close()

have = [0]*count                            #массив что надо заменить
need = [0]*count                            #массив на что надо заменить
zakl = [0]*count                            #показатель заключительной подстановки

t = 0
file = open(c, 'r')
for line in file.readlines():               #вводим в массив то, что надо зменить
    if "/=--" in line:                      #если в строке есть '))--', то в массив вводим строку без этой последовательности символов и без перехода на след строку
        have[t] = line[4:len(line)-1]
        t += 1
file.close()

r = 0
file = open(c, 'r')
for line in file.readlines():               #вводим в массив то, на что надо зменить
    if "--=>>" in line:                      #если в строке есть '-->>', то в массив вводим строку без этой последовательности символов и без перехода на след строку
        need[r] = line[5:len(line)-1]
        zakl[r] = 1
        r += 1
    else:
        if "-=>>" in line:
            need[r] = line[4:len(line) - 1]
            zakl[r] = 0
            r += 1
file.close()


def textfind(sourcetext):                   #проверяем наличие подстроки
    kek = open(b, 'r')
    textt = kek.read()
    a = textt.find(sourcetext)
    return a


def mpod(sourcetext, replacetext):          #заменяем подстроку на другую
    lol = open(b, 'r')
    textt = lol.read()
    openfilew = open(b, 'w')
    openfilew.write(textt.replace(sourcetext, replacetext, 1))
    lol.close()
    openfilew.close()


for i in range(count):                      #записываем все элементы по приколу(проверить корректность)
    print(have[i])
    print(need[i])

for j in range(0, count):                      #для каждой пары элементов массивов производим замены
    while textfind(have[j]) != -1:
        if zakl[i] == 0:
            mpod(have[j], need[j])
        else:
            mpod(have[j], need[j])
            break
