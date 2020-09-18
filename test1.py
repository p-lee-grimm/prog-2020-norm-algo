f = open(r'C:\Users\User\Desktop\folder1\stih.txt')
g = open(r'C:\Users\User\Desktop\folder1\newfile.txt', 'w')
for line in f:
    if line.__contains__('a'):
        newline = line.replace('a', 'b')
        g.writelines(newline)
        print(newline)




