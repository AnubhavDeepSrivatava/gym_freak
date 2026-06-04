from sqlalchemy import Column, Integer, String
from app.models.base import Base   # ✅ changed import

class School(Base):
    __tablename__ = "schools"

    school_id = Column(Integer, primary_key=True, index=True)
    school_name = Column(String, nullable=False)
    logo = Column(String, nullable=True)
