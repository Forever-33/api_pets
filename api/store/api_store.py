import requests
import allure

from utils.helper import Helper
from api.store.endpoints import Endpoints
from api.store.payloads import Payloads
from config.headers import Headers
from api.store.models.store_model import StoreModel


class StoreAPI(Helper):

    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step("Create Store Order")
    def create_store_order(self):
        response = requests.post(
            url=self.endpoints.create_store_order,
            headers=self.headers.basic,
            json=self.payloads.create_store_order,
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = StoreModel(**response.json())
        print(model)
        return model

    @allure.step("Get Pet by id")
    def get_store_order_by_id(self, id):
        response = requests.get(
            url=self.endpoints.get_store_order_by_id(id),
            headers=self.headers.basic,
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = StoreModel(**response.json())
        print(model)
        return model