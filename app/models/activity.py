from sqlalchemy import Column, Integer, String, ForeignKey
from app.models.base import Base

class Activity(Base):
    __tablename__ = "activities"

    activity_id = Column(Integer, primary_key=True, index=True)
    activity_name = Column(String, nullable=False)
    collaboration_link_template = Column(String, nullable=True)
    course_id = Column(Integer, ForeignKey("courses.course_id"), nullable=False)
