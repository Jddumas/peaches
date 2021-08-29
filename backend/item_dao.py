from entity.item import Item
from uuid import UUID4

mocks = {
    4: {
        'id': 4,
        'sku_id': 1,
        'reception_date': "7/4/2018",
        'removal_date': "",
        'state': "IN_INVENTORY"
    }
    }


class ItemDAO:
    def __init__(self):
        print("Instantiating Item DAO")

    def get_all(self):
        filtered = { id: item for id, item in mocks.items() }
        return filtered
    
    def get(self, id):
        return mocks.get(id)

    
    def create(self, item_configs = {}):
        generated_id = UUID4()
        new_item_configs = {**item_configs, "id": generated_id}
        new_item = Item(**new_item_configs) # may raise Validation Exception
        mocks[generated_id]= new_item.dict()
        return mocks.get(generated_id)

    
    def update(self, id, item_configs):
        # get item
        item = mocks.get(id)
        # calculate change, produce altered item
        altered_item_configs = {**item, **item_configs, "id": id}

        # validate altered item
        altered_item = Item(**altered_item_configs) # may raise Validation Exception
        
        # save altered item back into mocks
        mocks[id] = altered_item

        # return altered item to controller
        return altered_item
    
    def ship(self, id):
        item = self.get(id)
        item["state"] = "SHIPPED"
    
    def expire(self, id):
        item = self.get(id)
        item["state"] = "EXPIRED"
    
item_dao = ItemDAO()