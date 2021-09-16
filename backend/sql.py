# products
def SQL_CREATE_PRODUCT_TABLE(table_name):
    return f"CREATE TABLE {table_name} (sku integer SERIAL PRIMARY KEY, description character varchar(400), brand character varchar(400), price numeric, weight numeric, category character varchar(400), stock integer, thumbnail_url character varchar(800), shelf_life integer, active boolean);"

SQL_GET_ALL_PRODUCTS = "SELECT * FROM product;" # dont use this??
SQL_GET_PRODUCT_BY_SKU = "SELECT * FROM product WHERE sku=%(sku)s and active=true"
SQL_GET_PRODUCTS_BY_ACTIVE = "SELECT * FROM product WHERE active=true;"
SQL_UPDATE_PRODUCT = "UPDATE product SET sku=%(sku)s, description=%(description)s, brand=%(brand)s, price=%(price)s, weight=%(weight)s, category=%(category)s, stock=%(stock)s, thumbnail_url=%(thumbnail_url)s, shelf_life=%(shelf_life)s, active=%(active)s WHERE sku=%(sku)s  RETURNING *;"
SQL_CREATE_PRODUCT = "INSERT INTO product VALUES (default, %(name)s, %(description)s, %(brand)s, %(price)s, %(weight)s, %(category)s, %(stock)s, %(thumbnail_url)s, %(shelf_life)s, %(active)s) RETURNING *;"

# items
def SQL_CREATE_ITEM_TABLE(item_name):
    return f"CREATE TABLE {item_name} (id integer SERIAL PRIMARY KEY, sku_id integer, reception_date character varchar(400), removal_date character varchar(400), state character varchar(400));"

SQL_GET_ALL_ITEMS = "SELECT * FROM item;"
SQL_GET_ITEM_BY_ID = "SELECT * FROM item WHERE id=%(id)s;"
SQL_CREATE_ITEM = "INSERT INTO item VALUES (default, %(sku_id)s, %(description)s, %(reception_date)s, %(removal_date)s, %(state)s) RETURNING *;"


# BELOW HERE BAD
# In psycopg, you use syntax %(<variable_name>)s to specify a "named" slot for subsequent interpolation
# RETURNING * is a SQL clause equals to SELECT * FROM <table> WHERE id = <just inserted id>. It's a way to get the inserted row in 1 go


def SQL_GET_PRODUCTS_BY_BRAND(brand):
    return f"SELECT * FROM product WHERE brand={brand}"

def SQL_GET_PRODUCTS_BY_CATEGORY(category):
    return f"SELECT * FROM product WHERE category={category}"


def SQL_GET_PRODUCT_BY_CRITERIUM(criteria, value):
    return f"SELECT * FROM product WHERE {criteria}={value}"

# def SQL_GET_PRODUCT_BY_CRITERIA(criteria_list: [(criteria, value)]):
    # return f"SELECT * FROM product WHERE {[CRITERIA = VALUE]}"