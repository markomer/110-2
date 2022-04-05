


def test_dict():
  me = {
    "first": "Mark",
    "last": "Omer", # str
    "age": 29,      # int
    "hobbies": [],  # list
    "address": {    # dict
      "street": "2 E 3 S",
      "city": "Nowhere"
    },
    "another" : 12,

  }


  print(me["first"] + " " + me["last"])

  print("My age is: " + str(me["age"]))
  print(f"My age is: {me['age']}")

  address = me["address"]
  print(type(address))  # try this for type of data
  print(address["street"])

  print(me["address"]["city"])

  # add new keys
  me["color"] = "red"

  # modity existing keys
  me["age"] = 36

  # check if a key exists in a dict
  if "age" in me:
    print("Age extsts")


print("---- Dictionary Test ----")
test_dict()