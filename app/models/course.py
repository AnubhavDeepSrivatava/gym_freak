from sqlalchemy import Column, Integer, String, ForeignKey
from app.models.base import Base   # ✅ changed import

class Course(Base):
    __tablename__ = "courses"

    course_id = Column(Integer, primary_key=True, index=True)
    course_name = Column(String, nullable=False)
    sequence_number = Column(Integer, nullable=False)
    program_id = Column(Integer, ForeignKey("programs.program_id"), nullable=False)
