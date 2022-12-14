from fastapi import FastAPI
from routes import companyRoutes, clientRoutes

app = FastAPI()

app.include_router(companyRoutes.router)
app.include_router(clientRoutes.router)