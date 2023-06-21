#open a file to write
f=open("myfile.txt","w")
print("enter text(type # when done)")
s=''
while s!="#":
    s=input("")
    f.write(s)

f.close()