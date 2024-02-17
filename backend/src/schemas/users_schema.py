import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, EmailStr, SecretStr, validator
from pydantic_extra_types.phone_numbers import PhoneNumber
import pytz


time_zone = pytz.timezone('Asia/Kolkata')



class BaseSchema(BaseModel):
    id:int
    
class BaseNormal(BaseModel):
    created_by:int
    created_at:datetime.datetime = datetime.datetime.now(tz=time_zone)
    updated_at:Optional[datetime.datetime | None] = None
    updated_by:Optional[int | None]

    
class Gender(Enum):
    male:str = "Male"
    female:str = "Female"
    other:str = "Other"
    
    
class SignUpScheam(BaseNormal):
    email:Optional[EmailStr]
    mobile:Optional[PhoneNumber]
    password: SecretStr
    age:int
    gender: Gender
    
    # @validator()
    
class LoginScheam(BaseModel):
    email:Optional[EmailStr | None] = None
    mobile:Optional[PhoneNumber | None]
    password: SecretStr
    password_confirm:SecretStr