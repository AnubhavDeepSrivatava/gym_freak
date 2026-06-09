import socket
from typing import AsyncGenerator
from urllib.parse import urlparse, urlunparse

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker,
)
from app.core.config import settings


def _resolve_ip_uri(db_uri: str) -> str:
    """
    Replace the hostname with a resolved IP (IPv4 preferred, IPv6 fallback).
    Supabase's direct DB host may return only IPv6, which some networks can't route.
    Using the pooler host avoids this, but we still pin to an IP to skip repeated DNS lookups.
    """
    parsed = urlparse(str(db_uri))
    hostname = parsed.hostname
    for family, fmt in [(socket.AF_INET, "{}"), (socket.AF_INET6, "[{}]")]:
        try:
            ip = socket.getaddrinfo(hostname, None, family)[0][4][0]
            netloc = parsed.netloc.replace(hostname, fmt.format(ip))
            return urlunparse(parsed._replace(netloc=netloc))
        except socket.gaierror:
            continue
    return str(db_uri)


resolved_uri = _resolve_ip_uri(str(settings.SQLALCHEMY_DATABASE_URI))

engine = create_async_engine(
    resolved_uri,
    pool_pre_ping=True,
    connect_args={"ssl": "require"},
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session
