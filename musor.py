b = r'C:\Users\User\Desktop\folder1\t1\newfile.txt'
c = r'C:\Users\User\Desktop\folder1\t1\key.txt'
count = 0

file = open(c, 'r')
for line in file.readlines():
    if line.__contains__("||--"):
        count += 1
file.close()

FROM = [0]*count
TO = [0]*count
F = 0
T = 0

file = open(c, 'r')
for line in file.readlines():
    if line.__contains__("||--"):
        FROM[F] = line[4:]
        F += 1
file.close()

file = open(c, 'r')
for line in file.readlines():
    if line.__contains__("-->>"):
        TO[T] = line[4:]
        T += 1
file.close()


def textfind(filename, sourcetext):
    file = open(filename, 'r')
    text = file.read()
    a = text.find(sourcetext)
    file.close()
    return a


def mpod(filename, sourcetext, replacetext):
    file = open(filename, 'r')
    text = file.read()
    file.close()
    file = open(filename, 'w')
    file.write(text.replace(sourcetext, replacetext, 1))
    file.close()


for i in range(count):
    print(FROM[i])
    print(TO[i])


for i in range(count):
    mpod(b, FROM[i], TO[i])
