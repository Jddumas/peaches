from entity.product import Product
from postgres import Postgres
import sql

db = Postgres()

mocks = {
    1: {
        'sku': 1,
        'name': 'Peaches',
        'description': 'Peach box from Federiksburg, Texas',
        'brand': 'All Nature',
        'price': 3.00,
        'weight': 1.00,
        'category': 'fruits',
        'stock': 100,
        'thumbnail_url': 'https://assets.wsimgs.com/wsimgs/rk/images/dp/wcm/202130/0050/img23o.jpg',
        'shelf_life': 7,
        'active': True
    },
    2: {
        'sku': 2,
        'name': 'Spaghetti',
        'description': 'Spaghetti box from Italy',
        'brand': 'Skinner',
        'price': 5.00,
        'weight': 3.00,
        'category': 'Pasta',
        'stock':200,
        'thumbnail_url': 'https://i5.walmartimages.com/asr/bb8887af-420d-471d-a9db-e18010f6f369_1.225db54c3a0c677cb668f90b10b9737c.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF',
        'shelf_life': 120,
        'active': False
    },
    3: {
        'sku': 3,
        'name': 'Potato',
        'description': 'Potatos from Idaho',
        'brand': 'TaterLand',
        'price':6.00,
        'weight': 10.00,
        'category': 'Vegetable',
        'stock': 50,
        'thumbnail_url': 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.instacart.com%2Fproducts%2F16725303-russet-potato-bag-10-lbs&psig=AOvVaw0xsfbRvGRYi7JNVr3IbC-N&ust=1629919947007000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCKj7tI-zyvICFQAAAAAdAAAAABAI',
        'shelf_life': 14,
        'active': True
        }
}

class ProductDAO:
    def __init__(self):
        print("Instantiating product dao")

    # done
    def get_all(self):
        rows = db.query(sql.SQL_GET_PRODUCTS_BY_ACTIVE) # rows is array of tuple, that can be accessed in a manner like dictionary (but it's not dict)
        # we cannot return this to flask controller, so convert this to a model. We use Product.from_db to convert each row into a Product.
        products = [ Product.from_db(row) for row in rows ] # conversion using list comprehension

        # The next 3 lines convert the list of product to a dictionary of product dict. Flask cannot accept list, only dict or string, or number
        product_dicts = {}
        for product in products:
            product_dicts[product.sku] = product.dict() # flask cannot send Product typed object, so convert that to dict
        return product_dicts 

    # done
    def get(self, sku):
        rows = db.query(sql.SQL_GET_PRODUCT_BY_SKU, { "sku": sku })
        product = Product.from_db(rows[0]) # only 1 result, because select by SKU
        return product.dict()

    # done
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
        # print("altered project configs", altered_product_configs)
        altered_product = Product(**altered_product_configs) # FOR VALIDATION
        # print("got here")
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