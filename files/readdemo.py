f=open('sample.txt','r')
print(f.read())

f.seek(0) #moves cursor to that location
print(f.readline()) #read one line at a time

f.seek(0)
print(f.readlines())

f.close()

