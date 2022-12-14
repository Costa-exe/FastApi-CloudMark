from fastapi import FastAPI
from routes import companyRoutes

app = FastAPI()

app.include_router(companyRoutes.router)