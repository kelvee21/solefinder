from pydantic import BaseModel, EmailStr, Field


class MerchantIn(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr


class MerchantOut(MerchantIn):
    id: int


class ShoeIn(BaseModel):
    brand: str = Field(min_length=1, max_length=60)
    model: str = Field(min_length=1, max_length=100)
    price: float = Field(gt=0)


class ShoeOut(ShoeIn):
    id: int