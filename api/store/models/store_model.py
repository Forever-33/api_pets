from pydantic import BaseModel, field_validator


class BaseValidator(BaseModel):
    @field_validator("*")
    def fields_are_not_empty(cls, value, field):
        if value == "" or value is None:
            raise ValueError(f"Поле {field.name} пустое")
        return value


class StoreModel(BaseModel):
    id: int
    petId: int
    quantity: int
    shipDate: str
    status: str
    complete: bool


