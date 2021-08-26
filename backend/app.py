from flask import Flask, abort
from product_dao import product_dao

app = Flask(__name__)

@app.route("/")
def default():
    return "Hello world"

@app.route("/products")
def get_all_products():
    return product_dao.get_all()

@app.route("/products/<sku>")
def get_products_by_sku(sku):
    product = product_dao.get(sku)
    
    if product is None:
        abort(404)
    else:
        return product

# create
@app.route("/products", methods = ['POST'])
def create_product():
    new_product = req.body
    # new_product = {
    #             "6"{
    #                'sku': "6",
    #                'description': "something",
    #                'brand': "fdsafdsafds",
    #                'price': 43,
    #                'weight': 34,
    #                'category': "lala",
    #                'stock': 13,
    #                'thumbnail_url': "www.fdsfd.com",
    #                'shelf_life': 45,
    #                'active': True
    #                 }
    #             }
    product = product_dao.create(new_product)
    return product

# update
@app.route("/products/<sku>", methods = ['PUT'])
def update_product():
    product = update(sku, product_configs)
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
    



