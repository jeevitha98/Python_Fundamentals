class Flight:
    def __init__(self, engine):
        self.engine=engine
    
    def startEngine(self):
        self.engine.start();

class Airbusengine:
    def start(self):
        print("starting airbus engine")

class Boingengine:
    def start(self):
        print("starting Boing engine")

ae= Airbusengine()
f=Flight(ae)
f.startEngine()

be= Boingengine()
f=Flight(ae)
f.startEngine()