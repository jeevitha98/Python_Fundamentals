#print double the val of a num using decor
def decor(fun):
    def innerfunc():
        result= fun()
        return result*2
    return innerfunc

def num():
    return 5

finalresult=decor(num)
print(finalresult())
