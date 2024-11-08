from fastapi import FastAPI
from src.role.route import role_router

version = "v1"

app = FastAPI(
    title="Attendance System"
    description="A REST API for effective attendance at job site"
    version = version
)

app.include_router(role_router, prefix=f"/api/{version}/roles")