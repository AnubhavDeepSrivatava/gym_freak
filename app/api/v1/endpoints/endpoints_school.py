from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_db
from app.crud import crud_school
from app.schemas.schema_school import (
    SchoolCreate,
    SchoolUpdate,
    SchoolResponse,
)

router = APIRouter(
    prefix="/schools",
    tags=["School"]
)


@router.post("/", response_model=SchoolResponse, status_code=status.HTTP_201_CREATED)
async def create_school(
    payload: SchoolCreate,
    db: AsyncSession = Depends(get_db),
):
    return await crud_school.create_school(
        db=db,
        school_name=payload.school_name,
        logo=payload.logo,
    )


@router.get("/{school_id}", response_model=SchoolResponse)
async def get_school(
    school_id: int,
    db: AsyncSession = Depends(get_db),
):
    school = await crud_school.get_school(db, school_id)
    if not school:
        raise HTTPException(status_code=404, detail="School not found")
    return school


@router.get("/", response_model=list[SchoolResponse])
async def get_schools(
    db: AsyncSession = Depends(get_db),
):
    return await crud_school.get_schools(db)


@router.delete("/{school_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_school(
    school_id: int,
    db: AsyncSession = Depends(get_db),
):
    school = await crud_school.delete_school(db, school_id)
    if not school:
        raise HTTPException(status_code=404, detail="School not found")
    return None
