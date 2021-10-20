from entity.item import Item
from sql import SQL

class ItemDAO:
    def __init__(self, db):
        self.db = db;

    def get_all(self):
        rows = self.db.query(SQL.ITEM.GET_ALL)
        # conversion using list comprehension
        items = [Item.from_db(row) for row in rows]

        # The next 3 lines convert the list of product to a dictionary of item dict. Flask cannot accept list, only dict or string, or number
        item_dicts = {}
        for item in items:
            # flask cannot send Item typed object, so convert that to dict
            item_dicts[str(item.id)] = item.dict()
        return item_dicts

    def get(self, id):
        rows = self.db.query(SQL.ITEM.GET_BY_ID, {"id": id})
        item = Item.from_db(rows[0])  # only 1 result, because select by SKU
        return item.dict()

    def create(self, item_configs={}):
        item = Item(**item_configs)
        row = self.db.update(SQL.ITEM.INSERT, item.dict())
        # convert to Item, then to dict
        item_from_db = Item.from_db(row)
        return item_from_db.dict()

    def update(self, id, item_configs):
        item = self.get(id)
        if item is None:
            raise Exception("not found")
        altered_item_configs = {**item, **item_configs, "id": id}
        Item(**altered_item_configs)  # FOR VALIDATION
        self.db.update(SQL.ITEM.UPDATE, altered_item_configs)

    def ship(self, id):
        item = self.update(id, {"state": "SHIPPED"})
        return item

    def expire(self, id):
        item = self.update(id, {"state": "EXPIRED"})
        return item
