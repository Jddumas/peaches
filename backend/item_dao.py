from entity.item import Item
from uuid import uuid4, UUID
from postgres import Postgres
import sql

db = Postgres()

class ItemDAO:
    def __init__(self):
        print("Instantiating Item DAO")

    # done?
    def get_all(self):
        # old
        # filtered = { id: item for id, item in mocks.items() }
        # return filtered
        # new
        rows = db.query(sql.SQL_GET_ALL_ITEMS)
        items = [ Item.from_db(row) for row in rows ] # conversion using list comprehension
        
        # The next 3 lines convert the list of product to a dictionary of item dict. Flask cannot accept list, only dict or string, or number
        item_dicts = {}
        for item in items:
            item_dicts[str(item.id)] = item.dict() # flask cannot send Item typed object, so convert that to dict
        return item_dicts
    
    # done?
    def get(self, id):
        # old
        # return mocks.get(id)
        print("id", id)
        # new
        rows = db.query(sql.SQL_GET_ITEM_BY_ID, { "id": id })  
        print(rows)      
        item = Item.from_db(rows[0]) # only 1 result, because select by SKU
        return item.dict()

    # done?
    def create(self, item_configs = {}):
        # old
        # generated_id = uuid4()
        # new_item_configs = {**item_configs, "id": generated_id}
        # new_item = Item(**new_item_configs) # may raise Validation Exception
        # mocks[str(generated_id)]= new_item.dict()
        # return mocks.get(str(generated_id))

        # new
        generated_id = uuid4()
        item = Item(**item_configs, id=generated_id);

        print(item.dict())
        row = db.update(sql.SQL_CREATE_ITEM, item.dict())
        # convert to Item, then to dict
        item_from_db = Item.from_db(row)
        return item_from_db.dict()

    
    def update(self, id, item_configs):
        # old
        # # get item
        # item = mocks.get(id)
        # print("item", item)
        # # calculate change, produce altered item
        # altered_item_configs = {**item, **item_configs, "id": id}
        # # validate altered item
        # altered_item = Item(**altered_item_configs).dict() # may raise Validation Exception
        # # save altered item back into mocks
        # mocks[id] = altered_item
        # # return altered item to controller ###also bad
        # return altered_item

        # new
        item = self.get(id)
        if item is None:
            raise Exception("not found")             
        altered_item_configs = {**item, **item_configs, "id": id}
        altered_item = Item(**altered_item_configs) # FOR VALIDATION
        db.update(sql.SQL_UPDATE_ITEM, altered_item_configs)

    
    def ship(self, id):
        # old
        # item = self.get(id)
        # item["state"] = "SHIPPED"

        # new
        item = self.update(id, {"state": "SHIPPED"})
        return item
    
    def expire(self, id):
        # old
        # item = self.get(id)
        # item["state"] = "EXPIRED"

        # new
        item = self.update(id, {"state": "EXPIRED"})
        return item
    
item_dao = ItemDAO()