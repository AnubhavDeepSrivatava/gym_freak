from fastapi import FastAPI
# from my_company_core.logging import setup_logging
# from my_company_core.middleware import add_standard_middleware
from app.api.v1.api import api_router
from app.core.config import settings

def create_application() -> FastAPI:
    application = FastAPI(
        title=settings.PROJECT_NAME,
        openapi_url=f"{settings.API_V1_STR}/openapi.json"
    )
    
    # Standardized setup from your shared library
    # setup_logging()
    # add_standard_middleware(application)
    
    application.include_router(api_router, prefix=settings.API_V1_STR)
    return application

app = create_application()
