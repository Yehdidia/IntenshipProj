from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
#from src import project_data.py
#from src.role.schemas import Role, RoleUpdateModel
from typing import List

role_router = APIRouter()

@role_router.get("/", response_model=List[Role])
async def get_all_roles():
    pass
