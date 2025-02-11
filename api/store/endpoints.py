

BASE_URL = 'https://petstore.swagger.io/v2'


class Endpoints:

    create_store_order = f"{BASE_URL}/store/order"
    get_store_order_by_id = lambda self, id: f"{BASE_URL}/store/order/{id}"
