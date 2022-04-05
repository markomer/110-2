import json
from flask import Flask, abort, request  # from file or mdule import X
from mock_data import catalog  # fn or something...
from config import db
from bson import ObjectId


app = Flask("Server")


@app.route("/")
def home():
  return "Hello from Flask"



@app.route("/me") # add /me to the URL
def about_me():
  return "Mark Omer"



#####################################
####  API ENDPOINTS  ################
####   RETURN JSON   ################
#####################################


# @app.route("/api/catalog")
@app.route("/api/catalog", methods=["get"])
def get_catalog():

  """ return "catalog data"
  return json.dumps(prod) # this is how parse..."""
  # return json.dumps(catalog)

  products = []
  cursor = db.products.find({}) # cursor is collection

  for prod in cursor:
    prod["_id"] = str(prod["_id"])
    products.append(prod)

  return json.dumps(products)

@app.route("/api/catalog", methods=["post"])
def save_product():
  product = request.get_json()  # returns data (payload) from the 
  
  # set a unique _id on product
  # product["_id"] = 2
  # catalog.append(product) # save it to the data base

  db.products.insert_one(product) # into Mongo db
  print(product)

  # fix _id
  product["_id"] = str(product["_id"])



  # crash...
  return json.dumps(product)
  



# GET /api/catalog/count -> how many products exist in the catalog

@app.route("/api/catalog/count")
def product_count():
  cursor = db.products.find({})
  count = 0
  for prod in cursor:
    count += 1

  return json.dumps(count)
  # or... return json.dumps(len(count))

# get /api/catalog/total => the sum of all porduct's prices
@app.route("/api/catalog/total")
def total_of_catalog():
  total = 0
  cursor = db.products.find({})
  for prod in cursor: # into prods in catalog array
    total += prod["price"]

  return json.dumps(total)



@app.route("/api/product/<id>") # whatever is in <xx> is an id var
def get_by_id(id):

  prod = db.products.find_one({ "_id": ObjectId(id) })

  if not prod:

    return abort(404, "No product with such id")

  prod["_id"] = str(prod["_id"])
  return json.dumps(prod)

  # find the product with _id is equal to id
  #for prod in catalog:
    #if prod["_id"] == id:
      #return json.dumps(prod)

  # not found, return an error 404
  #return abort(404, "No product with such id")


# GET /api/product/cheapest
# should return the product with the lowest price


@app.route("/api/product/cheapest")
def cheapest_product():
  solution = catalog[0]
  for prod in catalog:
    if prod["price"] < solution["price"]:
      solution = prod

  return json.dumps(solution)



@app.route("/api/categories")
def unique_categories():
  categories = []
  for prod in catalog:
    category = prod["category"]
    if not category in categories:
      categories.append(category)

  return json.dumps(categories)

# 
# Ticket 2345
# Create and endpoint that allow the client to get all the products
# for an specified category 
# /api/catalog/Fruit where Fruit is the category in question

@app.route("/api/catalog/<category>")
def get_by_category(category):
  #  coursor = db.products.find({})
  products = []
  cursor = db.products.find({"category": category})
  for prod in cursor:
    prod["_id"] = str(prod["_id"])
    products.append(prod)

  return json.dumps(prod)
  #result = []
  #for prod in catalog:
    #if prod["category"] == category:
      #result.append(prod)

  #return json.dumps(result)

  #prod = db.products.find_one({ "_id": ObjectId(id) })

  #if not prod:

    #return abort(404, "No product with such id")

  #prod["_id"] = str(prod["_id"])
  #return json.dumps(prod)


@app.get("/api/someNumbers")
def some_numbers():
 # print numbers from 1 to 50
  numbers = []

  for num in range(1, 51):
    numbers.append(num)
  
  return json.dumps(numbers)


######################################################
#########    Coupon Code EndPoints   #################
######################################################

# 1 Get all coupons
# 2 Save coupon
# 3 Get a coupon based on its code

@app.route("/api/couponCode", methods=["GET"])
def get_coupons():

  coupons = []
  cursor = db.coupons.find({})
  
  for coup in cursor:
    coup["_id"] = str(coup["_id"])
    coupons.append(coup)
  return json.dumps(coupons)

# create the POST /api/couponCode
# get the coupon from the request 
# assign an _id
# and add it to all coupons
# return the coupon as json

@app.route("/api/couponCode", methods=["POST"])
# OR @app.post("/api/couponCode")
def save_coupon():
  coupon = request.get_json()
  
  db.coupons.insert_one(coupon)
  print(coupon)

  coupon["_id"] = str(coupon["_id"])

  return json.dumps(coupon)

@app.route("/api/couponCode/<codes>")
def coupon_code(code): 

  coupons = []
  cursor = db.coupons.find({"code": code})

  for coup in cursor:
    coup["_id"] = str(coup["_id"])
    coupons.append(coup)

  return json.dumps(coupons)

######### my version below #############

allTheCoupons = []

@app.route("/api/couponCodes", methods=["GET"])
def get_codes():
  return json.dumps(allTheCoupons)

@app.route("/api/couponCodes", methods=["POST"])
def save_codes():
  codes = request.get_json()  # returns data (payload) from the 
  codes["_id"] = 9  # set a unique _id on product

  allTheCoupons.append(codes) # save it to the data base
  
  return json.dumps(codes)




app.run(debug=True)