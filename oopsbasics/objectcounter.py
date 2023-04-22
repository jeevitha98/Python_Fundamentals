class Objectcounter:

    numOfObjects=0

    def __init__(self):
        Objectcounter.numOfObjects += 1

    @staticmethod
    def displayCount():
        print(Objectcounter.numOfObjects)

a1=Objectcounter()
a2=Objectcounter()

Objectcounter.displayCount()