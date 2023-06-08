#open a file to write
f=open("myfile.txt","w")

s=input("enter text")
f.write(s)
f.close()