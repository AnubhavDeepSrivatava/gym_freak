
from pydantic import BaseModel
from typing import Optional


# Used when creating a program (POST)
class ProgramCreate(BaseModel):
    program_name: str
    school_id: int


# Used when updating a program (PUT/PATCH)
class ProgramUpdate(BaseModel):
    program_name: Optional[str] = None
    school_id: Optional[int] = None


# Used when returning program data (GET response)
class ProgramResponse(BaseModel):
    program_id: int
    program_name: str
    school_id: int

    class Config:
        from_attributes = True
