from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_db
from app.crud import crud_program
from app.schemas.schema_program import (
    ProgramCreate,
    ProgramUpdate,
    ProgramResponse,
)

router = APIRouter(
    prefix="/programs",
    tags=["Program"]
)


@router.post("/", response_model=ProgramResponse, status_code=status.HTTP_201_CREATED)
async def create_program(
    payload: ProgramCreate,
    db: AsyncSession = Depends(get_db),
):
    return await crud_program.create_program(
        db=db,
        program_name=payload.program_name,
        school_id=payload.school_id,
    )


@router.get("/{program_id}", response_model=ProgramResponse)
async def get_program(
    program_id: int,
    db: AsyncSession = Depends(get_db),
):
    program = await crud_program.get_program(db, program_id)
    if not program:
        raise HTTPException(status_code=404, detail="Program not found")
    return program


@router.get("/", response_model=list[ProgramResponse])
async def get_programs(
    db: AsyncSession = Depends(get_db),
):
    return await crud_program.get_programs(db)


@router.delete("/{program_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_program(
    program_id: int,
    db: AsyncSession = Depends(get_db),
):
    program = await crud_program.delete_program(db, program_id)
    if not program:
        raise HTTPException(status_code=404, detail="Program not found")
    return None
