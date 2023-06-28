import pickle,student

f=open('student.data','wb')
s=student.Student(123,'john',90)

#pickle.dump(obj,file)
pickle.dump(s,f)

f.close()


