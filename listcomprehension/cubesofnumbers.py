'''lst=[]
for x in range(1,20):
    lst.append(x**3)
    
print(lst)'''

lst=[]

lst=[x**3 for x in range(1,20)]
print(lst)