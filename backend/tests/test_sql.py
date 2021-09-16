from entity.product import Product
from pydantic import ValidationError
import pytest
import product_dao as productDAO



def test_get_works():
    try:
        test = productDAO.get()
        print(test)


    except Exception as e:
        print(e)