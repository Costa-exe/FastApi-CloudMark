from fastapi import FastAPI
from routes import companyRoutes, clientRoutes, company_clientRoutes

app = FastAPI()

app.include_router(companyRoutes.router)
app.include_router(clientRoutes.router)
app.include_router(company_clientRoutes.router)