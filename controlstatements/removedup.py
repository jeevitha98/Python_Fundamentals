#remove dup entries in a list
l1=eval(input('enter a list of elements'))
print(l1)
l2=[]
for each_value in l1:
    if each_value not in l2:
        l2.append(each_value)
print(l2)

#or use set
s1=set(l1)
print(s1)