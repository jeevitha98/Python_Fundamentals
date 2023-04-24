class Patient:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def addClinicalData(self,clinical):
        self.clinical.append(clinical)

class Clinical:
    def __init__(self,componentName,componentValue) :
        self.componentname=componentName
        self.componentvalue=componentValue

p = Patient('john',40)

c1=Clinical('bp','88/122')
p.addClinicalData(c1)

c2=Clinical('bp','100/122')
p.addClinicalData(c2)

