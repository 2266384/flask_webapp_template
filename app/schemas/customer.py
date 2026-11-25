from pydantic import BaseModel, ConfigDict, EmailStr, Field


class CustomerSchema(BaseModel):
    """Customer response schema"""

    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str = Field(min_length=2, max_length=200)
    email: EmailStr


class CustomerCreateSchema(BaseModel):
    """Schema for creating a customer"""

    name: str = Field(min_length=2, max_length=200)
    email: EmailStr


class CustomerUpdateSchema(BaseModel):
    """Schema for cupdating a customer"""

    name: str | None = Field(default=None, min_length=2, max_length=200)
    email: EmailStr | None = None
