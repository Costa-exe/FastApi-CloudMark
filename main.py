from fastapi import FastAPI
from routes import companyRoutes, clientRoutes, company_clientRoutes, assignmentRoutes, assignmentEmployeeRoutes

app = FastAPI()

app.include_router(companyRoutes.router)
app.include_router(clientRoutes.router)
app.include_router(company_clientRoutes.router)
app.include_router(assignmentRoutes.router)
app.include_router(assignmentEmployeeRoutes.router)

