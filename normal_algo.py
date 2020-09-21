d = 'C:\\Users\\User\\PycharmProjects\\prog-2020-norm-algo\\src\\edit.txt'
c = 'C:\\Users\\User\\PycharmProjects\\prog-2020-norm-algo\\src\\key.txt'
count = 0
text = open('result.txt', 'w')
file = open(d, 'r')
readd = file.readline()
text.write(readd)
text.close()
file.close()
b = 'C:\\Users\\User\\PycharmProjects\\prog-2020-norm-algo\\src\\result.txt'

file = open(c, 'r')
for line in file.readlines():
    if "/=--" in line:
        count += 1
file.close()

have = [0]*count
need = [0]*count
zakl = [0]*count


t = 0
r = 0
file = open(c, 'r')
for line in file.readlines():
    if "/=--" in line:
        have[t] = line[4:len(line) - 1]
        t += 1
    else:
        if "--=>>" in line:
            need[r] = line[5:len(line) - 1]
            zakl[r] = 1
            r += 1
        else:
            if "-=>>" in line:
                need[r] = line[4:len(line) - 1]
                zakl[r] = 0
                r += 1


def textfind(sourcetext):
    kek = open(b, 'r')
    textt = kek.read()
    a = textt.find(sourcetext)
    return a


def markreplace(sourcetext, replacetext):
    lol = open(b, 'r')
    textt = lol.read()
    openfilew = open(b, 'w')
    openfilew.write(textt.replace(sourcetext, replacetext, 1))
    lol.close()
    openfilew.close()


for i in range(count):
    print(have[i])
    print(need[i])

j = 0
while j < count:
    if textfind(have[j]) != -1:
        if zakl[j] == 0:
            markreplace(have[j], need[j])
            j = 0
        else:
            markreplace(have[j], need[j])
            break
    else:
        j += 1

