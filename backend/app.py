from flask import Flask, abort, request
from product_dao import product_dao
from item_dao import item_dao
from pydantic import ValidationError

app = Flask(__name__)

@app.route("/")
def default():
    return "Hello world"

@app.route("/products")
def get_all_products():
    return product_dao.get_all()

@app.route("/products/<int:sku>")
def get_products_by_sku(sku):
    product = product_dao.get(sku)
    
    if product is None:
        abort(404)
    else:
        return product

# create
@app.route("/products", methods = ['POST'])
def create_product():
    data = request.get_json()
    try:
        product = product_dao.create(data)
        return product
    except ValidationError as e:
        abort(400, str(e))

# update
@app.route("/products/<int:sku>", methods = ['PUT'])
def update_product(sku):
    changes = request.get_json()
    # handle exceptions
    try:
        product = product_dao.update(sku, changes)
        return product
    except ValidationError as e:
        abort(400, str(e))

# deactivate/activate
@app.route('/products/<int:sku>', methods = ['DELETE'])
def deactivate_product_by_sku(sku):
    # if the product does not exist
    product = product_dao.get(sku)    
    if product is None:
        abort(404)
    
    # if the product does exist
    product_dao.deactivate(sku)
    return "OKAY"

# items
#get all
@app.route("/items")
def get_all_items():
    return item_dao.get_all()

# get by id
@app.route("/items/<int:id>")
def get_items_by_id(id):
    item = item_dao.get(id)
    
    if item is None:
        abort(404)
    else:
        return item

# create
@app.route("/items", methods = ['POST'])
def create_item():
    data = request.get_json()
    try:
        item = item_dao.create(data)
        return item
    except ValidationError as e:
        abort(400, str(e))

# update
@app.route("/items/<int:id>", methods = ['PUT'])
def update_item(sku):
    changes = request.get_json()
    # handle exceptions
    try:
        item = item_dao.update(sku, changes)
        return item
    except ValidationError as e:
        abort(400, str(e))

# ship
@app.route('/items/shipped/<int:id>', methods = ['DELETE'])
def ship_item_by_id(id):
    # if the item does not exist
    item = item_dao.get(id)    
    if item is None:
        abort(404)
    
    # if the item does exist
    item_dao.ship(id)
    return "SHIPPED OKAY"


# expire
@app.route('/items/expired/<int:id>', methods = ['DELETE'])
def expire_item_by_id(id):
    # if the item does not exist
    item = item_dao.get(id)    
    if item is None:
        abort(404)
    
    # if the item does exist
    item_dao.expire(id)
    return "EXPIRED OKAY"
       



