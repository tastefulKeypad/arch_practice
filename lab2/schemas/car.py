from pydantic import BaseModel

class CarBase(BaseModel):
    """Base schema with common car fields"""
    carClass: int
    price: int
    capacity: int
    name: str

class CarCreate(CarBase):
    """Schema for creating a new car"""
    pass

class CarResponse(CarBase):
    """Schema with car response"""
    id: int
    class Config:
        from_attributes = True
