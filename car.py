from mol import vehicle

class Car(vehicle):
    def __init__(self, engine, tires=None, distance_travelled=0, unit='miles'):
       super().__init__(distance_travelled, unit)
       if not tires:
           tires = ['tires', 'tires', 'tires', 'tires']
       self.tires = tires
       self.engine = engine

    def drive(self, distance):
        self.distance_travelled += distance