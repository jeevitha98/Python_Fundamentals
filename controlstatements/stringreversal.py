'''s=input('enter a string')
print(s[::-1])'''

s1=input('enter a string')
i=len(s1)-1
result=''

while i >= 0:
    result=result+s1[i]
    i=i-1

print(result)

s2='-'.join(['a','b','c'])
print(s2)
#or
'''s2=input('enter a string')
print(''.join(reversed(s)))'''