# products
from dotmap import DotMap

product_table_name = "flyway.product"
item_table_name = "flyway.item"

SQL = DotMap({
    'PRODUCT': {
        "GET_ALL": f"SELECT * FROM {product_table_name} WHERE active=true;",
        "GET_BY_ID": f"SELECT * FROM {product_table_name} WHERE sku=%(sku)s and active=true;",
        "UPDATE": f"UPDATE {product_table_name} SET description=%(description)s, brand=%(brand)s, price=%(price)s, weight=%(weight)s, category=%(category)s, stock=%(stock)s, thumbnail_url=%(thumbnail_url)s, shelf_life=%(shelf_life)s, active=%(active)s WHERE sku=%(sku)s RETURNING *;",
        "INSERT": f"INSERT INTO {product_table_name} (sku, name, description, brand, price, weight, category, stock, thumbnail_url, shelf_life, active) VALUES (default, %(name)s, %(description)s, %(brand)s, %(price)s, %(weight)s, %(category)s, %(stock)s, %(thumbnail_url)s, %(shelf_life)s, %(active)s) RETURNING *;"
    },
    'ITEM': {
        'GET_ALL': f'SELECT * FROM {item_table_name};',
        'GET_BY_ID': f'SELECT * FROM {item_table_name} WHERE id=%(id)s;',
        'UPDATE': f'UPDATE {item_table_name} SET sku=%(sku)s, reception_date=%(reception_date)s, removal_date=%(removal_date)s, state=%(state)s  WHERE id=%(id)s  RETURNING *;',
        'INSERT': f'INSERT INTO {item_table_name} VALUES (%(id)s, %(sku_id)s, %(reception_date)s, %(removal_date)s, %(state)s) RETURNING *;',
        # NO DELETE, APPEND-ONLY-TABLE.
    }
})
# In psycopg, you use syntax %(<variable_name>)s to specify a "named" slot for subsequent interpolation
# RETURNING * is a SQL clause equals to SELECT * FROM <table> WHERE id = <just inserted id>. It's a way to get the inserted row in 1 go
