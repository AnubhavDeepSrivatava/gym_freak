from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.core.db import get_db
from app.schemas.user import UserCreate, UserUpdate, UserResponse
from app.services.user_service import UserService

router = APIRouter()

def get_user_service(db: AsyncSession = Depends(get_db)) -> UserService:
    return UserService(db)

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED, summary="Create new user")
async def create_user(
    user_in: UserCreate,
    user_service: UserService = Depends(get_user_service)
):
    return await user_service.create_user(user_in)

@router.get("/", response_model=List[UserResponse], summary="Get all users")
async def read_users(
    skip: int = 0,
    limit: int = 100,
    user_service: UserService = Depends(get_user_service)
):
    return await user_service.get_users(skip=skip, limit=limit)

@router.get("/{user_id}", response_model=UserResponse, summary="Get user by ID")
async def read_user(
    user_id: int,
    user_service: UserService = Depends(get_user_service)
):
    return await user_service.get_user(user_id)

@router.patch("/{user_id}", response_model=UserResponse, summary="Update user")
async def update_user(
    user_id: int,
    user_in: UserUpdate,
    user_service: UserService = Depends(get_user_service)
):
    return await user_service.update_user(user_id, user_in)

@router.delete("/{user_id}", response_model=UserResponse, summary="Delete user")
async def delete_user(
    user_id: int,
    user_service: UserService = Depends(get_user_service)
):
    return await user_service.delete_user(user_id)
