from sqlalchemy import Column, BigInteger, String, DateTime, func
from sqlalchemy.orm import declarative_base
from app.models.base import Base as OldBase

# Use the same metadata so Alembic tracks it, but don't inherit the common columns
Base = declarative_base(metadata=OldBase.metadata)

class User(Base):
    __tablename__ = 'users'
    
    id = Column(BigInteger, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    user_name = Column(String)
