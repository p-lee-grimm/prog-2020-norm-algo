b = 'C:\\Users\\User\\Desktop\\folder1\\t1\\newfile.txt'
c = 'C:\\Users\\User\\Desktop\\folder1\\t1\\key.txt'
count = 0
result = open('result.txt', 'w')
rr = result.read()
have = [0]*count
need = [0]*count
zakl = [0]*count
t = 0
r = 0
file = open(c, 'r')
for line in file.readlines():
    if "/=--" in line:
        count += 1
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
file.close()
kek = open(b, 'r')
textt = kek.read()
openfilew = open(b, 'w')


def findsubstring(substring):
    a = textt.find(substring)
    return a


def markreplace(havesubstring, needsubstring):
    openfilew.write(textt.replace(havesubstring, needsubstring, 1))


for i in range(count):
    print(have[i])
    print(need[i])

j = 0
while j < count:
    if findsubstring(have[j]) != -1:
        if zakl[j] == 0:
            markreplace(have[j], need[j])
            j = 0
        else:
            markreplace(have[j], need[j])
            break
    else:
        j += 1
