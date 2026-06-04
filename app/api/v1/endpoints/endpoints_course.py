from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_db
from app.crud import crud_course
from app.schemas.schema_course import (
    CourseCreate,
    CourseUpdate,
    CourseResponse,
)

router = APIRouter(
    prefix="/courses",
    tags=["Course"]
)


@router.post("/", response_model=CourseResponse, status_code=status.HTTP_201_CREATED)
async def create_course(
    payload: CourseCreate,
    db: AsyncSession = Depends(get_db),
):
    return await crud_course.create_course(
        db=db,
        course_name=payload.course_name,
        sequence_number=payload.sequence_number,
        program_id=payload.program_id,
    )


@router.get("/{course_id}", response_model=CourseResponse)
async def get_course(
    course_id: int,
    db: AsyncSession = Depends(get_db),
):
    course = await crud_course.get_course(db, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course


@router.get("/", response_model=list[CourseResponse])
async def get_courses(
    db: AsyncSession = Depends(get_db),
):
    return await crud_course.get_courses(db)


@router.delete("/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_course(
    course_id: int,
    db: AsyncSession = Depends(get_db),
):
    course = await crud_course.delete_course(db, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return None
