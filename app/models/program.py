from sqlalchemy import Column, Integer, String, ForeignKey
from app.models.base import Base   # ✅ changed import

class Program(Base):
    __tablename__ = "programs"

    program_id = Column(Integer, primary_key=True, index=True)
    program_name = Column(String, nullable=False)
    school_id = Column(Integer, ForeignKey("schools.school_id"), nullable=False)
