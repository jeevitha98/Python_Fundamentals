#calculate average of six numbers-> avg of first three, avg of next three
#finally calculate the average of the two averages
a,b,c=[int(x) for x in input('enter first 3 int numbers').split()]
d,e,f=[int(y) for y in input('enter next 3 int numbers').split()]

avg1=(a+b+c)/3
print('average of first 3 numbers is',avg1)

avg2=(d+e+f)/3
print('average of next 3 numbers is',avg2)

avg=(avg1+avg2)/2
print('average of the calculated averages is',avg)