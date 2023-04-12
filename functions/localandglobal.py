x=123

def display():
    x=67
    print(x)
    print(globals()['x'])

print(x)
z=display
z()
