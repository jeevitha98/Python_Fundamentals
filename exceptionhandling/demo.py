#division by zero exception

#logging.basicConfig(filename="mylog.log",level=logging.DEBUG)

try:
    a,b=[int(x) for x in input("enter two numbers").split()]
    c=a/b
    print(c)

except ZeroDivisionError:
    print("division by zero not allowed")
    print("please enter a non zero number")

print("..code after exception..")


