from fastapi import APIRouter
from src.schemas.users_schema import SignUpScheam, LoginScheam


user_route = APIRouter(prefix="/user", tags=["User"])


@user_route.post("/")
async def login(user_login:LoginScheam):
    
    return {}