from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.course import Course


async def create_course(
    db: AsyncSession,
    course_name: str,
    sequence_number: int,
    program_id: int
):
    course = Course(
        course_name=course_name,
        sequence_number=sequence_number,
        program_id=program_id,
    )
    db.add(course)
    await db.commit()
    await db.refresh(course)
    return course


async def get_course(db: AsyncSession, course_id: int):
    result = await db.execute(
        select(Course).where(Course.course_id == course_id)
    )
    return result.scalar_one_or_none()


async def get_courses(db: AsyncSession):
    result = await db.execute(select(Course))
    return result.scalars().all()


async def delete_course(db: AsyncSession, course_id: int):
    course = await get_course(db, course_id)
    if not course:
        return None
    await db.delete(course)
    await db.commit()
    return course
