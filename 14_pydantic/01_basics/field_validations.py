from pydantic import BaseModel, field_validator, model_validator
class User(BaseModel):
    username:str
    @field_validator("username")
    def username_length(cls, v):
        if len(v)<4:
            raise ValueError("Username must be at least 4 characters long")
        return v
    
class Signup(BaseModel):
    password: str
    confirm_password: str
    @model_validator(mode="after")
    def password_match(cls,value):
        if value.password != value.confirm_password:
            raise ValueError("Password and confirm password do not match")
        return value
    