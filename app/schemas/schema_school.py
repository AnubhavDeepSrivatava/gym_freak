from pydantic import BaseModel
from typing import Optional


# Used when creating a school (POST)
class SchoolCreate(BaseModel):
    school_name: str
    logo: Optional[str] = None


# Used when updating a school (PUT/PATCH)
class SchoolUpdate(BaseModel):
    school_name: Optional[str] = None
    logo: Optional[str] = None


# Used when returning school data (GET response)
class SchoolResponse(BaseModel):
    school_id: int
    school_name: str
    logo: Optional[str]

    class Config:
        from_attributes = True
