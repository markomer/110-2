import json
from winreg import QueryReflectionKey
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
  return json.dumps(prod) # this is how to parse...
  #return json.dumps(catalog)"""
  
  products = []
  cursor = db.products.find({}) # cursor is collection

  for prod in cursor:
    prod["_id"] = str(prod["_id"])
    products.append(prod)

  return json.dumps(products)
  

@app.route("/api/catalog", methods=["post"])
def save_product():
  product = request.get_json()  # returns data (payload) from the 
  
  """ set a unique _id on product
  # product["_id"] = 2
  # catalog.append(product) # save it to the data base"""

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
    # not found, return an error 404
    return abort(404, "No product with such id")

  prod["_id"] = str(prod["_id"])
  return json.dumps(prod)


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

allCoupons = []

@app.route("/api/couponCode", methods=["GET"])
def get_coupons():
  coupons = []
  cursor = db.coupons.find({})
  for coups in cursor:
    coups["_id"] = str(coups["_id"])
    coupons.append(coups)
  
  return json.dumps(coupons)
  
  # return json.dumps(allCoupons)

# create the POST /api/couponCode
# get the coupon from the request 
# assign an _id
# and add it to all coupons
# return the coupon as json

# OR @app.post("/api/couponCode")
@app.route("/api/couponCode", methods=["POST"])
def save_coupon():
  coupon = request.get_json()

  # must contain code, discout
  if not "code" in coupon or not "discount" in coupon:
    return abort(400, "Code and Discount must be entered.")

  # code should have at least 5 characters
  if len(coupon["code"]) < 5:
    return abort(400, "code must have 5 characters.")


  # discount should not be lower than 5 a not greater than 50
  if coupon["discount"] < 5 or coupon["discount"] > 50:
    return abort(400, "Discount must be between 5 and 50.")

  db.coupons.insert_one(coupon)

  coupon["_id"] = str(coupon["_id"])
  return json.dumps(coupon)
  
  #coupon = request.get_json()
  #coupon["_id"] = 42

  #allCoupons.append(coupon)

  #return json.dumps(coupon)


@app.route("/api/couponCode/<code>")
def get_coupon_by_code(code): 
  coupon = db.coupons.find_one({"code": code})
  if not coupon:
    return abort(404, "Invalid Code")

  coupon["_id"] = str(coupon["_id"])
  return json.dumps(coupon)



######### my prior version below #############

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


#################################################
##########    Users EndPoints   #################
#################################################
"""
{
  _id
  email
  userName
  password
  first
  last
}
"""

allUsers = []

@app.route("/api/allUsers", methods=["GET"])
def get_users():
  users = []
  cursor = db.users.find({})
  for user in cursor:
    user["_id"] = str(user["_id"])
    users.append(user)
  
  return json.dumps(users)


@app.route("/api/allUsers", methods=["POST"])
def save_user():
  user = request.get_json()
  # validate userName, password, email
  if not "userName" in user or not "password" in user or not "email" in user:
    return abort(400, "User Name, Password and Email Required")

  # check that the values are not empty
  if len(user["userName"]) < 1 or len(user["password"]) < 1 or len(user["email"]) < 1:
    return abort(400, "Username, Password and Email must have an enrty.")

  db.users.insert_one(user)

  user["_id"] = str(user["_id"])
  return json.dumps(user)


@app.route("/api/allUsers/<email>")
def get_user_by_email(email): 
  user = db.users.find_one({"email": email})
  if not user:
    return abort(404, "No user with that email")

  user["_id"] = str(user["_id"])
  return json.dumps(user)


##################################


@app.route("/api/login", methods=["POST"])
def validate_user_data():
  data = request.get_json() # <= dict w/ user and password

  # if there id not user in data, return a 400 error
  if not "user" in data:
    return abort(400, "User is required for login")

  if not "password" in data:
    return abort(400, "Password is required for login")

  user = db.users.find_one({"userName": data["user"], "password": data["password"]})
  if not user:
    abort(401, "No such user with that userName and password")

  user["_id"] = str(user["_id"])

  user.pop("password")   # remove the password from the user dictionary

  return json.dumps(user)

  

app.run(debug=True)