#num=int(input("enter an even num"))
#assert num%2==0, "input invalid or odd num"

try:
    num=int(input("enter an even num"))
    assert num%2==0, "input invalid or odd num"

except AssertionError as obj:
    print(obj)

    print("after assertion")