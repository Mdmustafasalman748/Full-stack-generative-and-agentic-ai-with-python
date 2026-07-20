from pydantic import BaseModel, Field
from typing import Optional
import re

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Employee name",
        example="Chai code"
    )
    
    department:Optional[str]='General'
    salary:float=Field(
        ...,
        gt=10000,
        le=1000000,
        description="Annual Employee salary in USD"
    )
    
class User(BaseModel):
    email:str=Field(
        ...,
        regex=r'',
    )
    age=int=Field(
        ...,
        gt=0,
        le=150,
        description="User age in years"
    )
    phone: str = Field(
        ...,
        regex=r''
    )
    discount:float=Field(
        ...,
        gt=0,
        le=100,
        description="Discount percentage"
    )