from faker import Faker

fake = Faker()


class Payloads:

    order_id = fake.random_int(min=1, max=10000)

    create_store_order = {
      "id": order_id,
      "petId": fake.random_int(min=1, max=10000),
      "quantity": fake.random_int(min=1, max=10000),
      "shipDate": fake.iso8601(tzinfo=None),
      "status": "placed",
      "complete": True
    }