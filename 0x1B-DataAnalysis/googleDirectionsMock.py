import random

class GoogleDirectionsMock:
    def __init__(self):
       self.distance = {}
    
    def query(self, origin, destination):
        if (origin, destination) not in self.distance:
            distance = random.randint(1, 100)
            self.distance[(origin, destination)] = distance

        return GoogleDirectionsResponseMock(self.distance[(origin, destination)])
    
class GoogleDirectionsResponseMock:
    def __init__(self, distance):
        self.distance = distance 
