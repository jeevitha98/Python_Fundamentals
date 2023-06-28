import pickle

f=open('student.data','rb')

#pickle.load(filename)
obj=pickle.load(f)
obj.display()

f.close()
