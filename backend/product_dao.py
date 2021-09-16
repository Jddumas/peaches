from entity.product import Product
from postgres import Postgres
import sql

db = Postgres()

class ProductDAO:
    def __init__(self):
        print("Instantiating product dao")

    def get_all(self):
        rows = db.query(sql.SQL_GET_PRODUCTS_BY_ACTIVE) # rows is array of tuple, that can be accessed in a manner like dictionary (but it's not dict)
        # we cannot return this to flask controller, so convert this to a model. We use Product.from_db to convert each row into a Product.
        products = [ Product.from_db(row) for row in rows ] # conversion using list comprehension

        # The next 3 lines convert the list of product to a dictionary of product dict. Flask cannot accept list, only dict or string, or number
        product_dicts = {}
        for product in products:
            product_dicts[product.sku] = product.dict() # flask cannot send Product typed object, so convert that to dict
        return product_dicts 

    def get(self, sku):
        rows = db.query(sql.SQL_GET_PRODUCT_BY_SKU, { "sku": sku })
        product = Product.from_db(rows[0]) # only 1 result, because select by SKU
        return product.dict()

    def create(self, product_configs = {}):
        product = Product(**product_configs);
        row = db.update(sql.SQL_CREATE_PRODUCT, product.dict())
        # convert to Product, then to dict
        product_from_db = Product.from_db(row)
        return product_from_db.dict()
    

    def update(self, sku, product_configs):
        # Implement this method to talk to db
        # Step 1: get existing product from database, using method self.get(sku).
        product = self.get(sku)
        # Check if it exists. If not exists throw Exception (or allow Exception to "bubble" up if already throwing)
        if product is None:
            raise Exception("not found")             
        # # Step 2: calculate altered product. Make sure that sku cannot be altered.
        altered_product_configs = {**product, **product_configs, "sku": sku}
        altered_product = Product(**altered_product_configs) # FOR VALIDATION
        # # # Step 3: writes to database the updated product. Make sure to catch exception - caught in controller
        db.update(sql.SQL_UPDATE_PRODUCT, altered_product_configs)        

        # # Step 4: return altered product calculated above.
        return altered_product_configs


    def deactivate(self, sku):
        product = self.update(sku, {"active": False})
        return product


    def activate(self, sku):
        product = self.update(sku, {"active": True})
        return product

product_dao = ProductDAO()