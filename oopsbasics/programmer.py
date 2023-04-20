class Programmer:

    def setName(self,n):
        self.name=n

    def getName(self):
        return self.name

    def setSalary(self,sal):
        self.setSalary=sal

    def getSalary(self):
        return self.Salary
    
    def setTechnologies(self,techs):
        self.setTechnologies=techs

    def getTechnologies(self):
        return self.setTechnologies
    
p1=Programmer()
p1.setName('john')
p1.setSalary(700)
p1.setTechnologies(['java','python'])

print(p1.getName)
print(p1.getSalary)
print(p1.getTechnologies)

        
