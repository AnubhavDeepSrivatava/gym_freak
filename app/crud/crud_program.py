from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.program import Program


async def create_program(db: AsyncSession, program_name: str, school_id: int):
    program = Program(program_name=program_name, school_id=school_id)
    db.add(program)
    await db.commit()
    await db.refresh(program)
    return program


async def get_program(db: AsyncSession, program_id: int):
    result = await db.execute(
        select(Program).where(Program.program_id == program_id)
    )
    return result.scalar_one_or_none()


async def get_programs(db: AsyncSession):
    result = await db.execute(select(Program))
    return result.scalars().all()


async def delete_program(db: AsyncSession, program_id: int):
    program = await get_program(db, program_id)
    if not program:
        return None
    await db.delete(program)
    await db.commit()
    return program
