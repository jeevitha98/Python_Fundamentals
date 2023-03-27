s="food is love "
print(s)

#indexing
print(s[3])

#repetition-display string several times
print(s*3)

#length of string
print(len(s))

#slicing
print(s[8:12]) #from index 8 to 12
print(s[:8]) #from start till 8th char
print(s[3:-1]) #from 8th char till end of str

#reversing string
print(s[3::-1]) 
print(s[::-1]) #complete string is reversed

#strip- remove whitespaces
print(s.strip())
print(s.lstrip()) #strip from LHS
print(s.rstrip()) #strip from RHS

print(s.find("ood")) #find string/sub-string
print(s.count('a')) #count of char
print(s.count("food")) #count of sub-string
print(s.replace("is","isn't")) #replace old substring to new

