def SQL_CREATE_TABLE(table_name):
    return f"CREATE TABLE {table_name} (sku integer SERIAL PRIMARY KEY, description character varchar(400), brand character varchar(400), price numeric, weight numeric, category character varchar(400), stock integer, thumbnail_url character varchar(800), shelf_life integer, active boolean);"

SQL_GET_ALL_PRODUCTS = "SELECT * FROM product;"
SQL_GET_PRODUCT_BY_SKU = "SELECT * FROM product WHERE sku=%(sku)s"
SQL_GET_PRODUCTS_BY_ACTIVE = "SELECT * FROM product WHERE active=true;"

# In psycopg, you use syntax %(<variable_name>)s to specify a "named" slot for subsequent interpolation
# RETURNING * is a SQL clause equals to SELECT * FROM <table> WHERE id = <just inserted id>. It's a way to get the inserted row in 1 go
SQL_CREATE_PRODUCT = "INSERT INTO product VALUES (default, %(name)s, %(description)s, %(brand)s, %(price)s, %(weight)s, %(category)s, %(stock)s, %(thumbnail_url)s, %(shelf_life)s, %(active)s) RETURNING *;"


def SQL_GET_PRODUCTS_BY_BRAND(brand):
    return f"SELECT * FROM product WHERE brand={brand}"

def SQL_GET_PRODUCTS_BY_CATEGORY(category):
    return f"SELECT * FROM product WHERE category={category}"


def SQL_GET_PRODUCT_BY_CRITERIUM(criteria, value):
    return f"SELECT * FROM product WHERE {criteria}={value}"

# def SQL_GET_PRODUCT_BY_CRITERIA(criteria_list: [(criteria, value)]):
    # return f"SELECT * FROM product WHERE {[CRITERIA = VALUE]}"


# def SQL_CREATE_PRODUCT(description, brand, price, weight, category, stock, thumbnail_url, shelf_life, active):
#     # auto incrementing working?
#     return f"INSERT INTO products_table{(description, brand, price, weight, category, stock, thumbnail_url, shelf_life, active)} VALUES {(description, brand, price, weight, category, stock, thumbnail_url, shelf_life, active)}"


def SQL_UPDATE_PRODUCT(sku, product_updates):
    # convention for product_updates: stock = 100, price = 3.00 
    return f"UPDATE products_table SET {product_updates} WHERE sku={sku};"


def SQL_DEACTIVATE_PRODUCT(sku):
    return f"UPDATE products FROM products_table WHERE sku={sku}"