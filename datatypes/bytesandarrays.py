lst=[1,2,34]
print(lst)

b=bytes(lst)
print(type(b))

b1=bytearray(lst)
print(type(b1))
b1[2]=33
