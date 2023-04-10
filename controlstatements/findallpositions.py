'''prog to print psoitions of a substring in a string'''

s="take up one idea and make that idea your life."\
  "think and dream of that idea ad leave every other idea alone."

subs="idea"
fount= False
pos= -1
length=len(s)
while True:
    pos = s.find(subs,pos+1,length)
    if pos == -1:
        break
    print("found the substring at position", pos)
    found=True
if found==False:
    print("sub string not found")