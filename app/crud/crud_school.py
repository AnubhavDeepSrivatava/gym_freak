from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.school import School


async def create_school(db: AsyncSession, school_name: str, logo: str | None = None):
    school = School(school_name=school_name, logo=logo)
    db.add(school)
    await db.commit()
    await db.refresh(school)
    return school


async def get_school(db: AsyncSession, school_id: int):
    result = await db.execute(
        select(School).where(School.school_id == school_id)
    )
    return result.scalar_one_or_none()


async def get_schools(db: AsyncSession):
    result = await db.execute(select(School))
    return result.scalars().all()


async def delete_school(db: AsyncSession, school_id: int):
    school = await get_school(db, school_id)
    if not school:
        return None
    await db.delete(school)
    await db.commit()
    return school
