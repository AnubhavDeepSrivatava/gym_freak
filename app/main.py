from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from my_company_core.logging import setup_logging
# from my_company_core.middleware import add_standard_middleware
from app.api.v1.api import api_router
from app.core.config import settings

def create_application() -> FastAPI:
    application = FastAPI(
        title=settings.PROJECT_NAME,
        openapi_url=f"{settings.API_V1_STR}/openapi.json"
    )
    
    # Set all CORS enabled origins
    if settings.BACKEND_CORS_ORIGINS:
        application.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    # Standardized setup from your shared library
    # setup_logging()
    # add_standard_middleware(application)
    
    application.include_router(api_router, prefix=settings.API_V1_STR)
    return application

app = create_application()
