class Student:
    major="CSE"

    def __init__(self,rollno,name) :
        self.rollnum=rollno
        self.name=name

s1=Student(1,'jee')
s2=Student(2,'suu')

print(s1.major)
print(s2.major)
print(s1.name)
print(s2.name)
print(Student.major)



