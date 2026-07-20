from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str
    
class User(BaseModel):
    id:int
    name:str
    address:Address
    
address=Address(
    street="123 something",
    city="Hyderabad",
    postal_code="100001"
)

user=User(
    id=1,
    name="Chai Code",
    address=address,
)

user_data={
    "id":1,
    "name":"Chai Code",
    "address":{
        "street":"123 something",
        "city":"Hyderabad",
        "postal_code":"100001"
    }
}

user=User(**user_data)
print(user)