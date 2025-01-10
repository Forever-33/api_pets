

BASE_URL = 'https://petstore.swagger.io/v2'


class Endpoints:

    create_pet = f"{BASE_URL}/pet"
    get_pet_by_id = lambda self, id: f"{BASE_URL}/pet/{id}"
    update_pet = f"{BASE_URL}/pet"
    delete_pet_by_id = lambda self, id: f"{BASE_URL}/pet/{id}"
