from fastapi import FastAPI
from routes import assignmentRoutes

app = FastAPI()

app.include_router(assignmentRoutes.router)