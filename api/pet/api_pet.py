import requests
import allure

from utils.helper import Helper
from api.pet.endpoints import Endpoints
from api.pet.payloads import Payloads
from config.headers import Headers
from api.pet.models.pet_model import PetModel


class PetAPI(Helper):

    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step("Create Pet")
    def create_pet(self):
        response = requests.post(
            url=self.endpoints.create_pet,
            headers=self.headers.basic,
            json=self.payloads.create_pet,
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = PetModel(**response.json())
        print(model)
        return model

    @allure.step("Get Pet by id")
    def get_pet_by_id(self, id):
        response = requests.get(
            url=self.endpoints.get_pet_by_id(id),
            headers=self.headers.basic,
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = PetModel(**response.json())
        print(model)
        return model

    @allure.step("Update Pet by id")
    def update_pet(self):
        response = requests.put(
            url=self.endpoints.update_pet,
            headers=self.headers.basic,
            json=self.payloads.update_pet,
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = PetModel(**response.json())
        print(model)
        return model

    @allure.step("Delete Pet by id")
    def delete_pet_by_id(self, id):
        response = requests.delete(
            url=self.endpoints.delete_pet_by_id(id),
            headers=self.headers.basic,
        )
        print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())

    @allure.step("Get Pet by id")
    def get_pet_by_deleted_id(self, id):
        response = requests.get(
            url=self.endpoints.get_pet_by_id(id),
            headers=self.headers.basic,
        )
        print(response.json())
        assert response.status_code == 404, response.json()
        self.attach_response(response.json())

