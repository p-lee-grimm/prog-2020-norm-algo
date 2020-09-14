f = open('input.txt', 'r')
a = []
for line in f:
    a.append(int(line))
f.close()
f = open('output.txt', 'w')
f.write(str(sum(a)))