# from classes import Ice, Electric
from classes import ElectricCar, IceCar

def main():
  my_ev = ElectricCar("Tesla",25000,500)
  my_ev.drive(distance_km=300)


  print(my_ev.__dict__)
  print(my_ev)
  print("")

  ice_car = IceCar("Mercedes", 25000, 10, 80)
  ice_car.drive(distance_km=200)

  print(ice_car.__dict__)
  print(ice_car)

  


if __name__ == "__main__":
  main()