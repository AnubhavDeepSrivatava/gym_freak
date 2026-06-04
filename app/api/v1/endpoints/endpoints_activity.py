from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_db
from app.crud import crud_activity
from app.schemas.schema_activity import (
    ActivityCreate,
    ActivityUpdate,
    ActivityResponse,
)

router = APIRouter(
    prefix="/activities",
    tags=["Activity"]
)


@router.post("/", response_model=ActivityResponse, status_code=status.HTTP_201_CREATED)
async def create_activity(
    payload: ActivityCreate,
    db: AsyncSession = Depends(get_db),
):
    return await crud_activity.create_activity(
        db=db,
        activity_name=payload.activity_name,
        collaboration_link_template=payload.collaboration_link_template,
        course_id=payload.course_id,
    )


@router.get("/{activity_id}", response_model=ActivityResponse)
async def get_activity(
    activity_id: int,
    db: AsyncSession = Depends(get_db),
):
    activity = await crud_activity.get_activity(db, activity_id)
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")
    return activity


@router.get("/", response_model=list[ActivityResponse])
async def get_activities(
    db: AsyncSession = Depends(get_db),
):
    return await crud_activity.get_activities(db)


@router.delete("/{activity_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_activity(
    activity_id: int,
    db: AsyncSession = Depends(get_db),
):
    activity = await crud_activity.delete_activity(db, activity_id)
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")
    return None
