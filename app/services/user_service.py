from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from app.crud.crud_user import user as crud_user
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from fastapi import HTTPException, status

class UserService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_user(self, user_id: int) -> User:
        user = await crud_user.get(self.db, id=user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return user

    async def get_users(self, skip: int = 0, limit: int = 100) -> List[User]:
        return await crud_user.get_multi(self.db, skip=skip, limit=limit)

    async def create_user(self, user_in: UserCreate) -> User:
        return await crud_user.create(self.db, obj_in=user_in)

    async def update_user(self, user_id: int, user_in: UserUpdate) -> User:
        user = await self.get_user(user_id)
        return await crud_user.update(self.db, db_obj=user, obj_in=user_in)

    async def delete_user(self, user_id: int) -> User:
        user = await self.get_user(user_id)
        return await crud_user.remove(self.db, id=user_id)
