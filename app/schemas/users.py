from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email:str
    

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    hashed_password:str

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email:str
    plain_text_password: str

class UserOut(UserBase):
    pass