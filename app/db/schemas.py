from pydantic import BaseModel, EmailStr, Field


class MerchantIn(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr


class MerchantOut(MerchantIn):
    id: int