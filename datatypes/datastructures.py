students={'John':['python','ruby'],'Bob':['java','python']}
keys=students.keys()

for eachkey in keys:
    print("courses taken by", eachkey, "are:")
for eachcourse in students[eachkey]:
    print(eachcourse)