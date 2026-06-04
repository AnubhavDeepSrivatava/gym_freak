from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.activity import Activity


async def create_activity(
    db: AsyncSession,
    activity_name: str,
    collaboration_link_template: str | None,
    course_id: int,
):
    activity = Activity(
        activity_name=activity_name,
        collaboration_link_template=collaboration_link_template,
        course_id=course_id,
    )
    db.add(activity)
    await db.commit()
    await db.refresh(activity)
    return activity


async def get_activity(db: AsyncSession, activity_id: int):
    result = await db.execute(
        select(Activity).where(Activity.activity_id == activity_id)
    )
    return result.scalar_one_or_none()


async def get_activities(db: AsyncSession):
    result = await db.execute(select(Activity))
    return result.scalars().all()


async def delete_activity(db: AsyncSession, activity_id: int):
    activity = await get_activity(db, activity_id)
    if not activity:
        return None
    await db.delete(activity)
    await db.commit()
    return activity
