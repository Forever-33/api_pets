from api.pet.api_pet import PetAPI
from api.store.api_store import StoreAPI


class BaseTest:

    def setup_method(self):
        self.api_pet = PetAPI()
        self.api_store = StoreAPI()
