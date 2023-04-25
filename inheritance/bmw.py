class BMW:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def start(self):
        print('starting the car')
        
    def stop(self):
        print('stopping the car')

class ThreeSeries(BMW):
    def __init__(self, cruiseControlEnabled, make, model, year):
        BMW.__init__(self,make, model, year)
        self.cruiseControlEnabled = cruiseControlEnabled

    def display(self):
        print(self.cruiseControlEnabled)


class FiveSeries(BMW):
    def __init__(self, parkingAssistEnabled, make, model, year):
        BMW.__init__(self,make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled
        
threeSeries=ThreeSeries(True,'bmw','328i','2018')

print(threeSeries.cruiseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)

threeSeries.start()
threeSeries.stop()
threeSeries.display()