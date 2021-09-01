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

    def get_all(self):
        # TODO: handle db exception
        rows = db.query(sql.SQL_GET_PRODUCTS_BY_ACTIVE) # rows is array of tuple, that can be accessed in a manner like dictionary (but it's not dict)
        # we cannot return this to flask controller, so convert this to a model. We use Product.from_db to convert each row into a Product.
        products = [ Product.from_db(row) for row in rows ] # conversion using list comprehension

        # The next 3 lines convert the list of product to a dictionary of product dict. Flask cannot accept list, only dict or string, or number
        product_dicts = {}
        for product in products:
            product_dicts[product.sku] = product.dict() # flask cannot send Product typed object, so convert that to dict

        return product_dicts


    def get(self, sku):
        # TODO: handle db exception
        rows = db.query(sql.SQL_GET_PRODUCT_BY_SKU, { "sku": sku })
        product = Product.from_db(rows[0]) # only 1 result, because select by SKU
        return product.dict()

    
    def create(self, product_configs = {}):
        # TODO: handle db exception
        row = db.update(sql.SQL_CREATE_PRODUCT, product_configs)
        # convert to Product, then to dict
        product = Product.from_db(row)
        return product.dict()
    

    def update(self, sku, product_configs):
        # get product
        product = mocks.get(sku)
        # calculate change, produce altered product
        altered_product_configs = {**product, **product_configs, "sku": sku}
        print(altered_product_configs)
        # validate altered product
        altered_product = Product(**altered_product_configs).dict() # may raise Validation Exception
        # save altered product back into mocks
        mocks[sku] = altered_product

        # return altered product to controller ###updated
        return altered_product

    
    def deactivate(self, sku):
        product = self.get(sku)
        product["active"] = False

    def activate(self, sku):
        product = self.get(sku)
        product["active"] = True

product_dao = ProductDAO()