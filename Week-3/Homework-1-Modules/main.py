from dto import InventoryItem, ItemOrigin

def main():
  item_origin = ItemOrigin(country = "NZ", production_date = "02/1992")
  
  my_item1 = InventoryItem(name= "Rabbit",
                          quantity=20,
                          serial_num="dghfdg9843te!!",
                          origin=item_origin)
  
  my_serialized_object = my_item1.__dict__
  print(my_serialized_object)
  my_item2 = InventoryItem(**my_serialized_object)
  print(my_item2.__dict__)
  pass

if __name__ == "__main__":
  main()