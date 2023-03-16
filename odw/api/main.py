import time

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


from odw.api.routers import csvs

app = FastAPI(
    title="ODW API",
    version="0.0.1",
    description="Open Data Warehouse API"
)

app.include_router(csvs.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)