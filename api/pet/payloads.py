from faker import Faker

fake = Faker()


class Payloads:

    pet_id = fake.random_int(min=1, max=10000)

    create_pet = {
          "id": pet_id,
          "category": {
            "id": pet_id,
            "name": "string"
          },
          "name": fake.name(),
          "photoUrls": [
            "string"
          ],
          "tags": [
            {
              "id": pet_id,
              "name": "string"
            }
          ],
          "status": fake.random_element(elements=("available", "pending", "sold"))
    }

    update_pet = {
        "id": pet_id,
        "category": {
            "id": pet_id,
            "name": "string"
        },
        "name": fake.name_male(),
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": pet_id,
                "name": "string"
            }
        ],
        "status": fake.random_element(elements=("available", "pending", "sold"))
    }
