import re
str ="take up one idea at one time 1-12-2013"

result = re.search(r'o\w\w',str)
print(result.group())

result = re.findall(r'o\w\w',str)
print(result)

result = re.match(r'o\w\w',str)
print(result)

result = re.findall(r'o\w+',str) #('o\w*',o\w{1},o\w?,o\w{1,2})
print(result)

result = re.findall(r'\d{1,2}-\d{1,2}-\d{4}',str)
print(result)