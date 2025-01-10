from pydantic import BaseModel, field_validator


class BaseValidator(BaseModel):
    @field_validator("*")
    def fields_are_not_empty(cls, value, field):
        if value == "" or value is None:
            raise ValueError(f"Поле {field.name} пустое")
        return value


class CategoryModel(BaseModel):
    id: int
    name: str


class TagsModel(BaseModel):
    id: int
    name: str


class PetModel(BaseModel):
    id: int
    category: CategoryModel
    name: str
    photoUrls: list
    tags: list[TagsModel]
    status: str

