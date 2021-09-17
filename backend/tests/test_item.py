from entity.item import Item
from pydantic import ValidationError
import pytest
from uuid import uuid4

def test_it_validates_item_successfully():
    mock_item_config = {
        'id': uuid4(),
        'sku_id': 1,
        'reception_date': "5/7/2019",
        'removal_date': "",
        'state': "IN_INVENTORY"
    }
    try:
        item = Item(**mock_item_config)
    except Exception as e:
        pytest.fail(e)

def test_it_raise_validation_error():
    mock_item_config = {
        'id': 20,
        'sku_id': -1,
        'reception_date': "5/7/2019",
        'removal_date': "",
        'state': "IN_INVENTORY"
        }
    with pytest.raises(ValidationError):
        Item(**mock_item_config)

# if state is wrong then it will be valid?
def test_it_validates_impossible_state():
    mock_item_config = {
        'id': 20,
        'sku_id': 1,
        'reception_date': "5/7/2019",
        'removal_date': "",
        'state': "NOT_CORRECT"
        }
    try:
        Item(**mock_item_config)
    except ValidationError as e:
        assert len(e.errors()) == 2


## other tests
# id sku, rep date and state missing
def test_it_validates_fail_missing_fields():
    try:
        Item(**{})
    except ValidationError as e:
        assert len(e.errors()) == 4


def test_it_check_non_negative():
    try:
        mock_item_config = {
        'id': -20,
        'sku_id': -1,
        'reception_date': "5/7/2019",
        'removal_date': "",
        'state': "IN_INVENTORY"
        }
        Item(**mock_item_config)
    except ValidationError as e:
        assert len(e.errors()) == 2

def test_it_converts_from_db():
    id = uuid4()
    row = {
        "id": id,
        "sku_id": 3,
        "reception_date": "today",
        "removal_date": "tomorrow",
        "state": "IN_INVENTORY"
    }
    converted_item = Item.from_db(row);
    assert converted_item.dict() == row