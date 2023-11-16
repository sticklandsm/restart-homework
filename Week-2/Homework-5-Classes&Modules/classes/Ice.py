from .Car import Car

class IceCar(Car):
    def __init__(self, brand, milage_km, fuel_consumption, fuel_level):
        Car.__init__(self, brand, milage_km) #Initialize class Car bringing in the Car class variables, then we bring in IceCar class attrivutes with self
        self.fuel_consumption=fuel_consumption
        self.fuel_level=fuel_level
    def drive(self, distance_km):
      Car.drive(self, distance_km)
      self.fuel_level -= distance_km*self.fuel_consumption/100
