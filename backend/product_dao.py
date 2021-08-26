mocks = {
    '1': {
        'sku': 1,
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
    '2': {
        'sku': 2,
        'description': 'Spaghetti box from Italy',
        'brand': 'Skinner',
        'price': 5.00,
        'weight': 3.00,
        'category': 'Pasta',
        'stock': 200,
        'thumbnail_url': 'https://i5.walmartimages.com/asr/bb8887af-420d-471d-a9db-e18010f6f369_1.225db54c3a0c677cb668f90b10b9737c.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF',
        'shelf_life': 120,
        'active': True
    },
    '3': {
        'sku': 3,
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
        return mocks

    def get(self, sku):
        return mocks.get(sku)        
    
    def create(product_configs):
        mocks.append(product_configs)
        return mocks
    
    def update(sku, product_configs):
        pass
    
    def deactivate(sku):
        product = product_dao.get(sku)
        product.active = False

    def activate(sku):
        product = product_dao.get(sku)
        product.active = True

product_dao = ProductDAO()