from pydantic import BaseModel, validator
from datetime import datetime
from typing import Optional

class Trip(BaseModel):
    id: str
    owner: Optional[str] = None
    label: Optional[str] = None
    type: Optional[str] = None
    sub_type: Optional[str] = None
    destination: Optional[str] = None
    start_date: Optional[datetime] = None
    num_of_days: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    is_deleted: Optional[bool] = None

    @validator('id')
    def id_must_not_be_empty(cls, v):
        if not v:
            raise ValueError('id must not be empty')
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

    @validator('num_of_days')
    def num_of_days_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('num_of_days must be positive')
        return v
    
    @validator('start_date')
    def start_date_validations(cls, v):
        if v:
            if v < datetime.today():
                raise ValueError('start_date must be in the future')
        return v