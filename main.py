from fastapi import FastAPI
from routes import assignmentRoutes, assignmentEmployeeRoutes

app = FastAPI()

app.include_router(assignmentRoutes.router)
app.include_router(assignmentEmployeeRoutes.router)