f= open('sample.txt','a+')
print('cursor at',f.tell())
f.write("django for web\n")
f.seek(0)

a=[]
for line in f:
    a.append(line)

print(a)
f.close()