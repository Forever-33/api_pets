import allure
import pytest
from config.base_test import BaseTest


@allure.epic("Administration Order Store")
@allure.feature("Store")
class TestStore(BaseTest):

    @pytest.mark.regression
    @allure.title("Create new order store")
    def test_create_order_store(self):
        order_store = self.api_store.create_store_order()
        print(self.api_store.get_store_order_by_id(order_store.id))

