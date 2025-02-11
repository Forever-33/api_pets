import allure
import pytest
from config.base_test import BaseTest


@allure.epic("Administration Pet")
@allure.feature("Pet")
class TestPet(BaseTest):

    @pytest.mark.regression
    @allure.title("Create new pet")
    def test_create_pet(self):
        print(self.api_pet.create_pet())

    @pytest.mark.regression
    @allure.title("Get pet by id")
    def test_get_pet_by_id(self):
        pet = self.api_pet.create_pet()
        print(self.api_pet.get_pet_by_id(pet.id))

    @pytest.mark.regression
    @allure.title("Update pet by id")
    def test_update_pet_by_id(self):
        print(self.api_pet.update_pet())

    @pytest.mark.regression
    @allure.title("Delete pet by id")
    def test_delete_pet_by_id(self):
        pet = self.api_pet.create_pet()
        print(self.api_pet.delete_pet_by_id(pet.id))

    @pytest.mark.regression
    @allure.title("Get pet by deleted id")
    def test_get_pet_by_deleted_id(self):
        pet = self.api_pet.create_pet()
        print(self.api_pet.delete_pet_by_id(pet.id))
        print(self.api_pet.get_pet_by_deleted_id(pet.id))

