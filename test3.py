from mock_data import catalog


def lower_than(price):
    # print how many product exist 
    # with a price lower that price var
    pass


def greater_than(price):
    pass



lower_than(10)
lower_than(30)
lower_than(50)
lower_than(100)

greater_than(10)
greater_than(30)
greater_than(50)
greater_than(100)

# see test1.py

def items_in_inventory():
  inventory = []
  for prod in catalog:
    inventory = (prod["stock"])

    # print(inventory)
    # print(f"The Total Inventory Is: {sum(inventory)}")
    # print(f"Inventory Total Count Is: int{inventory})

    print(f"Inventory Item: {inventory}")
    # sum(inventory)


def inventory_total():
  inventories = []
  # total = 0
  for prod in catalog:
    inventory = prod["stock"]
    if not inventory in inventories:
      inventories.append(inventory)
      total = 0
      for num in inventories:
        total += num
  print(f"Inventory Total Is: {total}")

  # sum(inventory)    

  print(f"Inventory List Includes: {inventories}")


items_in_inventory()
inventory_total()
