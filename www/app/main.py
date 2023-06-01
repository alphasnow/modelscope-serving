from app.errors import http_error_handler, http422_error_handler, error_handler
from app.events import create_start_app_handler, create_stop_app_handler
from app.routers.routers import routers
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException

app = FastAPI(
    title="ModelScopeServing",
    description="Build AI model service based on ModelScope",
    version="0.0.1",
    debug=False
)

# Enable CORS.
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# exception
app.add_exception_handler(HTTPException, http_error_handler)
app.add_exception_handler(RequestValidationError, http422_error_handler)
app.add_exception_handler(Exception, error_handler)

# event
app.add_event_handler(
    "startup",
    create_start_app_handler(app),
)
app.add_event_handler(
    "shutdown",
    create_stop_app_handler(app),
)

app.include_router(routers)
