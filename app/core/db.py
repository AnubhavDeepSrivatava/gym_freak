from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker,
)
from app.core.config import settings

# ASYNC engine (asyncpg)
engine = create_async_engine(
    str(settings.SQLALCHEMY_DATABASE_URI),
    pool_pre_ping=True,
)

# ASYNC session factory
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)

# ✅ THIS WAS MISSING
async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
