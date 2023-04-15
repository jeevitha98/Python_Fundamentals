def decorfunc(func):
    def inner(n):
        result= func(n)
        result+= "how are you"
        return result
    return inner

@decorfunc
def hello(name):
    return "hello" +name
