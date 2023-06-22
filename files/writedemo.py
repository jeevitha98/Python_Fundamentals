f=open('sample.txt','w+')

f.write('python is easy\n')

f.writelines(['python\n','django\n'])

print('cursor is at ',f.tell()) # cursor location
f.seek(0)
print(f.read())