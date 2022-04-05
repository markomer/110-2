from mock_data import catalog



# count the product whose title contains the text
def find_prod():
  text = "shiRt"

  # 1 for loop and print the title
  for prod in catalog:
    title = prod["title"]
    print(title)


  count = 0
  for prod in catalog:
    title = prod["title"]
    if text.lower() in title.lower():  # or.. if title.find(text) >= 0:
      count += 1

  print(count)


def find_prod():
  text = "shi"

  count = 0
  for prod in catalog:
    title = prod["title"]
    if text.lower() in title.lower():  # or.. if title.find(text) >= 0:
      print(f"{title} ${prod['price']}")



def find_unique_categories():
  
  categories = [] # not inside the for loop..!!..
  for prod in catalog:
    category = prod["category"]
    if not category in categories:
      categories.append(category)

  print(categories)


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





inventory_total()
items_in_inventory()
find_unique_categories()
find_prod()