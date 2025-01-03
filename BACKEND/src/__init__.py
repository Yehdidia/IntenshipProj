from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.connection import connect
#from src.connection import init_db
#from src.role.route import role_router

version = "v1"

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    print(f"Server is starting")
    await connect.init_db()
    yield
    # Clean up the ML models and release the resources
    print(f"Server had been stopped")
    

app = FastAPI(
    title="Attendance System",
    description="A REST API for effective attendance at job site",
    version = version,
    lifespan = lifespan
)

#app.include_router(role_router, prefix=f"/api/{version}/roles")