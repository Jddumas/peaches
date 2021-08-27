from entity.product import Product
from pydantic import ValidationError
import pytest

def test_it_validates_successfully():
    mock_product_config =  {
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
    }
    try:
         product = Product(**mock_product_config)
    except Exception as e:
        pytest.fail(e)


def test_it_check_shelf_life_non_negative():
    mock_product_config = {
        'sku': 1,
        'description': 'Peach box from Federiksburg, Texas',
        'brand': 'All Nature',
        'price': 3.00,
        'weight': 1.00,
        'category': 'fruits',
        'stock': 100,
        'thumbnail_url': 'https://assets.wsimgs.com/wsimgs/rk/images/dp/wcm/202130/0050/img23o.jpg',
        'shelf_life': -7,
        'active': True
        } # fill this in
    with pytest.raises(ValidationError):
        Product(**mock_product_config)

def test_it_validates_fail_missing_fields():
    try:
        Product(**{})
    except ValidationError as e:
        assert len(e.errors()) == 10


def test_it_check_non_negative():
    try:
        mock_product_config = {
        'sku': 1,
        'description': 'Peach box from Federiksburg, Texas',
        'brand': 'All Nature',
        'price': -3.00,
        'weight': -1.00,
        'category': 'fruits',
        'stock': -100,
        'thumbnail_url': 'https://assets.wsimgs.com/wsimgs/rk/images/dp/wcm/202130/0050/img23o.jpg',
        'shelf_life': -7,
        'active': True
        }
        Product(**mock_product_config)
    except ValidationError as e:
        assert len(e.errors()) == 4