def ReplaceLineInFile(fileName, sourceText, replaceText):
    file = open(fileName, 'r')
    text = file.read()
    file.close()
    file = open(fileName, 'w')
    file.write(text.replace(sourceText, replaceText))
    file.close()
    print ('went well')

n = int(input())
array = [[0]*n for i in range(3)]

for i in range(0, n):
    array[i][0],array[i][1] = map(str, input().split())

for i in range(0, n):
    print(array[i][0], end=" ")
    print(array[i][1], end="\n")

b = r'C:\Users\User\Desktop\folder1\newfile.txt'

for i in range(n):
    ReplaceLineInFile(b, array[i][0], array[i][1])