# products
SQL_GET_ALL_PRODUCTS = "SELECT * FROM product;" # dont use this??
SQL_GET_PRODUCT_BY_SKU = "SELECT * FROM product WHERE sku=%(sku)s and active=true"
SQL_GET_PRODUCTS_BY_ACTIVE = "SELECT * FROM product WHERE active=true;"
SQL_UPDATE_PRODUCT = "UPDATE product SET sku=%(sku)s, description=%(description)s, brand=%(brand)s, price=%(price)s, weight=%(weight)s, category=%(category)s, stock=%(stock)s, thumbnail_url=%(thumbnail_url)s, shelf_life=%(shelf_life)s, active=%(active)s WHERE sku=%(sku)s  RETURNING *;"
SQL_CREATE_PRODUCT = "INSERT INTO product VALUES (default, %(name)s, %(description)s, %(brand)s, %(price)s, %(weight)s, %(category)s, %(stock)s, %(thumbnail_url)s, %(shelf_life)s, %(active)s) RETURNING *;"



# items
def SQL_CREATE_ITEM_TABLE(item_name):
    return f"CREATE TABLE {item_name} (id integer SERIAL PRIMARY KEY, sku_id integer, reception_date character varchar(20), removal_date character varchar(20), state character varchar(20));"

SQL_GET_ALL_ITEMS = "SELECT * FROM item;"
SQL_GET_ITEM_BY_ID = "SELECT * FROM item WHERE id=%(id)s;"
SQL_CREATE_ITEM = "INSERT INTO item VALUES (%(id)s, %(sku_id)s, %(reception_date)s, %(removal_date)s, %(state)s) RETURNING *;"
SQL_UPDATE_ITEM = "UPDATE item SET sku=%(sku)s, reception_date=%(reception_date)s, removal_date=%(removal_date)s, state=%(state)s  WHERE id=%(id)s  RETURNING *;"

# In psycopg, you use syntax %(<variable_name>)s to specify a "named" slot for subsequent interpolation
# RETURNING * is a SQL clause equals to SELECT * FROM <table> WHERE id = <just inserted id>. It's a way to get the inserted row in 1 go
