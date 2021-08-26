from flask import Flask, abort, request
from product_dao import product_dao

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
    product = product_dao.create(data)
    return product

# update
@app.route("/products/<int:sku>", methods = ['PUT'])
def update_product(sku):
    changes = request.get_json()
    product = product_dao.update(sku, changes)
    return product

# deactivate/activate
@app.route('/products/<sku>', methods = ['PUT'])
def deactivate_product_by_sku(sku):
    # if the product does not exist
    product = product_dao.get(sku)    
    if product is None:
        abort(404)
    
    # if the product does exist
    else:
        if product.active == True:
            product = product_dao.deactivate(sku)
            return ("deactivated", product)
        else:
            product = product_dao.activate(sku)
            return ("activated", product)
    



