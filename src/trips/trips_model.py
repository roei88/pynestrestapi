from pydantic import BaseModel, validator, ValidationError
from datetime import date

class Trip(BaseModel):
    id: str
    owner: str
    label: str
    type: str
    sub_type: str
    destination: str
    start_date: date
    num_of_days: int
    created_at: date
    updated_at: date
    is_deleted: bool

    @validator('id')
    def id_must_not_be_empty(cls, v):
        if not v:
            raise ValueError('id must not be empty')
        return v

    @validator('owner')
    def owner_must_not_be_empty(cls, v):
        if not v:
            raise ValueError('owner must not be empty')
        return v

    @validator('label')
    def label_must_not_be_empty(cls, v):
        if not v:
            raise ValueError('label must not be empty')
        return v

    @validator('type')
    def type_must_not_be_empty(cls, v):
        if not v:
            raise ValueError('type must not be empty')
        return v

    @validator('sub_type')
    def sub_type_must_not_be_empty(cls, v):
        if not v:
            raise ValueError('sub_type must not be empty')
        return v

    @validator('destination')
    def destination_must_not_be_empty(cls, v):
        if not v:
            raise ValueError('destination must not be empty')
        return v

    @validator('start_date')
    def start_date_must_be_in_future(cls, v):
        if v < date.today():
            raise ValueError('start_date must be in the future')
        return v

    @validator('num_of_days')
    def num_of_days_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('num_of_days must be positive')
        return v

    @validator('created_at', 'updated_at')
    def dates_must_be_valid(cls, v):
        if v > date.today():
            raise ValueError('created_at and updated_at must not be in the future')
        return v

    @validator('updated_at')
    def updated_at_must_be_after_created_at(cls, v, values):
        created_at = values.get('created_at')
        if created_at and v < created_at:
            raise ValueError('updated_at must be after created_at')
        return v

    @validator('is_deleted')
    def is_deleted_must_be_boolean(cls, v):
        if not isinstance(v, bool):
            raise ValueError('is_deleted must be a boolean')
        return v